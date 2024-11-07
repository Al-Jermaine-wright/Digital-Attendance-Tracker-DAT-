# Database Connectivity using Python
import mysql.connector

# Task 4: Error Handling
try:
    conn = mysql.connector.connect(user='root',
                                   password='',
                                   database='student_dat',
                                   host='localhost', )
    cnx = conn

except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)


# insert into table
def insert_into_table(id_, pres_date, time_in):
    cursor = cnx.cursor()
    a1 = "insert into student_dat.register_info(id, pres_date, time_in) values('{}', '{}', '{}')".format(
        id_, pres_date, time_in)

    # Error Handling
    try:
        query = a1
        cursor.execute(query)
        cnx.commit()
        # print("Present")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


# view table
def select_name(code):
    cursor = cnx.cursor()
    query = "select name from students_data where code_ = {}".format(code)
    cursor.execute(query)
    rows = []
    for i in cursor:
        i = i[0]
        rows.append(i)
    # print(rows)
    return rows


def select_code():
    cursor = cnx.cursor()
    query = "select code_ from students_data"
    cursor.execute(query)
    rows = []
    for i in cursor:
        i = i[0]
        rows.append(i)
    # print(rows)
    return rows


def select_number(code):
    cursor = cnx.cursor()
    query = "select number from students_data where code_ = {}".format(code)
    cursor.execute(query)
    rows = []
    for i in cursor:
        i = i[0]
        rows.append(i)
    # print(rows)
    x = rows[0]
    # x = '"{}"'.format(x)
    return x


def select_id(code):
    cursor = cnx.cursor()
    query = "select id from students_data where ran_code = {}".format(code)
    cursor.execute(query)
    rows = []
    for i in cursor:
        i = i[0]
        rows.append(i)
    # print(rows)
    return rows[0]


# update_record
def update_student_rand_num(random_code, code):
    cursor = cnx.cursor()
    a = (
        "UPDATE students_data SET ran_code = '{}' WHERE code_ = {}".format(random_code, code))
    # Task 4: Error Handling
    try:
        query = a
        cursor.execute(query)
        cnx.commit()
        # print("Record Update Successfully")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def update_student_time_out(time_out, id, date):
    cursor = cnx.cursor()
    a = (
        "UPDATE register_info SET time_out = '{}' WHERE id = {} and pres_date = '{}'".format(time_out, id, date))
    # Task 4: Error Handling
    try:
        query = a
        cursor.execute(query)
        cnx.commit()
        # print("Record Update Successfully")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def fetch_all():
    cursor = cnx.cursor()
    query = "SELECT ri.reg_id, sd.name,ri.pres_date,ri.time_in,ri.time_out FROM register_info ri left join students_data sd on sd.id = ri.id"
    cursor.execute(query)
    rows = []
    for i in cursor:
        rows.append(i)
    # print(rows)
    return rows


def reg_student_data(id, date, time_in, time_out):
    cursor = cnx.cursor()
    a = (
        "UPDATE register_info SET pres_date ={} and time_in ={} and	time_out ={} WHERE id = {}".format(id, date,
                                                                                                          time_in,
                                                                                                          time_out))
    # Task 4: Error Handling
    try:
        query = a
        cursor.execute(query)
        cnx.commit()
        # print("Record Update Successfully")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
