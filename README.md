Names:
Harikrishna Bathala (1001415489)
Rohit Katta (1001512896)

Language: PYTHON(To load csv into database and then to Mongodb)
	  C# (To create XML documents)

==============================================================================================================================================
Each File Explained:

CSvtoSQL.py
This program takes data from csv file and loads it into MySQL Database.

SQLtoMongo.py
This program takes data from MySQL database and inserts it into MongoDb
Selecting required data for Project collection from MySQL db using JOIN
Selecting required data for Department collection from MySQL db using JOIN
Queries:
1.) Printing project name and count of employees in the project
2.) Give an employee name and gives the total hours he/she worked 

Output-Project1-HariKrishna-Rohit.pdf
Contains few queries and their results exectued in mongodb for collections Project and Department.

XMLCreator.cs
Contains code to create department and project xml files.

department.xml
XML file containing all department data

project.xml
XML file containing all project data

Report.pdf
Contains detailed explanation using psuedo code.
============================================================================================================================================
CSV to MySQL to MongoDb:

Project Collection:
{‘pname’ –project name, ‘pnumber’ -project number, ‘dname’- department number and ‘employees’ 
which is again a JSON which has list of employees with {‘fname’-first name,’lname’- last name, ‘hours’= no of hours worked} }
Department Colletion:
{‘Dname’- department name, ‘lname’- manager’s last name and locations which is again a JSON 
which includes list of ‘locations’ {(‘dlocations’- department locations) } }


Design/PseudoCode:
1.)	Creating tables of employee, department, dept_locations, project, works_on in SQL and load the respective table data into them.
2.)	Writing a SQL query by joining project, department, employee and works_on and loading those tuples into the mongodb document ‘project’.
3.)	 Writing a SQL query by joining dept_locations, department and employee and loading those tuples into the mongodb document ‘department’.
4.)	Now, we can write mongodb queries on the both documents ‘project’ and ‘department’ to retrieve data based on our requirements.
================================================================================================================================================
XML Creation:
Code uses Newtonsoft JSON library and MongoDb drivers for .NET
It first connects to MongoDb. Fetches all the json objects and stores them in a list.
We iterate over each list item and convert it into xml string using newtonsoft json library and create XMLNode with this string.
All these nodes are inserted into a blank XML Document with root node as collection name.

================================================================================================================================================
How to Run the code:
CSvtoSQL.py
Requirements: pymsql Python module  

	Database 'pro2' needs to be created before runnning this file as we have to connect to some database to work with.
Change the file path for insert query which the ata in the path to db.

SQLtoMongo.py
Requirements: pymsql and pymong Python modules.  

	Simplying running the python file will do.
--------------------------------------------------------------------------------------------------------------------------------------------------
C# code procedure.
Requirements: NewtonsoftJson, MongoDbDrivers
execute XMLCreator.cs
==================================================================================================================================================
NOTE: Demo was given on Friday,but XML part was not shown in demo.
      Submitting complete XML portion now.
      Consider this submission for extra credit.
