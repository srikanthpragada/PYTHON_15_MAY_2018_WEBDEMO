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


def get_course_titles():
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select id,title from courses")
        courses = []
        for c in cur.fetchall():
             courses.append((c[0], c[1]))

        return courses   # List of Tuples
    except Exception as ex:
        print("Error :", ex)
        return None
    finally:
        con.close()


def get_courses_by_title(title):
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        param = "%" + title + "%"
        cur.execute("select *  from courses where title like ?", (param,))
        # courses = []
        return cur.fetchall()
    except Exception as ex:
        print("Error :", ex)
        return None
    finally:
        con.close()

def get_topics(id):
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select * from topics where courseid = ?", (id))
        return cur.fetchall()    # List of Tuples (id,title,duration,fee)
    except Exception as ex:
        print("Error :", ex)
        return None
    finally:
        con.close()


def get_course_count():
    try:
        con = sqlite3.connect(DBNAME)
        cur = con.cursor()
        cur.execute("select count(id) from courses")
        return cur.fetchone()[0]
    except Exception as ex:
        print("Error :", ex)
        return None
    finally:
        con.close()