import csv

with open("movie_links.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    headers_links = data[0]
    allMovies_links = data[1:]


with open("movies.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    header = data[0]
    allMovies = data[1:]

movies = []

header.append('posterlink')

for movie in allMovies:
    for movie_link in allMovies_links:
        if movie[8] == movie_link[0]:
            movie.append(movie_link[1])
            movies.append(movie)
            break

with open('merged.csv','a+',encoding="utf8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(movies)