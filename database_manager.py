from tkinter import *
from PIL import ImageTk,Image
import sqlite3

#out main root
mainroot = Tk()
mainroot.title('Students Database Manager')
screen_width = mainroot.winfo_screenwidth()
screen_height = mainroot.winfo_screenheight()
mainroot.geometry(str(screen_width) + "x" + str(screen_height))

root = LabelFrame(mainroot, text="Controling Bar", width=450, height=screen_height, padx=10 , pady=10 )
root.grid(row=0,column=0,rowspan=1,columnspan=1, sticky="NSEW")

root2 = LabelFrame(mainroot, text="Content of the Database", width=1050, height=screen_height, padx=10 , pady=10)
root2.grid(row=0,column=1,rowspan=1,columnspan=3, sticky="NSEW")


#____________________________________________________________________________________________________________#

# Create a database or connect to one
conn = sqlite3.connect('database.db')

# Create cursor
c = conn.cursor()

# Create table

c.execute("""CREATE TABLE database (
		first_name text,
		last_name text,
        neptun_code text,
		final_exam_grade text,
		midterm_grade text,
		homeworks_grad text
		)""")


#____________________________________________________________________________________________________________#

# Create Update function to update a record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('database.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	
	c.execute("""UPDATE database SET
		first_name = :f_name,
		last_name = :l_name,
		neptun_code = :n_code,
		final_exam_grade = :final_exam,
		midterm_grade = :midterm,
		homeworks_grad = :HWs 
		WHERE oid = :oid""",
		{
		'f_name': f_name_editor.get(),
		'l_name': l_name_editor.get(),
		'n_code': n_code_editor.get(),
		'final_exam': final_exam_editor.get(),
		'midterm': midterm_editor.get(),
		'HWs': HWs_editor.get(),
		'oid': record_id
		})


	#Commit Changes studnets
	conn.commit()

	# Close Connection 
	conn.close()

	editor.destroy()
	root.deiconify()

#____________________________________________________________________________________________________________#

# Create Edit function to update a record
def edit():
	#root.withdraw()
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("400x300")
	# Create a database or connect to one
	conn = sqlite3.connect('database.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM database WHERE oid = " + record_id)
	records = c.fetchall()
	
	#Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global n_code_editor
	global final_exam_editor
	global midterm_editor
	global HWs_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1)

	n_code_editor = Entry(editor, width=30)
	n_code_editor.grid(row=2, column=1)

	final_exam_editor = Entry(editor, width=30)
	final_exam_editor.grid(row=3, column=1)

	midterm_editor = Entry(editor, width=30)
	midterm_editor.grid(row=4, column=1)
	
	HWs_editor = Entry(editor, width=30)
	HWs_editor.grid(row=5, column=1)
	
	# Create Text Box Labels
	f_name_label = Label(editor, text="First Name")
	f_name_label.grid(row=0, column=0, pady=(10, 0))

	l_name_label = Label(editor, text="Last Name")
	l_name_label.grid(row=1, column=0)

	n_code_label = Label(editor, text="Neptun Code")
	n_code_label.grid(row=2, column=0)

	final_exam_label = Label(editor, text="Final Exam Grade")
	final_exam_label.grid(row=3, column=0)

	midterm_label = Label(editor, text="Midterm Exam Grade")
	midterm_label.grid(row=4, column=0)

	HWs_label = Label(editor, text="Homeworks Grade")
	HWs_label.grid(row=5, column=0)

	# Loop thru results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		n_code_editor.insert(0, record[2])
		final_exam_editor.insert(0, record[3])
		midterm_editor.insert(0, record[4])
		HWs_editor.insert(0, record[5])

	
	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Save Record", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	

#____________________________________________________________________________________________________________#


# Create Function to Delete A Record
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('database.db')
	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from database WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()


#____________________________________________________________________________________________________________#


# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('database.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO database VALUES (:f_name, :l_name, :n_code, :final_exam, :midterm, :HWs)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'n_code': n_code.get(),
				'final_exam': final_exam.get(),
				'midterm': midterm.get(),
				'HWs': HWs.get()
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	n_code.delete(0, END)
	final_exam.delete(0, END)
	midterm.delete(0, END)
	HWs.delete(0, END)

#____________________________________________________________________________________________________________#

# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('database.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM database")
	records = c.fetchall()
	# print(records)
	

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records = str(record[6])+ " \t" + str(record[0]) + "\t" +str(record[1])+ "\t"+str(record[2])+ "\t"+str(record[4])+ "\t" +str(record[5]) + "\n"
		query_label = Label(root2, text=print_records)
		query_label.pack(padx=5, pady=5, anchor=W)

	query_label = Label(root2, text="__________________________________________________________________________")
	query_label.pack(padx=5, pady=5, anchor=W)

	#Commit Changes
	conn.commit()

	# Close Connection 


#____________________________________________________________________________________________________________#

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

n_code = Entry(root, width=30)
n_code.grid(row=2, column=1)

final_exam = Entry(root, width=30)
final_exam.grid(row=3, column=1)

midterm = Entry(root, width=30)
midterm.grid(row=4, column=1)

HWs = Entry(root, width=30)
HWs.grid(row=5, column=1, pady=5)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


#____________________________________________________________________________________________________________#

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

n_code_label = Label(root, text="Neptun Code")
n_code_label.grid(row=2, column=0)

final_exam_label = Label(root, text="Final Exam Grade")
final_exam_label.grid(row=3, column=0)

midterm_label = Label(root, text="Midterm Exam Grade")
midterm_label.grid(row=4, column=0)

HWs_label = Label(root, text="Homeworks grade")
HWs_label.grid(row=5, column=0, pady=5)

delete_box_lable = Label(root, text="Delete or Edit Row Number:")
delete_box_lable.grid(row=9, column=0,)



#____________________________________________________________________________________________________________#

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=1, pady=10, padx=20, ipadx=50)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=1, columnspan=2, pady=10, padx=10, ipadx=50)

#____________________________________________________________________________________________________________#

#Commit Changes
conn.commit()

# Close Connection 
conn.close()

root.mainloop()