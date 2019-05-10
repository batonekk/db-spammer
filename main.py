import requests, os, random, string, json
from random import randint

requrl = '....'
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
names = json.loads(open('names.json').read())
emails = json.loads(open('emails.json').read())
passwords = json.loads(open('passwords.json').read())

for name in names:
    namesRandom = random.choice(names)
    emailDomain = random.choice(emails)
    nameNumbers = ''.join(random.choice(string.digits))
    username = namesRandom.lower() + nameNumbers + '@'+ emailDomain

    whatPassword = randint(0, 2)

    if whatPassword == 0:
        password =''.join(random.choice(chars) for i in range(12))
        pass

    if whatPassword == 1:
        password = random.choice(passwords)
        pass

    if whatPassword == 2:
        password1 = random.choice(passwords)
        password2 = random.choice(passwords)
        password = password1 + password2
        pass

    requests.post(requrl, data={
    'login': username,
    'password': password
    })

    print ('username: %s \n password: %s \n \n' % (username,password))
pass
