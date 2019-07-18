import argparse
import spamvnf.reader.reader as reader
import netfilterqueue
from scapy.all import TCP, IP
import re
import time


class Spam_VNF:

    def __init__(self, filter_file):
        self.emails, self.servers, self.subjects = \
            reader.read_dict_file(filter_file)
        self.packet_processed = 0

    def handle_packet(self, pkt: netfilterqueue.Packet):
        """
        Callback function to handle the packets passed by NFQueue
        """
        packet = IP(pkt.get_payload())
        payload = str(packet[TCP].payload)

        if self.check_email(payload):
            print("Packet accepted")
            pkt.accept()
        else:
            print("Packet dropped")
            pkt.drop()
        self.packet_processed += 1
        # TODO: Possibility of Queueing packets

    def check_email(self, text):
        """
        Email Filter
        Returns False if checks failed (email is spam)
        """

        sender_re = r"(.*)(From:\s)([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
        server_re = r"(.*)(Received: from\s)([a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
        subject_re = r"(.*)(Subject:\s)([a-zA-Z0-9._\s-]+)"

        sender = re.search(sender_re, text)
        server = re.findall(server_re, text)
        subject = re.search(subject_re, text)
        # Fetching sender email
        if sender:
            sender_email = sender.group(3)
            if sender_email in self.emails:
                return False
        # Fetching server address
        if len(server) > 0:
            server_name = server[-1]
            server_address = server_name[2]
            if server_address in self.servers:
                return False

        # Fetching subject
        if subject:
            subject_line = subject.group(3)
            print(subject_line)
            if subject_line in self.subjects:
                return False

        return True


def main():
    """
    Runs the main VNF
    """
    start_time = time.time()
    args = parse_args()
    filter_file = args.dict_file
    vnf = Spam_VNF(filter_file)
    nfqueue = netfilterqueue.NetfilterQueue()
    nfqueue.bind(1, vnf.handle_packet)
    print('Spam VNF running')
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('VNF Quitted')
        duration = time.time() - start_time
        print(f'Packets processed in {duration} seconds= {vnf.packet_processed}')
    nfqueue.unbind()


def parse_args():
    """
    Parse cli arguments
    """
    args = argparse.ArgumentParser("VNF Devs Spam Filter")
    args.add_argument('-d', '--dict', dest='dict_file',
                      help='Dictionary file', required=True)
    return args.parse_args()
