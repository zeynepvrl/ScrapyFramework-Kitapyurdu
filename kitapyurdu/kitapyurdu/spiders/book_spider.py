from pathlib import Path

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count=0

    start_urls = [                                 #scrapy crawl books komutunu çalıştırdında bu url den bir response döndürece ve sen o response sayfadaki her şeyi scrap crawl edebileceksin
            "https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=1"
    ]

    def parse(self, response):
        books_name=response.css("div.name.ellipsis a span::text").extract()
        books_author=response.css("div.author.compact.ellipsis a::text").extract()
        books_publisher=response.css("div.publisher span a span::text").extract()

        i=0
        while i<len(books_name):
            yield{
                "name":books_name[i],
                "author":books_author[i],
                "publisher":books_publisher[i]
            }
            i+=1



