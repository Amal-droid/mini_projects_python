from cryptography.fernet import Fernet

'''
def write_key():
    key =Fernet.generate_key()
    with open("key.key","wb") as key_file:    ##To genrate key##
        key_file.write(key)
write_key()   '''     

def load_key():
    file = open("key.key","rb")##Taking key from key file##
    key =file.read()
    file.close()
    return key

                
key=load_key()   
fer =Fernet(key)

def add():
    name = input("input account name:  ")
    pwd = input("enter password:  ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+"\n")

 
def view():
    with open('password.txt','r')as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw =data.split("|")
            print("user=",user,"password=",fer.decrypt(passw.encode()).decode(),"\n")
while True:
    mode = input("would you like to view passwords or view existing ones? (view,add)press q to quit :  ").lower()
    if mode == "q":
        quit()
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid \n")
        continue    