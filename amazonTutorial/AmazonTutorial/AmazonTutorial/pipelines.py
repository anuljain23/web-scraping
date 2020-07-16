# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AmazontutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("amazon_books.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_tb""")
        self.curr.execute("""CREATE TABLE books_tb(
                        title text,
                        author text,
                        price int,
                        imagelink CHARACTER(255)
                        )""")

    def store_db(self, item):

        self.curr.execute("""INSERT INTO books_tb values (?,?,?,?)""",(
                        item['product_name'][0],
                        item['product_author'][0],
                        item['product_price'][0],
                        item['product_imagelink'][0]
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
