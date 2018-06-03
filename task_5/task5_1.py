from ftplib import FTP
import gzip
import os

zip_name = 'ratings.list.gz'

if not os.path.isfile(zip_name):
    ftp_connection = FTP('ftp.fu-berlin.de')
    ftp_connection.login()
    ftp_connection.cwd('/pub/misc/movies/database/frozendata/')
    file_stream = open(zip_name, 'wb')
    ftp_connection.retrbinary('RETR ' + zip_name, file_stream.write)
    file_stream.close()

zip_file = gzip.GzipFile(zip_name, 'rb')
zip_file_stream = zip_file.read()
txt_file = open(zip_name + '.txt', 'wb')
txt_file.write(zip_file_stream)

zip_file.close()
txt_file.close()
