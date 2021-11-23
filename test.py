import sqlite3

con = sqlite3.connect("banking.db")
db = con.cursor()

rows = db.execute("SELECT * FROM users WHERE username = ?", ("justin",))

# print(rows)
user = rows.fetchone()
# print(rows.fetchone())
print(user[2])
# print(len(rows.fetchone()))
# print(rows.fetchall())


# # print(rows.fetchall()[0][2])

# print(len(rows.fetchall()))

con.commit()
con.close()