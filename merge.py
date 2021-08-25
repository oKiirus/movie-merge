import csv

f = open('movies.csv', encoding="utf8")
file = csv.reader(f)
data = list(file)

headers = data[0]
movies = data[1:]
headers.append('poster_link')

f = open('final.csv', 'a+', encoding="utf8")
file = csv.writer(f)

file.writerow(headers)

f = open('movie_links.csv', encoding="utf8")
file = csv.reader(f)
data = list(file)
links = data[1:]


for i in movies:
    poster = any(i[8] in j for j in links)
    if poster:
        for j in links:
            if i[8] ==  j[0]:
                i.append(j[1])
                f = open('final.csv', 'a+', encoding="utf8")
                file = csv.writer(f)
                file.writerow(i)
                    
    