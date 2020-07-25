import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


#访问地址
murl = 'https://maoyan.com/films?showType=3'    

#html报文头参数
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 
    'Cookie':'uuid_n_v=v1; uuid=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; _csrf=634c86e324fd45655a9b8573209f7ba8a566fccf8026be2489dacb427f007148; mojo-uuid=cfcf00377f0f9a348eea4c5ad7401352; _lxsdk_cuid=1737b3062d0c8-01d5a4db5e5bba-1b396257-13c680-1737b3062d0c8; _lxsdk=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595499635,1595499962; mojo-session-id={"id":"74dd8d0846f031922a491c90357d3eca","time":1595647316093}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595647327; __mta=150247945.1595499635438.1595647316257.1595647327282.8; _lxsdk_s=17383fdccb9-41c-848-528%7C%7C6'
    }
response = requests.get(murl,headers=headers)

print('返回码：%s'  % str(response.status_code))
print('------------------------')
# print(response.text)

#bs 解析
bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    print(tags.find('span', attrs={'class': 'name'}).text.strip())
    print(tags.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'}).text.strip())
    print(tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].text.strip())
    
    film_name = tags.find('span', attrs={'class': 'name'}).text.strip()
    film_date = tags.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'}).text.strip()
    film_type = tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].text.strip()
    mylist = [film_name, film_date, film_type]
    movie1 = pd.DataFrame(data=mylist)
    movie1.to_csv('./.movie.csv', encoding='utf8', index=False, mode='a', header=False)
