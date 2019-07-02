import yaml
import argparse
import spamvnf.reader.reader as reader
import nfqueue



def parse_args():
    """
    Parse cli arguments
    """
    args = argparse.ArgumentParser("VNF Devs Spam Filter")
    args.add_argument('-d', '--dict', dest='dict_file', help='Dictionary file', required=True)

    return args.parse_args()

   
def main():
    arguments = parse_args() 
    dict_file = arguments.dict_file
    email, websites = reader.read_dict_file(dict_file)

