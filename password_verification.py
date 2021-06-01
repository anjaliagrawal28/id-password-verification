import getpass

database = {"anju": "$anju58","anjali":"123"}
username = input("Enter Your Username : ")
flag =0
for i in database.keys():
    if username == i:
        password = getpass.getpass("Enter Your Password : ")
        flag=1
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
if flag==1:
    print("Verified")
else:
    print("User does not exist")
