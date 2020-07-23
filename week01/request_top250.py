import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

#html报文头
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

#访问地址
#murl = 'https://movie.douban.com/top250'   #页面一
murl = 'https://movie.douban.com/subject/1292052/'    #详细页面
# murl = 'http://tech.163.com/special/techscience/'

header = {'user-agent': user_agent}
response = requests.get(murl,headers=header)


#print(response.text)
print('返回码：%s'  % str(response.status_code))

#bs 解析
# bs_info = bs(response.text, 'html.parser')
# for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
#     for atag in tags.find_all('a',):
#         print(atag.get('href'))
#         #获取链接
#         print(atag.find('span',).text)

#xpath 解析
#xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称： {film_name}')  

#上映日期
film_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{film_date}')

#电影评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

mylist = [film_name, film_date, rating]

movie1 = pd.DataFrame(data=mylist)

movie1.to_csv('./.movie.csv', encoding='utf8', index=False, header=False)