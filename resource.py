import random
from datetime import datetime
import cxn
import vonage

dt_time = datetime.now()
pres_date = "%s/%s/%s" % (dt_time.year, dt_time.month, dt_time.day)
timein_out = dt_time.strftime("%H:%M:%S")


def second():
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        cxn.update_student_rand_num(random_code, code)
        print(f"Hello there {user} please insert your randomly generated code")
        user_input = int(input("..: "))
        if user_input == random_code:
            id = cxn.select_id(random_code)
            cxn.insert_into_table(id, pres_date, timein_out)
            print("{} Hope you have a great day".format(user))
        else:
            print("{} is not your randomly generated code".format(user_input))
    else:
        print("{} is an invalid code".format(code))
    # num = cxn.select_number(code)
    # print(num)
    # # send code to user #
    # print(f"Hello there {user} please insert your randomly generated code")
    # user_input = int(input("..: "))
    # if user_input == random_code:
    #     id = cxn.select_id(random_code)
    #     cxn.insert_into_table(id, pres_date, timein_out)
    #     print("{} Hope you have a great day".format(user))
    # else:
    #     print("Please Try Again")


def third():
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        cxn.update_student_rand_num(random_code, code)
        print(f"Hello there {user} please insert your randomly generated code")
        user_input = int(input("..: "))
        if random_code == user_input:
            id = cxn.select_id(random_code)
            cxn.update_student_time_out(timein_out, id, pres_date)
            print("{} Hope you had a great day".format(user))
        else:
            print("{} is not your randomly generated code".format(user_input))
    else:
        print("{} is an invalid code".format(code))

    # user = cxn.select_name(code)
    # random_code = random.randint(1000, 9999)
    # cxn.update_student_rand_num(random_code, code)
    # print(f"Hello there {user} please insert your randomly generated code")
    # user_input = int(input("..: "))
    # if random_code == user_input:
    #     id = cxn.select_id(random_code)
    #     cxn.update_student_time_out(timein_out, id, pres_date)
    #     print("{} Hope you had a great day".format(user))
    #
    # else:
    #     print("Please Try Again")


def first():
    print("Enter Your Code")
    x = int(input("..: "))
    global code
    code = x
    database_codes = cxn.select_code()
    if x in database_codes[:]:
        print("1.LOG IN \n 2.LOG OUT")
        opt = int(input("..: "))
        if opt == 1:
            second()
        elif opt == 2:
            third()
        else:
            print("Try Again")
    else:
        print("Please try again")


first()
















import random
from datetime import datetime
import cxn

dt_time = datetime.now()
pres_date = "%s/%s/%s" % (dt_time.year, dt_time.month, dt_time.day)
timein_out = dt_time.strftime("%H:%M:%S")


def second():
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        cxn.update_student_rand_num(random_code, code)
        print(f"Hello there {user} please insert your randomly generated code")
        user_input = int(input("..: "))
        if user_input == random_code:
            id = cxn.select_id(random_code)
            cxn.insert_into_table(id, pres_date, timein_out)
            print("{} Hope you have a great day".format(user))
        else:
            print("{} is not your randomly generated code".format(user_input))
    else:
        print("{} is an invalid code".format(code))


def third():
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        cxn.update_student_rand_num(random_code, code)
        print(f"Hello there {user} please insert your randomly generated code")
        user_input = int(input("..: "))
        if random_code == user_input:
            id = cxn.select_id(random_code)
            cxn.update_student_time_out(timein_out, id, pres_date)
            print("{} Hope you had a great day".format(user))
        else:
            print("{} is not your randomly generated code".format(user_input))
    else:
        print("{} is an invalid code".format(code))


def first():
    print("Enter Your Code")
    x = int(input("..: "))
    global code
    code = x
    database_codes = cxn.select_code()
    if x in database_codes[:]:
        print("1.LOG IN \n 2.LOG OUT")
        opt = int(input("..: "))
        if opt == 1:
            second()
        elif opt == 2:
            third()
        else:
            print("Try Again")
    else:
        print("Please try again")

if __name__ == '__main__':
    first()
