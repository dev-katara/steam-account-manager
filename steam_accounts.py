import sys, json, os

try:
    with open('C:\\Users\\user\\Desktop\\Steam_Automation\\accounts.data', 'r') as d:
        accountlist = json.load(d)
    d.close()
except FileNotFoundError:
    with open('C:\\Users\\user\\Desktop\\Steam_Automation\\accounts.data', 'w') as f:
        accountlist = {}
        json.dump(accountlist,f)
    f.close()

def menu():
    opt1, opt2, opt3, opt4, opt5 = "\n1. Accounts list", "\n2. Add account", "\n3. Remove account", "\n4. Edit account", "\n5. Exit"
    print("==[Steam Accounts]=="+opt1+opt2+opt3+opt4+opt5)

def addaccount():
    uid = input("Enter an unique id: ")
    if uid in accountlist:
        print("\nUid already existed!")
    else:
        adduser = input("Account username: ")
        addpass = input("Account password: ")

        accountlist[uid] = [adduser, addpass, '1']
        print("\nAccount added successfully!")

def editmenu():
    opt1, opt2 = "\n1. Change password", "\n2. Back"
    print("==[Edit Account]=="+opt1+opt2)

def start():
    running = True

    while (running):
        menu()
        try:
            choice = int(input("\nOption: "))
        except ValueError:
            print("Only integers are allowed.")
            continue

        if choice == 1:
            if len(accountlist) >= 1:     
                display = '{:10}'.format('[UID]')+'{:20}'.format('[Account Id]')+'{:25}'.format('[Password]')+'{:5}'.format('[Active]')+"\n"
                row = ""
                for uid in accountlist:
                    row += '{:10}'.format(uid)+'{:20}'.format(accountlist[uid][0])+'{:25}'.format(accountlist[uid][1])+'{:5}'.format(accountlist[uid][2])+"\n"
                print(display + row)

                activemenu = True
            else:
                print("\nThere are no accounts yet. ")
                prompt = input("Would you like to add one? (Y/N)")

                if prompt.lower() == 'y':
                    addaccount()
                else:
                    print("It's fine!")

        elif choice == 2:

            addaccount()

        elif choice == 3:

            uid = input("Enter the unique id for deletion: ")
            if uid in accountlist:
                del accountlist[uid]
                print("\n"+ uid + " has been removed.")
                count = 0
                for account in accountlist:
                    if accountlist[account][2] == '0':
                        count += 1
                if count == len(accountlist):
                    os.remove('C:\\Users\\user\\Desktop\\Steam_Automation\\login.data')
                count = 0
            else:
                print("\nUid does not exist in database!")

        elif choice == 4:

            uid = input("Enter the unique id for edition: ")
            if uid in accountlist:
                submenu = True
                while (submenu):
                    editmenu()
                    try:
                        choice = int(input("\nOption: "))
                    except ValueError:
                        print("Only integers are allowed.")
                        continue

                    if choice == 1:
                        cpass = input("Change password to?: ")
                        accountlist[uid][1] = cpass
                        print("\nPassword has been changed!")

                    elif choice == 2:
                        submenu = False

                    else:
                        print("Invalid choice")

            else:
                print("\nUid does not exist in database!")

        elif choice == 5:
            running = False

            print("Program exited.")
            with open('C:\\Users\\user\\Desktop\\Steam_Automation\\accounts.data', 'w') as f:
                json.dump(accountlist,f)
            f.close()
            
            with open('C:\\Users\\user\Desktop\\Steam_Automation\\login.data', 'w') as f:
                for uid in accountlist:
                    credentials = [uid,accountlist[uid][0], accountlist[uid][1]]
                    json.dump(credentials,f)
            f.close()
            sys.exit(0)

        else:
            print("Invalid choice.")

if __name__ == "__main__":start()