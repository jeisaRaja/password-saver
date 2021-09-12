from cryptography.fernet import Fernet

fernetkey = open("fernet.key","rb")
key = fernetkey.read()
fernetkey.close()
def view(key):
    file = open("pwbank.txt", 'rb')
    f = Fernet(key)
    for i in file:
        read_pwd = i.strip()
        real_pwd = f.decrypt(read_pwd)
        print(real_pwd)
        choose()


def create(key):
    file = open("pwbank.txt", 'ab')
    account = input("Password For: ")
    pwd = input("Password: ")
    f = Fernet(key)
    combine = account  + " : " +  pwd
    combineb = f.encrypt(f'{combine}'.encode('utf-8'))
    file.write(combineb+b'\n')
    file.close()
    choose()
def choose():
    print("Hello! This is your passwords bank\npress 1 to view your password \npress 2 to add new password\nYour input: ")
    x = int(input())
    if x == 1:
        view(key)

    elif x == 2:
        create(key)


choose()


