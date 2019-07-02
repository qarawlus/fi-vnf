"""
YAML File Reader helper module
"""
import yaml


def read_dict_file(file):
    with open(file) as data:
        data = yaml.load(data, Loader=yaml.FullLoader)
    email_list = []
    website_list = []
    for email in data['emails']:
        email_list.append(email)
    for website in data['websites']:
        website_list.append(website)
    return email_list, website_list
