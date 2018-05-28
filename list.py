# -*- coding: utf-8 -*- 
import sqlite3
import category as ctg

conn = sqlite3.connect("task.db")
cur = conn.cursor()
# table col : id, what, due, importance, category, finished

def list_todo_due():
	slct_data = "select * from todo where finished = ? order by due asc, what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		if(row[5]=='n'):
			print('☐', row[3], row[1], row[2], row[4])
		else:
			print('☑', row[3], row[1], row[2], row[4])

	print("")

def list_todo_importance():
	slct_data = "select * from todo where finished = ? order by importance asc, what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

	print("")

def list_todo_what():
	slct_data = "select * from todo where finished = ? order by what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

	print("")

def list_todo_category(category):	# 가나다순
	slct_data = "select * from todo where category = ? and finished = ? order by category asc"
	cur.execute(slct_data, [category,'n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2])

	print("")

def list_main():
	opt = input("(1: due, 2: what, 3: importance, 4: category)? ")
	while not opt.isdigit():
		opt = input("(1: due, 2: what, 3: importance, 4: category)? ")
	opt = int(opt)
	while opt < 1 or opt > 4:
		opt = int(input("(1: due, 2: what, 3: importance, 4: category)? "))
	if opt == 1:
		list_todo_due()
	elif opt == 2:
		list_todo_what()
	elif opt == 3:
		list_todo_importance()
	elif opt == 4:
		ctg.show_category()
		c = str(input("What cateogry do you want to list? "))
		list_todo_category(c)
