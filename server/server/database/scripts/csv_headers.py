import os

for f in os.listdir():
    if f.endswith("csv"):
        #print(f)
        if f.startswith("game_"):
            with open(f, newline='', encoding='utf-8') as csvfile:
                print('CREATE TABLE IF NOT EXISTS {} ('.format(f.split('.')[0]))
                ks = csvfile.readline().split(',')
                print("\t{} INTEGER NOT NULL,".format(ks[0].rstrip()))
                print("\t{} INTEGER NOT NULL,".format(ks[1].rstrip()))
                print("\tFOREIGN KEY ({})".format(ks[0].rstrip()))
                print("\t\tREFERENCES {} ({}),".format( "games", ks[0].rstrip() ))
                print("\tFOREIGN KEY ({})".format(ks[1].rstrip()))
                print("\t\tREFERENCES {} ({})".format( f.split(".")[0].split("game_")[1], ks[1].rstrip() ))
                print(');\n')
        else:
            with open(f, newline='', encoding='utf-8') as csvfile:
                print('CREATE TABLE IF NOT EXISTS {} ('.format(f.split('.')[0]))
                ks = csvfile.readline().split(',')
                print("\t{} INTEGER PRIMARY KEY,".format(ks[0].rstrip()))
                for k in ks[1:-1]:
                    print("\t{} TEXT NOT NULL,".format(k.rstrip()))
                print("\t{} TEXT NOT NULL".format(ks[-1].rstrip()))

                print(');\n')


