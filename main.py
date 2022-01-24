from helium import *
choice = input("Press 1 to reboot /n Press 2 to factory Reset")

username = "admin"
password = "password"
start_chrome(username + ':' + password + '@192.168.1.1/adv_index.htm')

if choice == 1:
    click("Reboot")
    click("Yes")
elif choice == 2:
    click("Factory Reset")
    click("Yes")
elif choice != 1 or choice != 2:
    print("Please enter 1 or 2")
