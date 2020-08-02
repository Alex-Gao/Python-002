# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanSpidersPipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_date = item['film_date']
        output = f'|{film_name}|\t|{film_type}|\t|{film_date}|\n\n'
        with open('./maoyan_list_fromspider.txt', 'a+', encoding='utf8') as article:
            article.write(output)
        return item


class MySQLPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'scrapy_default')
        cls.HOST = crawler.settings.get("MYSQL_HOST", '127.0.0.1')
        cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
        cls.USER = crawler.settings.get("MYSQL_USER", 'root')
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD", '123456')
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASSWD, db=self.MYSQL_DB_NAME, charset='utf8')

    def close_spider(self, spider):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)

        return item

    def insert_db(self, tx, item):
        values = (
            item['film_name'],
            item['film_type'],
            item['film_date'],
        )
        sql = 'INSERT INTO maoyan_table VALUES (%s,%s,%s)'
        tx.execute(sql, values)