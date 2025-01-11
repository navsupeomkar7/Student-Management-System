import sqlite3
db=sqlite3.connect('Student_Management.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS reg"
               "(Name TEXT,Address TEXT,Phone_no Text,Email TEXT,Password TEXT,Confirm_Password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS adreg"
               "(Name Text,Address Text,Phone_no Text,Email Text,Password Text,Confirm_Password Text)")
cursor.execute("CREATE TABLE IF NOT EXISTS contactus"
               "(Name TEXT,Email TEXT,Message TEXT)")
db.commit()
db.close()