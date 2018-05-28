# -*- coding: utf-8 -*- 
import sqlite3
import logo as lg
import add_todo as at
import list as li
import create_table as ct
import modify as md
import del_todo as dl
import category as ctg
import auto_finish as af

import inquirer


def run_program():
	while True:
		print("Choose what to do")
		# mode = str(input("(a: Add todo, l: list todo, m: Modify todo, d: Delete todo, c: Show category q:Quit)? "))
		af.auto_fin()
		mode = [
				inquirer.List('mode',
				message="Choose what to do",
				choices=['Add todo', 'List todo', 'Modify todo', 'Delete todo', 'Show category', 'Quit'],
			),
		]
		answers = inquirer.prompt(mode)

		if answers == 'Add todo' or answers == 'Add todo':
			at.add_todo()
		elif mode == 'l' or mode == 'L':
			li.list_main()
		elif mode == 'm' or mode == 'M':
			md.modify_todo()
		elif mode == 'd' or mode == 'D':
			dl.del_todo()
		elif mode == 'c' or mode == 'C':
			ctg.show_category()
		elif mode == 'q' or mode == 'Q':
			break
		af.auto_fin()

if __name__ == "__main__":
	lg.print_logo()
	ct.create_table()
	run_program()
