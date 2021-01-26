import mysql.connector
from tkinter import *
from tkinter import messagebox as mb
import datetime
import tkinter.font as tk_font

window = Tk()
window.geometry("500x325")
window.title("Lifechoices Online Login")
window.configure(bg="crimson")

# date time

q = datetime.datetime.now()

# labels
fontStyle = tk_font.Font(family="Sans-serif", size=30)

title = Label(window, text="LOGIN", font=fontStyle, background="darkslategrey", fg="white")

user_name = Label(window, text="Username:", background="darkslategrey", fg="white")

passwd = Label(window, text="Password:", background="darkslategrey", fg="white")

# key bind command to open admin login
# Ctrl + A opens up Admin Gui
# Username : "Admin"
# Password : "Admin"

window.bind('<Control-a>', lambda z: admin_form())

# Entry boxes

user_name_ent = Entry(window, width=20)
password_ent = Entry(window, width=20, show="*")

mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                               database='lifechoicesonline',
                               auth_plugin='mysql_native_password')

my_cursor = mydb.cursor()


# Login gui function


def verify():
    print("click")
    if user_name_ent.get() == "" and password_ent.get() == "":
        mb.showerror("NOTHING CAPTURED", "Please Insert A Valid Username and Password")
        user_name_ent.focus()
        password_ent.focus()
        # breakpoint()

    else:
        user = user_name_ent.get()
        pswd = password_ent.get()
        sql = "SELECT * from users where username =  %s and password = %s"
        my_cursor.execute(sql, [(user), (pswd)])
        my_cursor.fetchall()
        mydb.commit()

        x = datetime.datetime.now()
        w = x.strftime("%H:%M:%S")
        d = x.strftime("%d/%m/%y")
        mb.showinfo("Successful", "You have been Successfully Logged in")
        window.withdraw()

        # user tkinter window after login
        user_window = Tk()
        user_window.geometry("300x300")
        user_window.title("User Gui")
        user_window.configure(bg="crimson")
        # sign out window

        def close():

            t = datetime.datetime.now()
            log_off = t.strftime("%H:%M:%S")
            stmt = "INSERT INTO users_login_times(username, date, signed_in_time, signed_out_time)" \
                   " VALUES (%s, %s, %s, %s)"
            my_cursor.execute(stmt, [(user), (d), (w), (log_off)])
            mydb.commit()

            mb.showinfo("Signing Out", "You have successfully signed out")
            user_window.destroy()

        btn_sign_out = Button(user_window, text='Sign Out', command=close)
        btn_sign_out.place(x=125, y=150)
        user_window.mainloop()


# Register gui form and function below


def register_form():
    window.withdraw()
    window1 = Tk()
    window1.geometry("500x250")
    window1.title("Registration")
    window1.configure(bg="crimson")

    # labels

    title_1 = Label(window1, text="REGISTER USER")
    fl_name = Label(window1, text="Full Name:", bg="darkslategrey", fg='white')
    user_name_2 = Label(window1, text="Username:")
    passwd_1 = Label(window1, text="Password:")

    fl_name_ent = Entry(window1, width=20)
    user_name_ent_1 = Entry(window1, width=20)
    password_ent_1 = Entry(window1, width=20)

    mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                    database='lifechoicesonline', auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    # Register Function

    def register():

        print("click")
        f_name = fl_name_ent.get()
        user = user_name_ent_1.get()
        pswd = password_ent_1.get()

        try:
            sql = "insert into users (full_name, username, password) values (%s, %s, %s)"
            mycursor.execute(sql, [(f_name), (user), (pswd)])
            mydb.commit()
            window1.destroy()

            mb.showinfo("You have", "You have successfully registered")

        except IndexError:
            mb.showerror("Error", "PLease fill out the form")

    title_1.place(x=200, y=10)
    fl_name.place(x=150, y=60)
    user_name_2.place(x=150, y=100)
    passwd_1.place(x=150, y=150)

    fl_name_ent.place(x=250, y=60)
    user_name_ent_1.place(x=250, y=100)
    password_ent_1.place(x=250, y=150)

    btn_register = Button(window1, text="Register", command=register)
    btn_register.place(x=150, y=200)
    btn_return = Button(window1, text="return", command=window)
    btn_return.place(x=250, y=200)

    window1.mainloop()


# Admin Form and Function


