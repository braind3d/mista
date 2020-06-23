import csv
import itertools

with open('genres_by_id2.txt', newline='') as f:
    reader = csv.reader(f, delimiter = '	')
    skipFirst = itertools.islice(reader, 1, None)
    games = {rows[0]:rows[1].split(',') for rows in skipFirst}

# print(games)

with open('genres.csv', mode='r') as infile:
    reader = csv.reader(infile)
    genres = {rows[1]:rows[0] for rows in reader}

#print(genres)

'''
genres_list = list(genres)

with open('genres.csv', 'w', newline='') as csvfile:
    fieldnames = ['genre_id', 'genre_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(genres_list)):
        writer.writerow({'genre_id': i+1, 'genre_name': genres_list[i]})
'''  
'''
for game in games:
        for genre in games[game]:
            print(game, genres[genre])
'''
with open('game_genres.csv', 'w', newline='') as csvfile:
    fieldnames = ['game_id', 'genre_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for game in games:
        for genre in games[game]:
            writer.writerow({'game_id': game, 'genre_id': genres[genre]})