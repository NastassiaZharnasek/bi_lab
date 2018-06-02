import argparse
from ftplib import FTP

import os.path

imdb_data_url = 'www.kaggle.com/PromptCloudHQ/imdb-data_xml/' \
                'downloads/imdb-data_xml-from-2006-to-2016.zip'

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--url', default=imdb_data_url)

args = argument_parser.parse_args()
url = args.url

host = url[:url.find('/'):]
full_folder_name = url[url.find('/'):url.rfind('/'):]
file_name = url[url.rfind('/') + 1::]

file_name_with_directory = os.path.join(r'd:\task_5', file_name)

if not os.path.exists(file_name):
    ftp_connection = FTP(host, timeout=150)
    ftp_connection.login()
    ftp_connection.cwd(full_folder_name)
    file_stream = open(file_name_with_directory, 'wb')
    ftp_connection.retrbinary('RETR ' + file_name, file_stream.write)
    file_stream.close()
