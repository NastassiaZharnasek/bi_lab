import argparse
import csv
import json
import os
import urllib.request
import xml.etree.cElementTree as et
import xmltodict
import yaml


def convert_to_csv(file_name, data_to_convert):
    file = open(file_name + '.csv', 'w')
    csv_writer = csv.writer(file)

    tree = et.fromstring(data_to_convert)
    plants = tree.findall('PLANT')
    header_elements = []
    for child in plants[0]:
        header_elements.append(child.tag)

    csv_writer.writerow(header_elements)

    for plant in plants:
        plant_params = []
        for header_element in header_elements:
            plant_params.append(plant.find(header_element).text)
        csv_writer.writerow(plant_params)


def convert_to_json(file_name, data_to_convert):
    file = open(file_name + '.json', 'w')
    json.dump(xmltodict.parse(data_to_convert), file)


def convert_to_yml(file_name, data_to_convert):
    file = open(file_name + '.yml', 'w')
    yaml.dump(data_to_convert, file, default_flow_style=False)


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--url',
                             default='https://www.w3schools.com/xml/'
                                     'plant_catalog.xml')

args = argument_parser.parse_args()
url = args.url

content = urllib.request.urlopen(url)
data_xml = str(content.read(), 'utf-8')

file_name_with_directory = os.path.join(r'd:\task_5', 'result')

convert_to_yml(file_name_with_directory, data_xml)
convert_to_json(file_name_with_directory, data_xml)
convert_to_csv(file_name_with_directory, data_xml)
