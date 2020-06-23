import csv

with open('games.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
        # print(row['first_name'], row['last_name'])
    game_developers = { row['id']:row['developer'] for row in reader}

developers_set = set()

for game in game_developers:
    for developer in game_developers[game].split(','):
        developers_set.add(developer)


developers_list = list(developers_set)


with open('developers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['developer_id', 'developer_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(developers_list)):
        writer.writerow({'developer_id': i+1, 'developer_name': developers_list[i]})


with open('developers.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    developers = {rows['developer_name']:rows['developer_id'] for rows in reader}

'''
print(developers)
for game in game_developers:
    for developer in game_developers[game].split(','):
        print(game, developers[developer])
'''

with open('game_developers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['game_id', 'developer_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for game in game_developers:
        for developer in game_developers[game].split(','):
            writer.writerow({'game_id':game, 'developer_id':developers[developer]})
