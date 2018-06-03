import sqlite3

DBNAME = r"e:\classroom\python\may15\webdemo\db.sqlite3"


def add_course(title, duration, fee):
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("insert into courses(title,duration,fee) values(?,?,?)",
                    (title, duration, fee))

        if cur.rowcount == 1:
            con.commit()
            return True
        else:
            return False
    except Exception as ex:
        print("Error :", ex)
        return False
    finally:
        con.close()


def get_courses():
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select * from courses")
        return cur.fetchall()    # List of Tuples (id,title,duration,fee)
    except Exception as ex:
        print("Error :", ex)
        return None
    finally:
        con.close()