def admin_form():
    window.destroy()
    root = Tk()
    root.geometry("500x250")
    root.title("Welcome To ADMIN")
    root.configure(bg="crimson")

    title_1 = Label(root, text="LOGIN")

    lbl_username = Label(root, text="Username:")
    lbl_password = Label(root, text="Password:")

    ent_username = Entry(root, width=20)
    ent_password = Entry(root, width=20, show="*")

    username = "Admin"
    password = "Admin"

    # Admin login function

    def login():
        try:
            if (ent_username.get()) == username and (ent_password.get()) == password:
                root.withdraw()
                admin_main_window()
                return mb.showinfo("CONGRATULATIONS", "Click Ok to continue")
            elif (ent_username.get()) == "" and (ent_password.get()) == "":
                return mb.showerror("Error", "incorrect username and password")
            elif (ent_username.get() != username or ent_password != password):
                mb.showerror("Error", "Please Enter a Valid Username and Password ")
        except IndexError:
            mb.showerror("Error", "Please Enter a Valid Username and Password ")

    def ext():
        root.destroy()

    title_1.place(x=200, y=10)

    lbl_username.place(x=150, y=60)
    lbl_password.place(x=150, y=100)

    ent_username.place(x=250, y=60)
    ent_password.place(x=250, y=100)

    btn_login = Button(text="LOGIN", command=login)
    btn_login.place(x=150, y=180)

    btn_ext = Button(text="Exit", command=ext)
    btn_ext.place(x=250, y=180)

    root.mainloop()


# Admin Option Gui


