import argparse
import csv
import json
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
    yaml.dump(xmltodict.parse(data_to_convert), file, default_flow_style=False)


def convert_to_xml(file_name, data_to_convert):
    xml_data = str(data_to_convert.read(), 'utf-8')
    file = open(file_name + '.xml', 'w')
    file.write(xml_data)
    return xml_data


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--url',
                             default='https://www.w3schools.com/xml/'
                                     'plant_catalog.xml')

args = argument_parser.parse_args()
url = args.url
result_file_name = 'result'

content = urllib.request.urlopen(url)
data_xml = convert_to_xml(result_file_name, content)
convert_to_yml(result_file_name, data_xml)
convert_to_json(result_file_name, data_xml)
convert_to_csv(result_file_name, data_xml)
