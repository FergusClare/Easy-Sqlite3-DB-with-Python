# Easy Sqlite3 DB via Python3
A quick and easy Sqlite3 database with Python and Peewee.  Running this script will allow you to build your very own Sqlite3 database in no time so that you can begin working with queries as quickly as possible.  Great for beginners eager to experiment with Sqlite.

## Install Instructions (mac):
- Make sure you're running python3.6.3
- From root, pip3 install peewee
- Navigate to the directory where you have the script installed and run
- python3 db_173.py
- Open sqlite3 via terminal with sqlite3 db_173.db
- From here, you can begin to query the tables

## Table Schema:
There are three tables in the db_173 sample:
- employee [empid, empname, address, ssn]
- job [jobid, jobtitle, skillcode, dept]
- assignement [empid, jobid, startdate, termdate]

