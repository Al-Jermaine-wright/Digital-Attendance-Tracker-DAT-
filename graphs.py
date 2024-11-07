import pandas as pd
import cxn
import matplotlib.pyplot as plt

stu_data = pd.DataFrame(cxn.fetch_all())
stu_data.columns = ["ID","Student_Name", "Date", "Time_In", "Time_Out"]
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

print(stu_data)