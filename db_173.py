#!/usr/bin/env python3
'''
	Developer: Fergus W. Clare
	Contact: fergusclare@gmail.com
	Course: CSC387 - Foundations of Computer Science
	University: University of Illinois Springfield 
	Last Updated: November 13th, 2017
	License: MIT
	Required Libraries: peewee (pip3 install peewee) http://peewee.readthedocs.io/en/latest/peewee/querying.html
	Made for compatibility with Python 3.6.3 (latest release)
'''
from peewee import *

db = SqliteDatabase('db387_173.db')

class Employee(Model):
	'''represents single object in db'''
	#define all of the values for the employee table
	empid = CharField(max_length = 225)
	empname = CharField(max_length = 225)
	address = CharField(max_length = 225)
	ssn = CharField(max_length = 225)

	class Meta:
		database = db

class Job(Model):
	#define all of the values for the job table
	jobid = CharField(max_length = 225)
	jobtitle = CharField(max_length = 225)
	skillcode = CharField(max_length = 225)
	dept = CharField(max_length = 225)

	class Meta:
		database = db

class Assignment(Model):
	#define all of the values for the assignment table
	empid = CharField(max_length = 225)
	jobid = CharField(max_length = 225)
	startdate = CharField(max_length = 225)
	termdate = CharField(max_length = 225)

	class Meta:
		database = db

#create data dict list for subsequent looping to enter data in tables
employee = [
	{'empid': '25x15', 'empname': 'Joe Baker', 'address':'33 Nowhere', 'ssn': '11122333'},
	{'empid': '34y70', 'empname': 'Cheryl Clark', 'address':'563 Downtown', 'ssn': '999009999'},
	{'empid': '23y34', 'empname': 'Jerry Smith', 'address':'1555 Circle', 'ssn': '111005555'}
]

job = [
	{'jobid': 's25x', 'jobtitle': 'secretary', 'skillcode':'t5', 'dept': 'personnel'},
	{'jobid': 's26x', 'jobtitle': 'secretary', 'skillcode':'t6', 'dept': 'accounting'},
	{'jobid': 'f5', 'jobtitle': 'floor manager', 'skillcode':'fm3', 'dept': 'sales'}
]

assignment = [
	{'empid': '23y34', 'jobid': 's25x', 'startdate':'03012009', 'termdate': '04302015'},
	{'empid': '34x70', 'jobid': 'f5', 'startdate':'10012010', 'termdate': '99999999'},
	{'empid': '23x34', 'jobid': 's26z', 'startdate':'05012010', 'termdate': '99999999'}
]

#functions to add data from dicts into tables
def add_employees(employee):
	for employee in employee:
		Employee.create(
			empid = employee['empid'],
			empname = employee['empname'],
			address = employee['address'],
			ssn = employee['ssn']
		)

def add_job(job):
	for job in job:
		Job.create(
			jobid = job['jobid'],
			jobtitle = job['jobtitle'],
			skillcode = job['skillcode'],
			dept = job['dept']
		)

def add_assignment(assignment):
	for assignment in assignment:
		Assignment.create(
			empid = assignment['empid'],
			jobid = assignment['jobid'],
			startdate = assignment['startdate'],
			termdate = assignment['termdate']
		)

#turn on the lights
if __name__ == '__main__':
	db.connect()
	db.create_tables([Employee], safe=True)
	db.create_tables([Assignment], safe=True)
	db.create_tables([Job], safe=True)
	add_employees(employee)
	add_job(job)
	add_assignment(assignment)