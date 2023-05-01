# ===== By Harmony ========
import tkinter as tk

class LoginSystem(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("User Login System")
        self.pack(padx=20, pady=20)

        # Create widgets for full name, email, and scale reading
        self.fullname_label = tk.Label(self, text="Full Name:", font=("Arial", 12), fg="blue")
        self.fullname_label.grid(row=0, column=0, sticky="w", padx=20, pady=20)

        self.fullname_entry = tk.Entry(self, font=("Arial", 12))
        self.fullname_entry.grid(row=0, column=1, padx=20, pady=20)

        self.email_label = tk.Label(self, text="Email:", font=("Arial", 12), fg="blue")
        self.email_label.grid(row=1, column=0, sticky="w", padx=20, pady=20)

        self.email_entry = tk.Entry(self, font=("Arial", 12))
        self.email_entry.grid(row=1, column=1, padx=20, pady=20)

        self.scale_label = tk.Label(self, text="Your Value:", font=("Arial", 12), fg="blue")
        self.scale_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.scale_value = tk.StringVar()
        self.scale_value.set("0")
        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.scale_value, bg='light grey',
                              highlightthickness=0, troughcolor='grey')
        self.scale.grid(row=2, column=1, padx=20, pady=20)

        # Create the login button
        self.login_button = tk.Button(self, text="Login", command=self.show_info, bg="#2196f3", fg="white", font=("Helvetica", 14), padx=20, pady=10,
                                      borderwidth=0, highlightthickness=0, relief='flat', activebackground='#2196f3')
        self.login_button.grid(row=3, column=0, columnspan=3, pady=10)

    def show_info(self):
        # Create a new window to show user information
        info_window = tk.Toplevel(self)
        info_window.title("Submitted Information Details")
        info_window.geometry("300x250")

        fullname_text = "Full Name: " + self.fullname_entry.get()
        email_text = "Email: " + self.email_entry.get()
        scale_text = "Scale Reading: " + self.scale_value.get()

        fullname_label = tk.Label(info_window, text=fullname_text)
        fullname_label.pack(padx=10, pady=10)

        email_label = tk.Label(info_window, text=email_text)
        email_label.pack(padx=10, pady=10)

        scale_label = tk.Label(info_window, text=scale_text)
        scale_label.pack(padx=10, pady=10)

        # Create the close button
        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack(pady=30)

# Create the main window and run the application
root = tk.Tk()
app = LoginSystem(master=root)
app.mainloop()

# ===== By Harmony ========
