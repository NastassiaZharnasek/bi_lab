import csv
from pathlib import Path

# read from file
films_list = []
path = Path("IMDB-Movie-Data.csv")
try:
    with open(path, 'r') as films_file:
        read_from_file = csv.DictReader(films_file)
        for line in read_from_file:
            films_list.append({'Title': line['Title'], 'Year': line['Year'],
                               'Rating': line['Rating']})
        films_file.close()
except FileNotFoundError:
    print("Error: file does not exists")
print(films_list)

# top 250 films by rating
top_by_rating = []
for i in films_list:
    top_by_rating.append({'Title': i['Title'], 'Rating': i['Rating']})
top_by_rating.sort(key=lambda films_list: films_list['Rating'], reverse=True)
with open('top_250_film_by_rating.csv', 'w', newline='') as top_by_rating_file:
    writer = csv.DictWriter(top_by_rating_file, ['Title', 'Rating'])
    writer.writeheader()
    writer.writerows(top_by_rating[:250])
top_by_rating_file.close()

# rating_by_years
rating_by_years = {}
for i in films_list:
    res = rating_by_years.get(i['Year'], [0, 0.0])
    res[0] += 1
    res[1] += float(i['Rating'])
    rating_by_years[i['Year']] = res

avg_rating = {}
for i, j in rating_by_years.items():
    avg_rating[i] = j[1] / j[0]
with open('avg_rating_by_years.csv', 'w', newline='') as rating_by_years_file:
    writer = csv.DictWriter(rating_by_years_file, ['Year', 'Rating'])
    writer.writeheader()
    for i, j in avg_rating.items():
        writer.writerow({"Year": i, "Rating": j})
rating_by_years_file.close()
