import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="todolistpython"
)
mycursor = my_db.cursor()


def user_login():
    print("===LOGIN===")
    while True:
        user_name = input("Enter username: ")
        user_pass = input("Enter password: ")

        if user_name.strip() == "" or user_pass.strip() == "":
            print("Please fill up the username of password")
            continue
        sql = "SELECT * FROM users WHERE username= %s AND password=%s"
        values = (user_name, user_pass)

        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        if result:
            print(f"Login Successfully, Welcome {result[1]}")
            return result
        else:
            print("User not found.")
            continue


def user_register():
    print("===REGISTER===")

    while True:
        name = input("Enter name: ")
        user_name = input("Enter username: ")
        password = input("Enterpassword: ")

        if name.strip() == "" or user_name.strip() == "" or password.strip() == "":
            print("Please fill up the registration form. ")
            continue
        if len(password) < 5:
            print("Password must not less than 5.")
            continue

        sql = "INSERT INTO users (name,username,password) VALUES (%s,%s,%s)"
        values = (name, user_name, password)
        mycursor.execute(sql, values)
        my_db.commit()
        print("Register Successful")
        break


def view_list(user_id):
    sql = "SELECT * FROM list WHERE user_id=%s"
    mycursor.execute(sql, (user_id,))
    the_lists = mycursor.fetchall()

    if not the_lists:
        print("No list for the moment....")
    else:
        for x in the_lists:
            print(f"[{x[0]}],[{x[2]}]\n[{x[3]}],[{x[4]}]\n")
    print("-----------------")
    return the_lists


def add_list(user_id):
    print("===ADD LIST===")

    while True:
        list_title = input("Title: ")
        list_description = input("Description: ")

        if list_title.strip() == "" or list_description.strip() == "":
            print("Please Input Title or Description of the list")
            continue
        sql = "INSERT INTO list (user_id,title,description,status) Values(%s,%s,%s,%s)"
        mycursor.execute(
            sql, (user_id, list_title, list_description, "pending"))
        my_db.commit()
        print("Task Successfully Created")
        break


def update_list(user_id):
    print("===UPDATE LIST===")
    the_list = view_list(user_id)
    if not the_list:
        return
    try:
        the_list_id = int(input("Enter the task id to update: "))
    except ValueError:
        print("Invalid ID...")
        return

    sql = "SELECT * FROM list WHERE list_id=%s AND user_id=%s"
    mycursor.execute(sql, (the_list_id, user_id))
    result = mycursor.fetchone()
    if not result:
        print("Task not found..")
        return

    new_task_title = input("Enter Title: ")
    new_task_description = input("Enter Description: ")
    new_task_status = input("Pending/Complete: ")

    if new_task_title.strip() == "":
        new_task_title = result[2]
    if new_task_description.strip() == "":
        new_task_description = result[3]
    if new_task_status.strip() not in ("pending", "complete"):
        new_task_status = result[4]
    sql = "UPDATE list SET title=%s, description=%s,status=%s"
    val = (new_task_title, new_task_description, new_task_status)
    mycursor.execute(sql, val)
    my_db.commit()
    print("List Successfully Updated")


def delete_list(user_id):
    print("===DELETE List===")
    the_list = view_list(user_id)
    if not the_list:
        return
    try:
        list_id = int(input("Enter the list ID to Delete: "))
    except ValueError:
        print("Invalid ID....")
        return
    sql = "DELETE FROM list WHERE user_id=%s and list_id=%s"
    val = (user_id, list_id)
    mycursor.execute(sql, val)
    my_db.commit()
    print(f"{mycursor.rowcount}, list(s) Deleted ")


def list_functions(user):
    user_id = user[0]
    while True:
        print(f"\n{user[1]} To do list")
        print("[1]View\n[2]Add list\n[3]Update list\n[4]Delete List\n[5] Exit")
        choice = input("Enter choice: \n")

        if choice.strip() == "":
            print("choice cannot be empty!")
            continue
        elif choice == "1":
            view_list(user_id)
        elif choice == "2":
            add_list(user_id)
        elif choice == "3":
            update_list(user_id)
        elif choice == "4":
            delete_list(user_id)
        elif choice == "5":
            print("Goodbye...")
            break


def main_menu():
    print("=====To Do List=====")

    while True:
        print("[1] Log In\n[2]Register\n[5]Exit")
        choice = input("Enter Choice: ")
        if choice.strip() == "":
            print("choice cannot be empty.")
            continue
        elif choice == "1":
            user = user_login()
            if user:
                list_functions(user)
            break
        elif choice == "2":
            user_register()
            break
        elif choice == "5":
            print("Goodbye...")
            break


main_menu()
