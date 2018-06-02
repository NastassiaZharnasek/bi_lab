import FTP
import gzip
import os

zip_name = 'ratings.list.gz'
result_file_name = os.path.join(r'd:\task_5', zip_name)

if not os.path.isfile(result_file_name):
    ftp_connection = FTP('fu-berlin.de')
    ftp_connection.login()
    ftp_connection.cwd('/pub/misc/movies/database/frozendata/')
    file_stream = open(result_file_name, 'wb')
    ftp_connection.retrbinary('RETR ' + zip_name, file_stream.write)
    file_stream.close()

zip_file = gzip.GzipFile(result_file_name, 'rb')
zip_file_stream = zip_file.read()
txt_file = open(result_file_name + '.txt', 'wb')
txt_file.write(zip_file_stream)

zip_file.close()
txt_file.close()
