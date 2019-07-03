import yaml
import argparse
import spamvnf.reader.reader as reader
import netfilterqueue
from scapy.all import *

DICT_FILE = None

def parse_args():
    """
    Parse cli arguments
    """
    args = argparse.ArgumentParser("VNF Devs Spam Filter")
    args.add_argument('-d', '--dict', dest='dict_file', help='Dictionary file', required=True)

    return args.parse_args()

   
def main():
    # arguments = parse_args() 
    # DICT_FILE = arguments.dict_file
    
    
    nfqueue = netfilterqueue.NetfilterQueue()
    nfqueue.bind(1,handle_packet)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('VNF Quitted')
    nfqueue.unbind()


def handle_packet(pkt: netfilterqueue.Packet):
    
    # email, websites = reader.read_dict_file(DICT_FILE)
    packet = IP(pkt.get_payload())
    print(packet.show())
    pkt.accept()
    # send(IP(src="10.0.99.100",dst="10.1.99.100")/ICMP()/"Hello World")