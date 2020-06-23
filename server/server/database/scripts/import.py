import csv, sqlite3, os, itertools

con = sqlite3.connect("./mista.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
# cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

for f in os.listdir():
    if f.endswith("csv"):
        if f.startswith("game_"):
            with open(f,'r', encoding='utf-8', newline='') as csvfile: # `with` statement available in 2.5+
                # csv.DictReader uses first line in file for column headings by default
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                cols = [row for row in itertools.islice(reader, 1)] 
                to_db = [(row[0], row[1]) for row in reader]
                # print(to_db)
                f_name = f.split('.')[0]
                print("INSERT INTO {} ({}) VALUES (?, ?);".format(f_name, ",".join(cols[0])) )
                cur.executemany("INSERT INTO {} ({}) VALUES (?, ?);".format(f_name, ",".join(cols[0])), to_db)


# print(to_db)

# cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()
