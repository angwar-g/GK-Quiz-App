from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox  # to display messages to the user

def on_click(): # to enter username into database
    global username
    username = uname.get() # storing info typed in blank box which is uname
    if username == "":     # if user does not enter any value
        MessageBox.showinfo("Insert Status", "Username required")
    else:
        con = mysql.connect(host="localhost", user="root", passwd="pw", database="quiz")

        if con.is_connected() == False:   # if there is a failure in establishing connection
            MessageBox.showinfo("Insert Status", "Error")

        cursor = con.cursor()  # cursor is a module in sql.connector package
        cursor.execute("insert into scores (Username) values('" + username + "')")  # scores is the table and Username is the column
        cursor.execute("commit")

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()
        mainscreen.destroy()   # first screen gets destroyed
    global count
    count = 0
    count += 1


def store_score(scores, username):    # store score in table
    con = mysql.connect(host="localhost", user="root", passwd="pw", database="quiz")

    if con.is_connected() == False:
        MessageBox.showinfo("Insert Status", "Error")

    cursor = con.cursor()
    query = """ update scores set score = %s where Username = %s"""  # %s implies that user will enter the value
    input_data = (scores, username)  # tuple
    cursor.execute(query, input_data)
    cursor.execute("commit")
    con.close()


def on_exit():   # exit the quiz in the beginning
    mainscreen.destroy()
    mainscreen1.destroy()

def main_screen():  # first screen
    global uname
    global mainscreen
    mainscreen = Tk()  # create a GUI window
    mainscreen.geometry("4800x880")  # set the configuration of GUI window
    mainscreen.title(" Login Page")  # set the title of GUI window

    # create a Form label
    login_canvas = Canvas(mainscreen, width=4800, height=880, bg="blue")
    login_canvas.pack()    # position of any widget
    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    heading = Label(login_frame, text="GK QUIZ", fg="black", bg="white")
    heading.config(font='calibri 40')
    heading.place(relx=0.45, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username", fg='black', bg='white', font='calibri 15')
    ulabel.place(relx=0.30, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3', fg='black', font='calibri 15')
    uname.config(width=42)
    uname.place(relx=0.45, rely=0.4)

    # LOGIN BUTTON
    log = Button(login_frame, text='START', padx=5, pady=5, width=5, command=on_click)  # command has the function to be executed when button is clicked
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)  # activebackground sets bg colour of button, releif is the 3D configuration of button
    log.place(relx=0.45, rely=0.6)

    # EXIT BUTTON
    exit = Button(login_frame, text='EXIT QUIZ', padx=5, pady=5, width=5, command=on_exit)
    exit.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    exit.place(relx=0.60, rely=0.6)

    mainscreen.mainloop()  # start the GUI
main_screen()  # call the main_account_screen() function


def display_score(): # display score at the end (last screen)
    b = 1
    global mainscreen2
    mainscreen2 = Tk()  # create a GUI window
    mainscreen2.geometry("4800x880")  # set the configuration of GUI window
    mainscreen2.title("YOUR SCORE")  # set the title of GUI window

    # create a Form label
    score_canvas = Canvas(mainscreen2, width=4800, height=880, bg="blue")
    score_canvas.pack()
    score_frame = Frame(score_canvas, bg="white")
    score_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    score_heading = Label(score_frame, text="YOUR SCORE", fg="black", bg="white")
    score_heading.config(font='calibri 40')
    score_heading.place(relx=0.45, rely=0.1)
    s = Label(score_frame, text=score, fg="black", bg="white")
    s.config(font='calibri 40')
    s.place(relx=0.45, rely=0.3)
    mainscreen2.mainloop()  # start the GUI
    if b == 1:
        scores = int(score)
        store_score(scores, username)


score=0
def answer(args):     # args is the argument that takes the chosen option
    global score
    ans = int(lines[i+5])
    if args == ans:
        score+=1     # if answer is correct increment the score
    mainscreen1.destroy()   # each question screen gets destroyed as soon as you click on an option

filename = "GK Quiz.txt"  # text file that contains the questions and answers
with open(filename) as f:
    global lines
    lines= f.read().splitlines()  # each line is taken as a separate element in a list
global length
length = len(lines)  # no. of items in the list


if count == 1:  # when first screen gets destroyed open the next screen
    def quiz():
        global c
        c=0
        global i
        for i in range(0, length, 6):
            global mainscreen1
            mainscreen1 = Tk()  # create a GUI window
            mainscreen1.geometry("4800x880")  # set the configuration of GUI window
            mainscreen1.title(" Question")  # set the title of GUI window

            global one_canvas
            global one_frame
            global one_heading
            one_canvas = Canvas(mainscreen1, width=4800, height=880, bg="blue")
            one_canvas.pack()
            one_frame = Frame(one_canvas, bg="white")
            one_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
            one_heading = Label(one_frame, text=lines[i], fg="black", bg="white")
            one_heading.config(font='calibri 40')
            one_heading.place(relx=0.1, rely=0.1)

            opt1 = Button(one_frame, text=lines[i+1], padx=5, pady=5, width=7, command=lambda:answer(1))
            opt1.configure(width=20, height=3, activebackground="#33B5E5", relief=FLAT)
            opt1.place(relx=0.4, rely=0.4)

            opt2 = Button(one_frame, text=lines[i+2], padx=5, pady=7, width=7, command=lambda:answer(2))
            opt2.configure(width=20, height=3, activebackground="#33B5E5", relief=FLAT)
            opt2.place(relx=0.4, rely=0.5)

            opt3 = Button(one_frame, text=lines[i+3], padx=5, pady=9, width=7, command=lambda:answer(3))
            opt3.configure(width=20, height=3, activebackground="#33B5E5", relief=FLAT)
            opt3.place(relx=0.4, rely=0.6)

            opt4 = Button(one_frame, text=lines[i+4], padx=5, pady=11, width=7, command=lambda:answer(4))
            opt4.configure(width=20, height=3, activebackground="#33B5E5", relief=FLAT)
            opt4.place(relx=0.4, rely=0.7)
            c+=1

            mainscreen1.mainloop()  # start the GUI

            if c == 5:    # signifies the end of the number of questions
                display_score()


    quiz()  # call the main_account_screen() function
