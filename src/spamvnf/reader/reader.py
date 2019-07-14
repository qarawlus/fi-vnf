"""
YAML File Reader helper module
"""
import yaml


def read_dict_file(file):
    """
    Reads the yaml spam filter file. Return list of emails, websites, subject lists
    """
    with open(file) as data:
        data = yaml.load(data, Loader=yaml.FullLoader)
    email_list = []
    website_list = []
    subject_list = []
    for email in data['emails']:
        email_list.append(email)
    for website in data['websites']:
        website_list.append(website)
    for subject in data['subjects']:
        website_list.append(subject)
    return email_list, website_list, subject_list
