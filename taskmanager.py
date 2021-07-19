from tkinter import *
from tkinter import messagebox 

tasks_list = [] 

counter = 1

def inputError() : 
	
	if enterTaskField.get() == "" : 
		
		messagebox.showerror("Input Error") 
		
		return 0
	
	return 1

def clear_taskNumberField() : 
	
	taskNumberField.delete(0.0, END) 

def clear_taskField() : 

	enterTaskField.delete(0, END) 
	

def insertTask(): 

	global counter 
	
	value = inputError() 

	if value == 0 : 
		return


	content = enterTaskField.get() + "\n"

	tasks_list.append(content) 

	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content) 

	counter += 1

	clear_taskField() 

def delete() : 
	
	global counter 
	
	if len(tasks_list) == 0 : 
		messagebox.showerror("No task") 
		return

	number = taskNumberField.get(1.0, END) 

	if number == "\n" : 
		messagebox.showerror("input error") 
		return
	
	else : 
		task_no = int(number) 

	clear_taskNumberField() 
	

	tasks_list.pop(task_no - 1) 

	counter -= 1
	
	TextArea.delete(1.0, END) 

	for i in range(len(tasks_list)) : 
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i]) 
	

# Driver code 
if __name__ == "__main__" : 

	gui = Tk() 

	gui.configure(background = "#94d3f7")

	gui.title("Ripunjay's To-Do App") 

	gui.geometry("1024x768") 

	enterTask = Label(gui, text = "Enter Your Task", background="#94d3f7")


	enterTaskField = Entry(gui, background="#e8e9ed")


	Submit = Button(gui, text = "Submit", fg = "Black", bg = "#fafcfc", command = insertTask)

	
	TextArea = Text(gui, height = 10, width = 110, font = "lucida 13", background="#e8e9ed")

	taskNumber = Label(gui, text="Delete Task Number", bg = "#94d3f7")
						
	taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13", background="#e8e9ed")
 
	delete = Button(gui, text = "Delete", fg = "Black", bg = "#fafcfc", command = delete)

 
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "#f25f49", command = exit)


	enterTask.grid(row = 0, column = 2) 

	enterTaskField.grid(row = 1, column = 2, ipadx = 50) 
						
	Submit.grid(row = 3, column = 2)
	
	TextArea.grid(row = 5, column = 2, padx = 10, sticky = W)
						
	taskNumber.grid(row = 6, column = 2, pady = 5)
						
	taskNumberField.grid(row = 7, column = 2)

			 
	delete.grid(row = 8, column = 2, pady = 5)
						
	Exit.grid(row = 9, column = 2)

	gui.mainloop()
