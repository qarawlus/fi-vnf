"""
YAML File Reader helper module
"""
import yaml


def read_dict_file(file):
    """
    Reads the yaml spam filter file. Return list of emails, server, subject lists
    """
    with open(file) as data:
        data = yaml.load(data, Loader=yaml.FullLoader)
    email_list = []
    server_list = []
    subject_list = []
    for email in data['emails']:
        email_list.append(email)
    for server in data['servers']:
        server_list.append(server)
    for subject in data['subjects']:
        subject_list.append(subject)
    return email_list, server_list, subject_list
