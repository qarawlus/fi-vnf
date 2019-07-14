import argparse
import spamvnf.reader.reader as reader
import netfilterqueue
from scapy.all import TCP, IP


class Spam_VNF:
    def __init__(self, filter_file):
        self.emails, self.websites, self.subjects = \
            reader.read_dict_file(filter_file)

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
        # TODO: Possibility of Queueing packets

    def check_email(self, text):
        """
        Email Filter
        Returns False if checks failed (email is spam)
        """

        # Filtering the sender address
        sender_address_op1 = list(filter(lambda i: "From:" in i, text))
        sender_address_op2 = sender_address_op1[0].strip()
        sender_address_op3 = sender_address_op2.split("From: ")[1]
        sender_email = sender_address_op3.rstrip().replace('\\n\\', '')
        # print("sender_email:",sender_email)
        # Fetching domain name
        domain_name = sender_email.split("@")[1]
        # print("domain_name:",domain_name)
        # Finding email server
        # email_server_op1 = list(filter(lambda k: "Received: from " in k, text))
        # email_server_op2 = email_server_op1[0]
        # email_server_op3 = email_server_op2.split("Received: from ")[1]
        # email_server = email_server_op3.split(" ")[0]
        # print("email_server:",email_server)
        # Filtering subject line
        subject_op1 = list(filter(lambda j: "Subject:" in j, text))
        subject_op2 = subject_op1[0].strip()
        subject_op3 = subject_op2.split("Subject: ")[1]
        subject_email = subject_op3.rstrip().replace('\\n\\', '')
        # print("subject:",subject_email)
        # Check if sender domain in dict of domains
        if domain_name in self.websites:
            return False
        elif subject_email in self.subjects:
            return False
        elif sender_email in self.emails:
            return False
        else:
            return True


def main():
    """
    Runs the main VNF
    """
    args = parse_args()
    filter_file = args.dict_file
    vnf = Spam_VNF(filter_file)
    print
    nfqueue = netfilterqueue.NetfilterQueue()
    nfqueue.bind(1, vnf.handle_packet)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('VNF Quitted')
    nfqueue.unbind()


def parse_args():
    """
    Parse cli arguments
    """
    args = argparse.ArgumentParser("VNF Devs Spam Filter")
    args.add_argument('-d', '--dict', dest='dict_file',
                      help='Dictionary file', required=True)
    return args.parse_args()
