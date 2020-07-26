### 学习笔记

#### 1.git test

#### 2.BeautifulSoup 测试代码review
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


#### 3.xpath



#### 4.scrapy
scrapy startproject maoyan_spiders #创建项目
cd maoyan_spiders
scrapy genspider maoyan maoyan.com #创建一个名称是maoyan的爬虫，生产maoyan.py文件在spiders里面

setting.py
1.DOWNLOAD_DELAY = 1 下载间隔时间
2.


scrapy crawl maoyan #启动maoyan 爬虫
