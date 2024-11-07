import random
import smtplib
from datetime import datetime
import cxn
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

dt_time = datetime.now()
pres_date = "%s/%s/%s" % (dt_time.year, dt_time.month, dt_time.day)
timein_out = dt_time.strftime("%H:%M:%S")


def attendace_login():
    # generate random code
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        # emial random code
        server= smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("","")
        server.sendmail("@gmail.com","@gmail.com",random_code)
        server.quit()
        cxn.update_student_rand_num(random_code, code)

        def log_in():
            x = ran_code.get()
            user_input = int(x)
            if random_code == user_input:
                id = cxn.select_id(random_code)
                cxn.insert_into_table(id, pres_date, timein_out)
                messagebox.showinfo(title='Log-in Successfully', message="{} Hope you have a great day".format(user))
            else:
                messagebox.showinfo(title='Invalid Code',
                                    message="{} is not your randomly generated code".format(user_input))

        ran_code_label = Label(tab1, text='Enter Your Code:')
        ran_code_label.pack()
        ran_code = Entry(tab1)
        ran_code.pack()

        add_button = Button(tab1, text='Submit', command=log_in)
        add_button.pack()

    else:
        messagebox.showinfo(title='Invalid Code',
                            message="{} is an invalid code or if you are seeing this there must be a bug somewhere F***".format(
                                code))
        print("{} is an invalid code".format(code))


def attendace_logout():
    # generate random code
    database_codes = cxn.select_code()
    if code in database_codes[:]:
        user = cxn.select_name(code)
        random_code = random.randint(1000, 9999)
        # email random code
        cxn.update_student_rand_num(random_code, code)

        def log_out():
            x = ran_code.get()
            user_input = int(x)
            if random_code == user_input:
                id = cxn.select_id(random_code)
                cxn.update_student_time_out(timein_out, id, pres_date)
                messagebox.showinfo(title='Log-Out Successfully', message="{} Hope you had a great day".format(user))

            else:
                messagebox.showinfo(title='Invalid Randomly Generated Code',
                                    message="{} is not your randomly generated code".format(user_input))

        ran_code_label = Label(tab1, text='Enter Your Code:')
        ran_code_label.pack()
        ran_code = Entry(tab1)
        ran_code.pack()

        add_button = Button(tab1, text='Submit', command=log_out)
        add_button.pack()

    else:
        messagebox.showinfo(title='Invalid Code',
                            message="{} is an invalid code and if you are seeing this there must be a bug somewhere F***".format(
                                code))
        print("{} is an invalid code".format(code))


# Function To check User code and select log option
def stu_login():
    # function Get what user typed in and compare
    def get_():
        x = x_entry.get()
        global code  # make code usable in other function
        code = int(x)
        database_codes = cxn.select_code()
        if code in database_codes[:]:
            # function to get value for radio button
            def opt_():
                if (x.get() == 0):
                    attendace_login()
                elif (x.get() == 1):
                    attendace_logout()
                else:
                    messagebox.showinfo(title='title', message='Wow')
                    messagebox.askokcancel(title='ohk cancel', message='do you')
                    print("Try Again")

            # Radio Button
            val = ["LOG IN", "LOG OUT"]
            x = IntVar()
            for i in range(len(val)):
                radio_button = Radiobutton(window,
                                           text=val[i],
                                           variable=x,
                                           value=i,
                                           indicatoron=0,
                                           width=100,
                                           command=opt_)
                radio_button.pack()
        else:
            messagebox.showinfo(title='Invalid Code', message='{} is not a valid entry code'.format(code))

    # Entry Box for code
    x_label = Label(tab1, text='Enter Your Code:')
    x_label.pack()
    x_entry = Entry(tab1)
    x_entry.pack()

    add_button = Button(tab1, text='Submit', command=get_)
    add_button.pack()


