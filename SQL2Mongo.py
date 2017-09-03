""" Team Members"""
# Harikrishna Bathala (1001415489)
# Rohit Katta (1001512896)

#This program takes data from MySQL database and inserts it into MongoDb

import pymysql.cursors
from pymongo import MongoClient

#Connection Parameters for MySQL
conn = pymysql.connect(host='127.0.0.1',user='root', password='', db='proj2', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor, local_infile=1)
cur = conn.cursor()
#Connection Parameters for MongoDb
client = MongoClient('localhost', 27017)

""" inserting project table into mongodb document named 'peoject' in collection 'project2'"""
db = client.project2.project

#Selecting required data for Project collection from MySQL db using JOIN
cur.execute(r"SELECT p.pnumber, p.pname, d.dname, e.lname, e.fname, w.hours FROM project p JOIN department d ON p.dnum = d.dnumber JOIN works_on w ON p.pnumber = w.pno JOIN employee e ON w.Essn = e.Ssn ORDER BY p.pnumber ")
project_table = cur.fetchall()

#Code below iterates through all rows of output, parses them to create PROJECT json object.
#Foreach Project, all rows of Employees are put in a list.
#Employee list along with other Project details are converted to JSON and inserted into MongoDb
employee_json = []
for row in project_table:
    pro_name=row['pname'] #Assigning first Project as current Project
    try:
        if same_pro_name==pro_name: #For each row we check whether we are working on same project
            pname=row['pname']
            pnumber = row['pnumber']
            dname=row['dname']
            employee_json.append({'lname': row['lname'], 'fname': row['fname'], 'hours': row['hours']})
        else: #If Project changes
            same_pro_name=pro_name
            project_json={}
            project_json['pname']=pname
            project_json['pnumber'] = pnumber
            project_json['dname']=dname
            project_json['employees']=employee_json
            db.insert(project_json)
            employee_json=[]
            print project_json
            print '\n'
            pname = row['pname']
            pnumber = row['pnumber']
            dname = row['dname']
            employee_json.append({'lname': row['lname'], 'fname': row['fname'], 'hours': row['hours']})
    except:
        same_pro_name = pro_name
        pname = row['pname']
        pnumber = row['pnumber']
        dname = row['dname']
        employee_json.append({'lname': row['lname'], 'fname': row['fname'], 'hours': row['hours']})

#Inserting last remaining row
project_json = {}
project_json['pname'] = pname
project_json['dname'] = dname
project_json['pnumber'] = pnumber
project_json['employees'] = employee_json
db.insert(project_json)
employee_json = []
print project_json

""" inserting DEpartment Table into mongodb document named 'department' in collection 'project2' """
#Selecting required data for Department collection from MySQL db using JOIN
cur.execute("SELECT d.dname, e.lname, dl.dlocation FROM department d JOIN dept_locations dl ON d.dnumber = dl.dnumber JOIN employee e ON d.Mgr_Ssn = e.Ssn ORDER BY d.dname;")
department_Table = cur.fetchall()
db1 = client.project2.department

#Code below iterates through all rows of output, parses them to create DEPARTMENT json object.
#Foreach Department, all rows of Locations are put in a list.
#Locations list along with other Department details are converted to JSON and inserted into MongoDb
location_json=[]
for row in department_Table:
    dname=row['dname'] #Assigning first Department
    try:
        if same_dname==dname: #For each row we check whether we are working on same department
            location_json.append({'dlocation': row['dlocation']})
            lname=row['lname']
            dname1=row['dname']
        else: #Department changes
            dept_json={}
            dept_json['lname']=lname
            dept_json['dname']=dname1
            dept_json['locations']=location_json
            db1.insert(dept_json)
            location_json=[]
            print dept_json
            print '\n'
            same_dname = dname
            location_json.append({'dlocation': row['dlocation']})
            lname = row['lname']
            dname1 = row['dname']
    except:
        same_dname = dname
        location_json.append({'dlocation': row['dlocation']})
        lname = row['lname']
        dname1 = row['dname']

dept_json={}
dept_json['lname']=lname
dept_json['dname']=dname
dept_json['locations']=location_json
db1.insert(dept_json)
location_json=[]
print dept_json


"""Printing project name and count of employees in the project """
print "No of employee in each db"
emp=db.find()
for row in emp:
    employees=row['employees']
    employee_count=0
    for e in employees:
        employee_count=employee_count+1
    pro_name=row['pname']
    print pro_name +": "+str(employee_count)

""" Give an employee name and gives the total hours he/she worked """
print "Give an employee name and gives the total hours he/she worked"
emp_fname=str(raw_input("Enter first name: "))
emp_lname=str(raw_input("Enter last name: "))
emp_hours=0
emp=db.find()

for rec in emp:
    employees_det=rec['employees']
    for e1 in employees_det:
        get_fname=e1['fname']
        get_lname=e1['lname']

        if get_fname==emp_fname and get_lname==emp_lname:
            emp_hours=emp_hours+e1['hours']
            break

print emp_hours

