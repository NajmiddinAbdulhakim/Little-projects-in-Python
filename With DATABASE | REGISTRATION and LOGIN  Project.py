from os import system
import sys
import psycopg2

mydb = psycopg2.connect(
    host='localhost',
    user="najmiddin",
    password="1234",
    database="user_database",
    port='5432'
)
mycursor = mydb.cursor()
# mycursor.execute("create table user_info(id serial,name text,age int,profession text,login text,password text)")

class User:
    def __init__(self):
        self.user_login = None
        self.user_password = None
        self.user_name = None
        self.user_profession = None
        self.age = None
        self.all_about_users = []
        self.entering_system()
        mydb.commit()


    def entering_system(self):
        system("clear")
        enter_sys = input(self.view_welcome()+"-> ").strip()
        while enter_sys not in ["1", "2", "3"]:
            system("clear")
            print("'Input' error!")
            enter_sys = input(self.view_welcome()+"-> ").strip()
        if enter_sys == "1":
            self.register()
        elif not self.database_is_correct() and enter_sys == "2":
            self.log_in()
        else:
            sys.exit()

    def register(self):
        system('clear')
        user_name1 = input("Enter your name: ").strip().capitalize()
        while not self.name_is_correct(user_name1):
            system("clear")
            print("Error!\nConditions: to consist of a letter and more than 1 character")
            user_name1 = input("Enter your name: ").strip().capitalize()
        self.user_name = user_name1
        system("clear")
        user_age1 = input("Enter your age: ").strip()
        while not user_age1.isdigit():
            system("clear")
            print("Error!\nYou can only enter a number")
            user_age1 = input("Enter your age: ").strip()
        while int(user_age1) > 150:
            system("clear")
            user_age1 = input(f"Are you relly {user_age1} years old?\n"
                              f"Enter your aga: ")
        self.user_age = user_age1
        system("clear")
        user_profession1 = input("Enter your profession: ").strip()
        if user_profession1 == "":
            user_profession1 = "No information"
        self.user_profession = user_profession1
        system("clear")
        user_login1 = input("Enter your login: ").strip().lower()
        while not self.login_is_correct(user_login1):
            system("clear")
            print("Error!\nCondition: consists of letters and numbers and must be more than 1 character")
            user_login1 = input("Enter your login: ").strip().lower()

        if not open(self.database, "r").read() == "":
            self.get_all_user_from_db()

        while self.check_for_availability(user_login1,self.user_password):
            system("clear")
            print(f'This login is not empty: "{user_login1}"\nPlease other login entering: ')
            user_login1 = input().strip().lower()
        self.user_login = user_login1
        system("clear")
        user_password1 = input("Enter your password: ").strip().upper()
        while not self.password_is_correct(user_password1):
            system("clear")
            print("Error\nCondition: Password length must be at least 6 characters")
            user_password1 = input("Enter your password: ").strip().upper()
        system("clear")
        user_confirm_password = input("Confirm password: ").strip().upper()
        while not user_confirm_password == user_password1:
            system("clear")
            user_confirm_password = input("Error\nConfirm password: ").strip().upper()
        self.user_password = user_password1

        self.entering_info()
        self.all_about_users.clear()
        self.get_all_user_from_db()

    def log_in(self):
        if self.user_name is not None and self.user_password is not None:
            system("clear")
            print("You are already logged in")
            return
        system("clear")
        temp_login = input("Your login: ").strip().lower()
        temp_password = input("Your Password: ").strip().upper()

        self.get_all_user_from_db()
        while not self.check_for_availability(temp_login,temp_password):
            system('clear')
            print("Login or password wrong!")
            temp_login = input("Your login: ").strip().lower()
            temp_password = input("Your Password: ").strip().upper()
        print("Successfully\n")
        self.user_login = temp_login
        self.user_password = temp_password
        self.all_about_users.clear()
        self.get_all_user_from_db()

    def main_view(self):
        system('clear')
        print("What you want to do?\n\n"
              "Opportunities:\n"
              "[1] Update login:\n"
              "[2] Update password:\n"
              "[3] Log out:\n"
              "[4] Delete account:\n"
              "[5] Profile\n"
              "[6] Exit\n")
        what = input("-> ").strip()
        while not what in ["1", "2", "3", "4", "5", "6"]:
            system("clear")
            print("Invalid input!\n")
            print("What you want to do?\n\n"
                  "Opportunities:\n"
                  "[1] Update login:\n"
                  "[2] Update password:\n"
                  "[3] Log out:\n"
                  "[4] Delete account:\n"
                  "[5] Profile\n"
                  "[6] Exit\n")
            what = input("-> ").strip()

        if what == "1":
            self.update_login()
        elif what == "2":
            self.update_password()
        elif what == "3":
            self.log_out()
        elif what == "4":
            self.delete_account()
        elif what == "5":
            self.about()
        else:
            sys.exit()

    def update_login(self):
        system('clear')
        new_login = input("New login: ").strip().lower()
        while not self.login_is_correct(new_login):
            system("clear")
            print("Error!\nCondition: consists of letters and numbers and must be more than 1 character")
            user_login1 = input("Enter your login: ").strip().lower()
        while self.check_for_availability(new_login):
            print(f'This login is not empty: "{new_login}"\nPlease other login entering: ')
            new_login = input().lower().strip()
        with open(self.database, "r") as file:
            vaqtincha = file.readlines()
            with open(self.database, "w") as fille:
                for i in vaqtincha:
                    if self.user_login in i:
                        j = i.replace(self.user_login, new_login,1)
                        fille.write(j)
                    else:
                        fille.write(i)
        print("Successfully")
        self.user_login = new_login
        yubor = input('Press "Enter" to go to the menu ')
        self.main_view()

    def update_password(self):
        system('clear')
        new_pass = input("New password: ").strip().upper()
        while not self.password_is_correct(new_pass):
            system("clear")
            print("Error\nCondition: Password length must be at least 6 characters")
            new_pass = input("Enter your password: ").strip().upper()
        with open(self.database,"r") as file:
            vaqtincha = file.readlines()
            with open(self.database,"w") as fille:
                for i in vaqtincha:
                    if self.user_login in i:
                        j = i.replace(self.user_password,new_pass)
                        fille.write(j)
                    else:
                        fille.write(i)
        print("Successfully")
        self.user_password = new_pass
        yubor = input('Press "Enter" to go to the menu ')
        self.main_view()

    def log_out(self):
        self.user_name = None
        self.user_age = None
        self.user_profession = None
        self.user_login = None
        self.user_password = None
        # yubor = input('Press "Enter" to go to the general menu')
        self.entering_system()

    def delete_account(self):
        system('clear')
        dele = input("Do you want to delete the account? [y/n]: ")
        while not dele in ["Y","y","N","n"]:
            system("clear")
            print("Invalid input")
            dele = input("Select [y/n]: ")
        if dele in ["Y","y"]:
            while not self.user_password == input("Your password: ").strip().upper():
                system("clear")
                print("Password error")
            with open(self.database, "r") as file:
                vaqtincha = file.readlines()
                with open(self.database, "w") as fille:
                    for i in vaqtincha:
                        if not self.user_login in i:
                            fille.write(i)
            print("Successfully")
            yubor = input('Press "Enter" to go to the general menu ')
            self.entering_system()
        else:
            self.main_view()

    def get_all_user_from_db(self):
        with open(self.database) as file:
            falle = file.read().strip()
            for userrr in falle.split("\n"):
                self.all_about_users.append(
                    {
                    userrr.split("|")[0].split("=")[0]: userrr.split("|")[0].split("=")[1],
                    userrr.split("|")[1].split("=")[0]: userrr.split("|")[1].split("=")[1],
                    userrr.split("|")[2].split("=")[0]: userrr.split("|")[2].split("=")[1],
                    userrr.split("|")[3].split("=")[0]: userrr.split("|")[3].split("=")[1],
                    userrr.split("|")[4].split("=")[0]: userrr.split("|")[4].split("=")[1].strip()
                    }
                )

    def check_for_availability(self, login_: str, password_=None) -> bool:
        if not password_ == None:
            for user__ in self.all_about_users:
                if user__["Login"] == login_ and user__["Password"] == password_:
                    return True
            return False
        else:
            for user__ in self.all_about_users:
                if user__["Login"] == login_:
                    return True
            return False

    def entering_info(self):
        with open(self.database, "a") as entering_file:
            entering_file.write(f"Name={self.user_name}|Age={self.user_age}|Profession={self.user_profession}"
                                f"|Login={self.user_login}|Password={self.user_password}\n")

    def view_welcome(self):
        if self.database_is_correct():
            return Please select one of these options:\n[1] Register\n[2] Exit
        else:
            return Please select one of these options:\n[1] Register\n[2] Login\n[3] Exit

    @staticmethod
    def login_is_correct(loggin: str) -> bool:
        return len(loggin) > 1  and loggin.isalnum()

    @staticmethod
    def password_is_correct(passworrd: str) -> bool:
        return len(passworrd) > 5

    @staticmethod
    def name_is_correct(namme: str) -> bool:
        return len(namme) > 1 and namme.isalpha()

    def database_is_correct(self):
        return open(self.database, "r").read() == ""

    def about(self):
        self.all_about_users.clear()
        self.get_all_user_from_db()
        print(self.all_about_users)
        for i in self.all_about_users:
            if self.user_login == i['Login']:
                system("clear")
                print(f"Name: {i['Name']}\n"
                      f"Age: {i['Age']}\n"
                      f"Profession: {i['Profession']}\n"
                      f"Login: {i['Login']}\n"
                      f"Password: {i['Password'].lower()}")
        yubor = input('Press "Enter" to go to the menu ')
        self.main_view()


open('Database.txt',"a")
user = User()
"""