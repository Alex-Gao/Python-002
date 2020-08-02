import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://shimo.im/login?from=home'
}
s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
    'mobile' : '+8618217264079',
    'password' : '1qaz2wsx',
}

response = s.post(login_url, data=form_data, headers = headers)
print(response.text)

url2 = 'https://shimo.im/desktop'

response2 = s.get(url2, headers=headers)
print(response2.status_code)
print(response2.text)