import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
cur.execute("create table if not exists Student(Name text,roll num int ,Section text)")
con.commit()
cur.execute('insert into Student values("sai",12,"a")')
con.commit()
data=cur.execute('select * from Student')
print(data.fetchall())
con.rollback()
con.close()