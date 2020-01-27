import string
import secrets
alphabet=string.ascii_letters+string.digits+string.ascii_lowercase+string.punctuation

password=''

for i in range(4):
    password+=secrets.choice(string.ascii_lowercase)
    password+=secrets.choice(string.ascii_uppercase)
    password+=secrets.choice(string.digits)
    password+=secrets.choice(string.hexdigits)


print("seed is : ",password)

char_list=list(password)
#secrets.SystemRandom().shuffle(char_list)
secrets.SystemRandom().shuffle(char_list)
password=''.join(char_list)
print("Secure password is ",password)