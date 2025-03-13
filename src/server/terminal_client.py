
from sql import SQL

# load the database
db = SQL()

# get all the hosts
hosts = db.fetch_all()

# print the hosts
for host in hosts:
    print(f"{host[0]}: {host[1]}")

# close the database
db.close()
