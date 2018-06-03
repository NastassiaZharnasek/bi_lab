import argparse
import os.path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--year',
                    help='Displays Top250 movies titles with year')
parser.add_argument('--rate',
                    help='Displays Top250 movies titles with rate',
                    default=True)
parser.add_argument('--all',
                    help='Shows title, rate, year')
parser.add_argument('--histogram',
                    help='Displays histogram for rating or for '
                         'years (in text format)',
                    default='rating')
parser.add_argument('--output',
                    help='Stores data to specified filename file')
args = parser.parse_args()

filename = 'IMDB-ratings.csv'


def read_csv_file(file_name):
    return pd.read_csv(file_name)


def create_output(output):
    if args.output:
        result_imdb_data.to_csv(args.output)
    else:
        print(output)


if not os.path.exists(filename):
    print('File does not exist!')
else:
    imdb_data = read_csv_file(filename)
    if args.year:
        sorted_imdb_data = imdb_data.sort_values(by=['Year', 'Title'],
                                                 ascending=[False, True])[:250]
        result_imdb_data = sorted_imdb_data[['Title', 'Year']]
        create_output(result_imdb_data)
    if args.rate:
        sorted_imdb_data = imdb_data.sort_values(by=['Rating', 'Title'],
                                                 ascending=[False, True])[:250]
        result_imdb_data = sorted_imdb_data[['Title', 'Rating']]
        create_output(result_imdb_data)
    if args.all:
        result_imdb_data = imdb_data[['Title', 'Rating', 'Year']]
        create_output(result_imdb_data)
    if args.histogram == 'rating':
        grouped_imdb_data = imdb_data.groupby('Rating')['Rating'].count()
        result_imdb_data = grouped_imdb_data.sort_index(ascending=False)
        create_output(result_imdb_data)
    if args.histogram == 'year':
        grouped_imdb_data = imdb_data.groupby('Year')['Year'].count()
        result_imdb_data = grouped_imdb_data.sort_index(ascending=False)
        create_output(result_imdb_data)