def admin_main_window():
    main_window = Tk()
    main_window.geometry("400x300")
    main_window.title("Admin Form")
    main_window.configure(bg="crimson")

    lbl_header_1 = Label(main_window, text="Select One option below: ")
    lbl_header_1.place(x=125, y=10)

    def admin_logout():
        main_window.withdraw()
        admin_form()

    def dump_data_funct():
        mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                        database='lifechoicesonline',
                                        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "[mysql dir]/bin/mysqldump -u lifechoices - @Lifechoices1234 --opt >/tmp/alldatabases.sql"

        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo("You have", "You have successfully registered")

    # Admin Add User Function

    def add_user_gui():
        main_window.withdraw()
        edit = Tk()
        edit.geometry("500x300")
        edit.title("Edit")
        edit.configure(bg="crimson")

        lbl_header_2 = Label(edit, text="Add a new user: ")
        lbl_header_2.place(x=200, y=10)
        full_name = Label(edit, text="Full Name:")
        new_user_name = Label(edit, text="Username:")
        new_user_passwd = Label(edit, text="Password:")

        new_fl_name_ent = Entry(edit, width=20)
        new_user_name_ent = Entry(edit, width=20)
        new_password_ent = Entry(edit, width=20)

        mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                        database='lifechoicesonline',
                                        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        # Add user function

        def add_user():

            try:
                new_f_name = new_fl_name_ent.get()
                new_user = new_user_name_ent.get()
                new_pswd = new_password_ent.get()
                if new_f_name and new_user and new_pswd == "":
                    mb.showerror("Error", " Failed To Add User")

                else:
                    sql = "insert into users (full_name, username, password) values (%s, %s, %s)"
                    mycursor.execute(sql, [(new_f_name), (new_user), (new_pswd)])
                    mydb.commit()
                    mb.showinfo("You have", "Successfully Added User")

            except IndexError:
                mb.showerror("Error", "Unsuccessfully added User")

        def re_turn():
            edit.withdraw()
            admin_main_window()

        full_name.place(x=50, y=80)
        new_user_name.place(x=50, y=125)
        new_user_passwd.place(x=50, y=170)

        new_fl_name_ent.place(x=150, y=80)
        new_user_name_ent.place(x=150, y=125)
        new_password_ent.place(x=150, y=170)
        btn_register_new_user = Button(edit, text="Register", command=add_user)
        btn_register_new_user.place(x=150, y=200)

        btn_return_to_main = Button(edit, text="Return", command=re_turn)
        btn_return_to_main.place(x=250, y=200)

    # Delete user Gui

    def del_user_gui():
        main_window.withdraw()
        del_window = Tk()
        del_window.geometry("500x500")
        del_window.title("Delete A User")
        del_window.configure(bg="crimson")

        lbl_header_3 = Label(del_window, text="Students: ")
        lbl_header_3.place(x=210, y=10)

        lbl_username = Label(del_window, text="Enter a Username you choose to discard:")
        lbl_username.place(x=125, y=310)

        admin_user_ent_box = Entry(del_window, width=20)
        admin_user_ent_box.place(x=180, y=345)

        dis_text = Listbox(del_window, height=15, width=50)
        dis_text.place(x=50, y=30)

        # Display all users function

        def display_users():
            mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                            database='lifechoicesonline', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            mycursor.execute('select * from users')
            mb.showinfo("complete", "Records Now on display")

            for i in mycursor:
                dis_text.insert('end', str(i))

        # Delete records function

        def delete_records():
            user_name_ = admin_user_ent_box.get()
            mydb = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                            database='lifechoicesonline',
                                            auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            sql = "Delete from users Where username = %s "
            mycursor.execute(sql, [(user_name_)])
            mydb.commit()
            mb.showinfo("You have", "You have successfully deleted a User " + str(admin_user_ent_box))

        # Exit window function

        def ext_del_window():
            del_window.destroy()

        # Refresh Function

        def re_fresh():
            del_window.withdraw()
            del_user_gui()

        def re_open_main_menu():
            del_window.withdraw()
            admin_main_window()

        btn_delete_users = Button(del_window, text="Delete", command=delete_records)
        btn_delete_users.place(x=50, y=380)

        btn_show_users = Button(del_window, text="Show Users", command=display_users)
        btn_show_users.place(x=125, y=380)

        btn_admin_ext = Button(del_window, text="Exit", command=ext_del_window)
        btn_admin_ext.place(x=235, y=380)

        btn_refresh = Button(del_window, text="Refresh", command=re_fresh)
        btn_refresh.place(x=295, y=380)

        btn_re_open_main = Button(del_window, text="Return", command=re_open_main_menu)
        btn_re_open_main.place(x=380, y=380)

    # Daily Logs Gui

    def daily_logs_users():
        main_window.withdraw()
        logs = Tk()
        logs.title("Daily Logs")
        logs.geometry('500x500')
        logs.configure(bg="crimson")

        display_logs = Listbox(logs, height=15, width=50)
        display_logs.place(x=50, y=30)

    # Return function

        def back():
            logs.withdraw()
            admin_main_window()

        # Daily logs function

        def daily_log():
            my_db = mysql.connector.connect(user='lifechoices', password="@Lifechoices1234", host='127.0.0.1',
                                            database='lifechoicesonline', auth_plugin='mysql_native_password')

            mycursor = my_db.cursor()

            mycursor.execute('select * from users_login_times')
            mb.showinfo("complete", "Records Now on display")

            for i in mycursor:
                display_logs.insert('end', str(i))

        # Close window Function

        def cls_logs_window():
            logs.destroy()

        btn_logs_daily = Button(logs, text="Display", command=daily_log)
        btn_logs_daily.place(x=125, y=380)

        btn_admin_ext = Button(logs, text="Exit", command=cls_logs_window)
        btn_admin_ext.place(x=235, y=380)

        btn_back = Button(logs, text="Return", command=back)
        btn_back.place(x=300, y=380)

        logs.mainloop()

    btn_add_user = Button(main_window, text="Add a User", command=add_user_gui)
    btn_add_user.place(x=150, y=50)

    btn_delet_user = Button(main_window, text="Delete a User", command=del_user_gui)
    btn_delet_user.place(x=140, y=100)

    btn_show_data = Button(main_window, text="Daily Log", command=daily_logs_users)
    btn_show_data.place(x=150, y=150)

    btn_dump_data = Button(main_window, text="Dump", command=dump_data_funct)
    btn_dump_data.place(x=160, y=200)

    btn_log_off_admin = Button(main_window, text="Sign-Out", command=admin_logout)
    btn_log_off_admin.place(x=150, y=250)

    main_window.mainloop()


title.place(x=200, y=10)

user_name.place(x=100, y=125)
passwd.place(x=100, y=170)

user_name_ent.place(x=200, y=125)
password_ent.place(x=200, y=170)

btn_submit = Button(text="Login", command=verify)
btn_submit.place(x=150, y=250)

btn_submit = Button(text="Register", command=register_form)
btn_submit.place(x=225, y=250)

window.mainloop()
