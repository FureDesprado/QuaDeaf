import tkinter as tk
from tkinter import messagebox


class StudentSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Student Simulator")

        # create widgets
        self.name_label = tk.Label(master, text="Name:")
        self.name_entry = tk.Entry(master)
        self.grade_label = tk.Label(master, text="Grade:")
        self.grade_entry = tk.Entry(master)
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)

        # layout widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.grade_label.grid(row=1, column=0)
        self.grade_entry.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0)
        self.quit_button.grid(row=2, column=1)

    def submit(self):
        name = self.name_entry.get()
        grade = int(self.grade_entry.get())

        if grade >= 90:
            message = "Congratulations, {}! You got an A!".format(name)
        elif grade >= 80:
            message = "Good job, {}! You got a B.".format(name)
        elif grade >= 70:
            message = "Keep working, {}! You got a C.".format(name)
        else:
            message = "Uh oh, {}! You got an F. Better luck next time.".format(name)

        # create message box
        messagebox.showinfo("Results", message)


# create main window
root = tk.Tk()

# create student simulator
simulator = StudentSimulator(root)

# start main loop
root.mainloop()