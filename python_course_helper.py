import sqlite3 as lite


#functinality goes here
class DatabaseManage(object):


    def __init__(self):
        global dbconn
        try:
            dbconn = lite.connect('courses.db')
            with dbconn:
                cur = dbconn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")

        except Exception:
            print("Unable to connect database")

    def insert_data(self,data):
        try:
            with dbconn:
                cur = dbconn.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)",data)
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with dbconn:
                cur = dbconn.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self,id):
        try:
            with dbconn:
                cur = dbconn.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql ,[id])
                return True
        except Exception:
            return False




# TODO: provide interface to user

def main():
    print("*"*40)
    print("\n :: COURSE MANAGEMENT:: \n")
    print("*"*40)
    print("\n")

    db  = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print("\n1. Insert a new course \n")
    print("\n2. Show all courses \n")
    print("\n3. Delete a course (NEED ID) \n")
    print("#"*40)
    print("\n")

    choice = input("\nEnter your choice: \n")

    if choice == "1":
        name = input("\nEnter course name: \n")
        description = input("\nEnter course description: \n")
        price = input("\n Enter course price: \n")
        private = input("\nIs course private (0/1): \n")

        if db.insert_data([name,description,price,private]):
            print("Course inserted successfully")
        else:
            print("Something went wrong!!!")
    
    elif choice == "2":
        print("\n :: Course list ::\n")

        for index,item in enumerate(db.fetch_data()):
            print("\n Sr no. "+str(index + 1))
            print("\n Course ID "+str(item[0]))
            print("\n Course name "+str(item[1]))
            print("\n Course description "+str(item[2]))
            print("\n Course price "+str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("\n Is private "+ private)
            print("\n")
    elif choice == "3":
        record_id = input("\nEnter course ID : ")
        if db.delete_data(record_id):
            print("\n Course was deleted ")
        else:
            print("\n Something went wrong!!!")

    else:
        print("WRONG CHOICE")

if __name__ == '__main__' : 
    main()