def admin_login():
    def fetch_data():
        stu_data = pd.DataFrame(cxn.fetch_all())
        stu_data.columns = ["Student_Name", "Date", "Time_In", "Time_Out"]
        stu_data["Date"] = pd.to_datetime(stu_data["Date"])
        stu_data["Time_In"] = stu_data["Time_In"].astype(str).map(lambda x: x[7:])
        stu_data["Time_Out"] = stu_data["Time_Out"].astype(str).map(lambda x: x[7:])
        x = stu_data["Time_Out"]
        y = stu_data["Time_In"]
        ti_ou = []
        ti_in = []
        for i in y:
            ti_ou.append(i)
        for i in x:
            ti_ou.append(i)
        if "" in ti_ou:
            stu_data["Time_Out"].replace("", "A", inplace=True)
        if "" in ti_in:
            stu_data["Time_In"].replace("", "A", inplace=True)
        # stu_data.set_index("Student_Name", inplace=True)

        ws = Tk()

        ws.title('000')
        ws.geometry('500x500')

        set = ttk.Treeview(ws)
        set.pack()

        set['columns'] = ('ID','Name', 'Date', 'Time IN', "Time Out")
        set.column("#0", width=0, stretch=NO)
        set.column("ID", anchor=CENTER, width=20)
        set.column("Name", anchor=CENTER, width=120)
        set.column("Date", anchor=CENTER, width=91)
        set.column("Time IN", anchor=CENTER, width=80)
        set.column("Time Out", anchor=CENTER, width=80)

        set.heading("#0", text="", anchor=CENTER)
        set.heading("ID", text="ID", anchor=CENTER)
        set.heading("Name", text="Name", anchor=CENTER)
        set.heading("Date", text="Date", anchor=CENTER)
        set.heading("Time IN", text="Time IN", anchor=CENTER)
        set.heading("Time Out", text="Time Out", anchor=CENTER)

        global count
        count = 0

        stu_data_list = stu_data.values.tolist()

        for record in stu_data_list:
            set.insert(parent='', index='end', iid=count, text='',
                       values=(record[0], record[1], record[2], record[3], record[4]))

            count += 1

        Input_frame = Frame(ws)
        Input_frame.pack()
        id = Label(Input_frame, text="ID")
        id.grid(row=0, column=0)

        date = Label(Input_frame, text="Date")
        date.grid(row=0, column=1)

        time_in = Label(Input_frame, text="time_in")
        time_in.grid(row=0, column=2)

        time_out = Label(Input_frame, text="time_out")
        time_out.grid(row=0, column=3)

        id_entry = Entry(Input_frame)
        id_entry.grid(row=1, column=0)

        date_entry = Entry(Input_frame)
        date_entry.grid(row=1, column=1)

        time_inentry = Entry(Input_frame)
        time_inentry.grid(row=1, column=2)

        time_outentry = Entry(Input_frame)
        time_outentry.grid(row=1, column=3)

        def input_record():
            global count

            id_entry.get(), date_entry.get(), time_inentry.get(), time_outentry.get()

            set.insert(parent='', index='end', iid=count, text='',
                       values=(id_entry.get(), date_entry.get(), time_inentry.get(), time_outentry.get()))
            cxn.reg_student_data(id_entry.get(), date_entry.get(), time_inentry.get(), time_outentry.get())
            count += 1

        # button
        Input_button = Button(ws, text="Input Record", command=input_record)

        Input_button.pack()
        ws.mainloop()

    def check_pswd():
        admin_pswd = pswd.get()
        if admin_pswd == "123435":
            fetch_data()
        else:
            print(9)
        # disable after user inputs. entry.config(state=DISABLED)

    pswd = Label(tab2, text='Enter Password:')
    pswd.pack()
    pswd = Entry(tab2, show="+")
    pswd.pack()

    submit_button = Button(tab2, text='Submit', command=check_pswd)
    submit_button.pack()


window = Tk()

window.title('DAT')
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='Students Portal')
notebook.add(tab2, text='Administrative Portal')

notebook.pack(expand=True, fill="both")

Label(tab1, stu_login(), width=50, height=25).pack()
Label(tab2, admin_login(), width=50, height=25).pack()

window.mainloop()

#
# from tkinter import *
# from tkinter import ttk
#
# ws = Tk()
#
# ws.title('PythonGuides')
# ws.geometry('500x500')
#
# set = ttk.Treeview(ws)
# set.pack()
#
# set['columns'] = ('id', 'full_Name', 'award')
# set.column("#0", width=0, stretch=NO)
# set.column("id", anchor=CENTER, width=80)
# set.column("full_Name", anchor=CENTER, width=80)
# set.column("award", anchor=CENTER, width=80)
#
# set.heading("#0", text="", anchor=CENTER)
# set.heading("id", text="ID", anchor=CENTER)
# set.heading("full_Name", text="Full_Name", anchor=CENTER)
# set.heading("award", text="Award", anchor=CENTER)
#
# # data
# data = [
#     [1, "Jack", "gold"],
#     [2, "Tom", "Bronze"]
#
# ]
#
# global count
# count = 0
#
# for record in data:
#     set.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
#
#     count += 1
#
# Input_frame = Frame(ws)
# Input_frame.pack()
#
# id = Label(Input_frame, text="ID")
# id.grid(row=0, column=0)
#
# full_Name = Label(Input_frame, text="Full_Name")
# full_Name.grid(row=0, column=1)
#
# award = Label(Input_frame, text="Award")
# award.grid(row=0, column=2)
#
# id_entry = Entry(Input_frame)
# id_entry.grid(row=1, column=0)
#
# fullname_entry = Entry(Input_frame)
# fullname_entry.grid(row=1, column=1)
#
# award_entry = Entry(Input_frame)
# award_entry.grid(row=1, column=2)
#
#
# def input_record():
#     global count
#
#     set.insert(parent='', index='end', iid=count, text='',
#                values=(id_entry.get(), fullname_entry.get(), award_entry.get()))
#     count += 1
#
#     id_entry.delete(0, END)
#     fullname_entry.delete(0, END)
#     award_entry.delete(0, END)
#
#
# # button
# Input_button = Button(ws, text="Input Record", command=input_record)
#
# Input_button.pack()
#
# ws.mainloop()
