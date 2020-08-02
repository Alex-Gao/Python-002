import scrapy
from maoyan_spiders.items import MaoyanSpidersItem
from scrapy import Selector
import lxml


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.prase)
        # callback 回调函数，引擎会将下载好的页面（response对象）打给该方法，执行数据解析
        # 使用callback指定新的函数，不适用parse作为默认的回调参数
        
                
    def prase(self, response):
        items = []
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i = 0
        for movie in movies:
            if i==10:
                break
            item = MaoyanSpidersItem()
            film_name = movie.xpath('./div[1]/@title')
            film_type = movie.xpath('./div[2]/text()')
            film_date = movie.xpath('./div[4]/text()')

            print('-------')
            print(film_name[0].extract().strip())
            print(film_type[1].extract().strip())
            print(film_date[1].extract().strip())

            item['film_name'] = film_name[0].extract().strip()
            item['film_type'] = film_type[1].extract().strip()
            item['film_date'] = film_date[1].extract().strip()
            items.append(item)
            i+=1
            


        return items
