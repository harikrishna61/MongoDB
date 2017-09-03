""""Team Members"""
# Harikrishna Bathala (1001415489)
# Rohit Katta (1001512896)

#This program takes data from csv file and loads it into MySQL Database

import pymysql.cursors

#connection parameters
conn = pymysql.connect(host='127.0.0.1',user='root', password='', db='proj2', charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor, local_infile=1)
cur = conn.cursor()

#Queries to create all tables
emp_create_q = "CREATE TABLE employee (fname varchar(255) NOT NULL,minit varchar(4),lname varchar(255) NOT NULL,Ssn char(9) NOT NULL,Bdate varchar(20),address varchar(255),sex char,salary decimal(10,2),Super_ssn char(9) NOT NULL,dno int NOT NULL,PRIMARY KEY (Ssn))"
dept_create_q = "CREATE TABLE department (dname varchar(255) NOT NULL,dnumber int NOT NULL,Mgr_Ssn char(9) NOT NULL,Mgr_start_date varchar(20),PRIMARY KEY (dnumber))"
dept_loc_create_q = "CREATE TABLE dept_locations (dnumber int NOT NULL,dlocation varchar(255) NOT NULL,PRIMARY KEY (dnumber,dlocation))"
proj_create_q = "CREATE TABLE project (pname varchar(255) NOT NULL,pnumber int NOT NULL,plocation varchar(15),dnum int NOT NULL,PRIMARY KEY (pnumber))"
works_create_q = "CREATE TABLE works_on (Essn char(9) NOT NULL,pno int NOT NULL,hours decimal(3,1) NOT NUll,PRIMARY KEY (Essn,pno))"

#Code to execute all Create Tables queries
cur.execute(emp_create_q)
cur.execute(dept_create_q)
cur.execute(dept_loc_create_q)
cur.execute(proj_create_q)
cur.execute(works_create_q)

#Queries to Insert data into tables by reading csv files given as input.
emp_insert_query = r"LOAD DATA local INFILE 'D:\\CourseWork\\Summer2017\\Db2\\Project2\\EMPLOYEE.csv' INTO TABLE employee FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\r\n'"
dept_insert_query = r"LOAD DATA local INFILE 'D:\\CourseWork\\Summer2017\\Db2\\Project2\\DEPARTMENT.csv' INTO TABLE department FIELDS TERMINATED BY ', ' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\r\n'"
dept_loc_insert_query = r"LOAD DATA local INFILE 'D:\\CourseWork\\Summer2017\\Db2\\Project2\\DEPT_LOCATIONS.csv' INTO TABLE dept_locations FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\r\n'"
proj_insert_query = r"LOAD DATA local INFILE 'D:\\CourseWork\\Summer2017\\Db2\\Project2\\PROJECT.csv' INTO TABLE project FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\r\n'"
works_insert_query = r"LOAD DATA local INFILE 'D:\\CourseWork\\Summer2017\\Db2\\Project2\\WORKS_ON.csv' INTO TABLE works_on FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '''' LINES TERMINATED BY '\r\n'"

#Code to execute all Insert queries
cur.execute(emp_insert_query)
cur.execute(dept_insert_query)
cur.execute(dept_loc_insert_query)
cur.execute(proj_insert_query)
cur.execute(works_insert_query)

#Commiting all operations performed.
conn.commit()
