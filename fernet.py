from cryptography.fernet import Fernet

# file = open("fernet.key", 'wb')
# key = Fernet.generate_key()
# file.write(key)

fernetkey = open("fernet.key", "rb")
f = fernetkey.read()
fernetkey.close()

print(type(f))
