import sqlite3
con=sqlite3.connect("user_register.db")
cur=con.cursor()
cur.execute("create table if not exists User_reg( user_id INTEGER PRIMARY KEY AUTOINCREMENT, User_name VARCHAR(200),Password VARCHAR(200),active TEXT NOT NULL)")
con.commit()
def insert(username,password):
    active = 'True'
    qry = "insert into User_reg(User_name,Password,active) values(?,?,?)"
    cur.execute(qry, (username, password, active))
    con.commit()
    print("\n User inserted successfully \n")
def details():
    cur.execute("select * from User_reg")
    record = cur.fetchall()
    for i in record:
        print(f"User ID  :{i[0]}")
        print(f"User Name  :{i[1]}")
        print(f"User password : {i[2]} \n")
def update(user_id):
        username = input("Enter the username:")
        password = input("Enter the password:")
        qry = ("UPDATE User_reg set User_name=?,Password=? where user_id=?")
        cur.execute(qry, (username, password, user_id))
        con.commit()
        qry2=("select * from User_reg where user_id=?")
        cur.execute(qry2,(user_id,))
        con.commit()
        record = cur.fetchall()
        for i in record:
            print("\n")
            print(f"User ID  :{i[0]}")
            print(f"User Name  :{i[1]}")
            print(f"User password : {i[2]} \n")
def delete(username):
    reco = ("Delete from User_reg where User_name=? and active='True'")
    cur.execute(reco, (username,))
    con.commit()
    print("User deleted successfully")

while True:
    print("-----Menu-------")
    print("1.User registration")
    print("2.User details")
    print("3.Update user")
    print("4. Delete user")
    print("5. Exit")
    print("....Select your options.....")
    print("...............................")
    option=int(input("please Enter your options:"))
    if option==1:
        username=input("Enter username :")
        password=input("Eneter password :")
        insert(username,password)

    if option ==2:
        details()

    if option==3:
        user_id=input("Enter the user id for update :")
        update(user_id)
    if option==4:
        username=input("Eneter user for delete:")
        delete(username)

    if option==5:
        break
con.close()
