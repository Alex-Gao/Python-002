### 学习笔记


#### 1.BeautifulSoup 测试代码review
解析html片段
```
<div class="hd">
      <a href="https://movie.douban.com/subject/1292052/" class="">
         <span class="title">肖申克的救赎</span>
            <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
         <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
     </a>
         <span class="playable">[可播放]</span>
</div>
```


代码解析：
```
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):  #tags 获取html 文件中所有的<div class="hd">
    for atag in tags.find_all('a',)        #atag 获取<a> 
        print(atag.get('href'))            #打印<a> 元素的属性  href
        #获取链接
        print(atag.find('span',).text)     #打印<a>元素中 <span>元素的值
```


#### 2.xpath
xpath的匹配效率比bs要高，xpath可以制定匹配开始位置，在某个范围内多次匹配，bs是每次从页面开始出进行匹配
例子：
```
movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]') #相对路径匹配div，属性class="movie-hover-info"
        i = 0
        for movie in movies:
            if i==10:
                break
            item = MaoyanSpidersItem()
            film_name = movie.xpath('./div[1]/@title') #在匹配到相对位置以后，子节点匹配div,属性是title 
            film_type = movie.xpath('./div[2]/text()') #初始匹配后，子节点会有多个div元素，[]可以指定第几个div
```

#### 3.scrapy
##### 常规操作
scrapy startproject maoyan_spiders #创建项目
cd maoyan_spiders
scrapy genspider maoyan maoyan.com #创建一个名称是maoyan的爬虫，生产maoyan.py文件在spiders里面
scrapy crawl maoyan #启动maoyan 爬虫

##### 参数配置 setting.py
```
1.DOWNLOAD_DELAY = 1 下载间隔时间
2.USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
3.#配置cookie， COOKIES_ENABLED，在默认DEFAULT_REQUEST_HEADERS增加Cookie
COOKIES_ENABLED = True
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie' : '__mta=150247945.1595499635438.1595726937207.1595729340863.17; uuid_n_v=v1; uuid=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; _csrf=634c86e324fd45655a9b8573209f7ba8a566fccf8026be2489dacb427f007148; mojo-uuid=cfcf00377f0f9a348eea4c5ad7401352; _lxsdk_cuid=1737b3062d0c8-01d5a4db5e5bba-1b396257-13c680-1737b3062d0c8; _lxsdk=23F353E0CCCE11EA84945F632DCF0A4DCEFE032F925645FC99EE76F3A3EFE98B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595499635,1595499962; mojo-session-id={"id":"33036e78ff22ecd0e98543118dca94e8","time":1595735429165}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595736400; __mta=150247945.1595499635438.1595729340863.1595736399650.18; _lxsdk_s=173893e4d26-243-844-b%7C%7C12'
  }
```

##### scrapy工作流程
爬虫start_requests 开始调用一次，yield scrapy.Request 获取response，使用对象的函数prase做页面解析，可嵌套多级解析。
pipline 用于存储、输出 匹配后的数据，存储的对象是item。
spider 用于爬虫匹配规则，处理数据。





