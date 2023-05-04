# ===== By Harmony ========
from tkinter import *

root = Tk()
root.title("GPA Calculator")
root.configure(bg="#f2f2f2")

course_code = StringVar()
grade = StringVar()

courses = []
grades = []

gpa_label = Label(root, text="", font=("Helvetica", 14), bg="#f2f2f2")


def add_course():
    new_grade = grade.get()
    new_course = course_code.get()

    if not new_course:
        return

    try:
        grade_float = float(new_grade)
        if grade_float < 0 or grade_float > 100:
            raise ValueError()
    except ValueError:
        grade.set("")
        return

    grades.append(new_grade)
    courses.append(new_course)

    grade.set("")
    course_code.set("")

    for i in range(len(courses)):
        course_label = Label(root, text=f"Course Code: {courses[i]}   Score: {grades[i]}", font=("Helvetica", 12),
                             bg="#f2f2f2")
        course_label.grid(row=i + 2, column=0, padx=10, pady=5)

    if len(courses) > 0:
        gpa_button.grid(row=len(courses) + 3, column=0, pady=20, padx=10)


def calculate_gpa():
    total_points = sum(map(float, grades))
    avg_score = total_points / len(grades)
    gpa = (avg_score / 20) - 1  # convert to 5.0 scale

    gpa_label.config(text=f"Your GPA is: {gpa:.2f}")
    gpa_label.grid(row=0, column=2, padx=10)


course_label = Label(root, text="Enter Course Code:", font=("Helvetica", 12), bg="#f2f2f2")
course_label.grid(row=0, column=0, padx=10, pady=5)

course_entry = Entry(root, textvariable=course_code, width=20, font=("Helvetica", 12), relief='flat',
                     highlightthickness=1, highlightcolor='#2196f3', highlightbackground='#2196f3')
course_entry.grid(row=1, column=0, padx=10, pady=5)

grade_label = Label(root, text="Enter Grade (0-100):", font=("Helvetica", 12), bg="#f2f2f2")
grade_label.grid(row=0, column=1, padx=10, pady=5)

grade_entry = Entry(root, textvariable=grade, width=20, font=("Helvetica", 12), relief='flat', highlightthickness=1,
                    highlightcolor='#2196f3', highlightbackground='#2196f3')
grade_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = Button(root, text="Add Course", command=add_course, bg="#2196f3", fg="white", font=("Helvetica", 12), bd=0,
                    borderwidth=0, highlightthickness=0, padx=20, pady=10, relief='flat', activebackground='#2196f3',
                    activeforeground='white')
add_button.grid(row=1, column=2, padx=10, pady=5)

gpa_button = Button(root, text="Calculate GPA", command=calculate_gpa, bg="#4caf50", fg="white", font=("Helvetica", 12),
                    bd=0, borderwidth=0, highlightthickness=0, padx=20, pady=10, relief='flat',
                    activebackground='#4caf50', activeforeground='white')

root.mainloop()

# ===== By Harmony ========