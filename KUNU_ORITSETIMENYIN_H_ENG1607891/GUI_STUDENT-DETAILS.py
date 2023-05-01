# ===== By Harmony ========
import tkinter as tk

import tkinter as tk

class FruitGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Details")  # Set the title of the GUI

        self.fruit_list = ['Apple', 'Orange', 'Banana', 'Kiwi', 'Huckleberry', 'Mango', 'Loquat', 'Bilberry', 'Cherry',
                           'Grapefruit', 'Apricot', 'Honeydew', 'Mangosteen', 'Mulberry', 'Clementine', 'Boysenberry',
                           'Lychee', 'Gooseberry', 'Blackcurrant', 'Date', 'Jambul', 'Apple', 'Feijoa', 'Grape',
                           'Guava',
                           'Elderberry', 'Blueberry', 'Nectarine', 'Jackfruit', 'Blackberry', 'Cranberry',
                           'Marionberry',
                           'Lemon', 'Dragonfruit', 'Melon', 'Coconut', 'Kumquat', 'Cantaloupe', 'Fig', 'Litchi',

                           'Raspberry', 'Damson', 'Longan', 'Currant', 'Avocado', 'Goji Berry', 'Mandarine', 'Papaya']

        self.selected_fruit = tk.StringVar()
        self.selected_fruit.set(self.fruit_list[0])

        # Create the left frame for scrolling through the fruit list
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the scrollbar and attach it to the left frame
        self.scrollbar = tk.Scrollbar(self.left_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the listbox and attach it to the left frame and scrollbar
        self.listbox = tk.Listbox(self.left_frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.listbox.yview)

        # Fill the listbox with fruits from the fruit list
        for fruit in self.fruit_list:
            self.listbox.insert(tk.END, fruit)

        # Bind a function to execute when a new selection is made in the listbox
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Create the right frame for displaying the selected fruit
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a label to display the title of the canvas
        self.title_label = tk.Label(self.right_frame, text="Draw", font=("Arial", 20))
        self.title_label.pack(padx=50, pady=10)

        # Create the canvas that displays the selected fruit
        self.canvas = tk.Canvas(self.right_frame, bg="white", height=200, width=200)
        self.canvas.pack(padx=50, pady=50)

    def on_select(self, event):
        # Get the selected fruit from the listbox and update the label and canvas
        self.selected_fruit.set(self.listbox.get(self.listbox.curselection()))
        self.title_label.config(text=self.selected_fruit.get())

        # Clear any previous drawings on the canvas
        self.canvas.delete("all")

        # Draw the selected fruit on the canvas
        if self.selected_fruit.get() == "Apple":
            self.canvas.create_oval(50, 50, 150, 150, fill="red")
            stem = self.canvas.create_rectangle(90, 20, 110, 50, fill="brown", outline="")
            self.canvas.tag_lower(stem)  # Move the stem behind the apple
        elif self.selected_fruit.get() == "Banana":
            self.canvas.create_rectangle(50, 50, 150, 100, fill="yellow")
            self.canvas.create_polygon(75, 25, 85, 5, 115, 5, 125, 25, fill="green")
        elif self.selected_fruit.get() == "Orange":
            self.canvas.create_oval(50, 50, 150, 150, fill="orange")
            leaf1 = self.canvas.create_polygon(70, 80, 60, 70, 80, 50, 90, 60, fill="green")
            leaf2 = self.canvas.create_polygon(120, 80, 130, 70, 110, 50, 100, 60, fill="green")
            self.canvas.tag_lower(leaf1, leaf2)
        else:
            self.canvas.create_text(100, 100, text="Sorry, I don't know how to draw that fruit yet.")




#=============== Creating the Input Field =================
import tkinter as tk

class StudentInfoForm(tk.Frame):
    def __init__(self, master, on_submit=None):
        super().__init__(master)

        self.on_submit = on_submit

        # Create labels for input fields
        tk.Label(self, text="Name:").grid(row=0, column=0)
        tk.Label(self, text="Age:").grid(row=1, column=0)
        tk.Label(self, text="Course of Study:").grid(row=2, column=0)
        tk.Label(self, text="School:").grid(row=3, column=0)
        tk.Label(self, text="Days of Week:").grid(row=4, column=0)
        tk.Label(self, text="Sex Type:").grid(row=5, column=0)
        tk.Label(self, text="Favorite Programming Language:").grid(row=6, column=0)

        # Create input fields
        self.name_entry = tk.Entry(self)
        self.age_scale = tk.Scale(self, from_=16, to=100, orient=tk.HORIZONTAL)
        self.course_entry = tk.Entry(self)
        self.school_entry = tk.Entry(self)

        # Create a frame for the days of the week field
        days_frame = tk.Frame(self)
        days_frame.grid(row=4, column=1, sticky="w")

        # Create a variable to store the selected days of the week
        self.selected_days = []

        # Create a list of days of the week options
        days_options = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ]

        # Set Monday as the default value for days of the week
        self.days_var = tk.StringVar(value="Monday")

        # Create a custom dropdown menu for selecting the days of the week
        days_dropdown_label = tk.Label(days_frame, textvariable=self.days_var, width=8, anchor='w')
        days_dropdown_label.pack(side=tk.LEFT, padx=(0, 5))
        days_dropdown_button = tk.Button(days_frame, text="▾", command=lambda: days_options_menu.tk_popup(days_dropdown_button.winfo_width(), days_dropdown_button.winfo_rooty()))
        days_dropdown_button.pack(side=tk.RIGHT)
        days_options_menu = tk.Menu(self, tearoff=False)
        for option in days_options:
            days_options_menu.add_command(label=option, command=lambda day=option: self.days_var.set(day))
        days_options_menu.configure(borderwidth=1)
        days_options_menu.bind("<FocusOut>", lambda event: days_options_menu.unpost())
        days_options_menu.bind("<<MenuSelect>>", lambda event: days_dropdown_label.config(fg="black"))
        days_options_menu.bind("<Leave>", lambda event: days_dropdown_label.config(fg="black"))

        self.sex_var = tk.StringVar(value="Male")
        self.sex_male_radio = tk.Radiobutton(self, text="Male", variable=self.sex_var, value="Male")
        self.sex_female_radio = tk.Radiobutton(self, text="Female", variable=self.sex_var, value="Female")
        self.language_var = tk.StringVar(value="Python")
        self.language_checkbutton = tk.Checkbutton(self, text="Python", variable=self.language_var)

        self.language_vars = [
            tk.StringVar(value="Python"),
            tk.StringVar(value="C"),
            tk.StringVar(value="C++"),
            tk.StringVar(value="Java")
        ]
        self.language_checkbuttons = [
            tk.Checkbutton(self, text="Python", variable=self.language_vars[0]),
            tk.Checkbutton(self, text="C", variable=self.language_vars[1]),
            tk.Checkbutton(self, text="C++", variable=self.language_vars[2]),
            tk.Checkbutton(self, text="Java", variable=self.language_vars[3])
        ]
        # Set the text of the Checkbutton widgets to only display the language name
        for i in range(len(self.language_checkbuttons)):
            self.language_checkbuttons[i].configure(text=self.language_vars[i].get())

            # Add the Checkbutton widgets to the form's grid
            self.language_checkbuttons[i].grid(row=6 + i // 2, column=i % 2 + 1)

        # Add input fields to grid
        self.name_entry.grid(row=0, column=1)
        self.age_scale.grid(row=1, column=1)
        self.course_entry.grid(row=2, column=1)
        self.school_entry.grid(row=3, column=1)
        self.sex_male_radio.grid(row=5, column=1)
        self.sex_female_radio.grid(row=5, column=2)
        for i in range(len(self.language_checkbuttons)):
            self.language_checkbuttons[i].grid(row=6 + i // 2, column=i % 2 + 1, pady=10)

        # Create submit button
        submit_button = tk.Button(self, text="Submit", command=self.show_info, bg='blue', fg='white',
                                  font=('Arial', 14), padx=15, pady=5)
        submit_button.grid(row=7, column=1, pady=10)

        # Create labels to display student information
        self.result_label_top = tk.Label(self, text="")
        self.result_label_bottom = tk.Label(self, text="")
        self.result_label_top.grid(row=9, columnspan=2, pady=10)
        self.result_label_bottom.grid(row=9, columnspan=2, pady=10)

    def show_info(self):
        # Get input field values
        name = self.name_entry.get()
        age = self.age_scale.get()
        course = self.course_entry.get()
        school = self.school_entry.get()
        days = self.days_var.get()
        sex = self.sex_var.get()
        languages = [var.get() for var in self.language_vars]  # Get the value of each language checkbox

        # Format student information string
        selected_languages = [language for language in languages if language != '']
        languages_string = ', '.join(selected_languages)
        student_info = f"Name: {name}\nAge: {age}\nCourse of Study: {course}\nSchool: {school}\nDays of Week: {days}\nSex Type: {sex}\nFavorite Programming Languages: {languages_string}"

        # Display student information in result label
        self.result_label_top.config(text=student_info)

        # Call the on_submit callback function if provided
        if self.on_submit is not None:
            self.on_submit(name, age, course, school, days, sex, languages)

class MyGUI:
        def __init__(self, master):
            self.master = master
            self.master.configure(bg='#f6f5f5')  # Set background color

            # Create a label for the title
            tk.Label(self.master, text="Student Details Form", font=("Helvetica", 28), bg='#f6f5f5',
                     fg='#333333').pack(
                pady=20)

            # Create a student information form and attach it to the master frame
            self.student_info_form = StudentInfoForm(self.master, on_submit=self.handle_submit)
            self.student_info_form.pack(padx=30, pady=20)

        def handle_submit(self, name, age, course, school, days, sex, languages):
            # Display the student information in the console
            print(f"\nName: {name}")
            print(f"Age: {age}")
            print(f"Course of Study: {course}")
            print(f"School: {school}")
            print(f"Days of Week: {days}")
            print(f"Sex Type: {sex}")
            print(f"Favorite Programming Languages: {', '.join(languages)}\n")

# ======================================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Details Form")

    # Create an instance of FruitGUI
    fruit_gui = FruitGUI(root)
    my_gui = MyGUI(root)

    # Run the GUI
    root.mainloop()

# ===== By Harmony ========
