import sqlite3

# creating .db file
conn = sqlite3.connect('orders.db')

# object storage
cur = conn.cursor()

# 1) Method execute creates table
# 2) If there is no table, create it
# 3) Create the first four columns: userid, firstname, lastname and gender. Userid is the main key.
# 4) Method .commit saves changes

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   firstname TEXT,
   lastname TEXT,
   gender TEXT);
""")
conn.commit()

# similarly with the table of orders
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

# adding info to the user's table (I way)
cur.execute("""INSERT INTO users(userid, firstname, lastname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()

# adding info to the user's table (I way)
user = ('00002', 'Lois', 'Lane', 'Female')
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()