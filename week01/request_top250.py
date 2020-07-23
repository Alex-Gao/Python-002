import requests

#html报文头
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

#访问地址
murl = 'https://movie.douban.com/top250'
# murl = 'http://tech.163.com/special/techscience/'

header = {'user-agent': user_agent}
response = requests.get(murl,headers=header)


print(response.text)
print('返回码：%s'  % str(response.status_code))