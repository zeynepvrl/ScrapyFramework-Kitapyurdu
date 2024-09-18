from pathlib import Path

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count=0
    book_count=0
    file=open("books.txt" , "a", encoding="UTF-8")        #bu class oluş oluşmaz dosya açılacak, ve en son işlemler bittinde kapanacak. aç kapa yapmak performansı kötü etkileyebilir

    start_urls = [                                 #scrapy crawl books komutunu çalıştırdında bu url den bir response döndürece ve sen o response sayfadaki her şeyi scrap crawl edebileceksin
            "https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=1"
    ]

    def parse(self, response):
        books_name=response.css("div.name.ellipsis a span::text").extract()
        books_author=response.css("div.author.compact.ellipsis a::text").extract()
        books_publisher=response.css("div.publisher span a span::text").extract()

        i=0
        while i<len(books_name):
            """ yield{
                "name":books_name[i],
                "author":books_author[i],
                "publisher":books_publisher[i]
            } """

            self.file.write("------------------------------\n")
            self.file.write(str(self.book_count)+"\n")
            self.file.write("Kitap ismi:" + books_name[i]+"\n")
            self.file.write("Yazarı:"+books_author[i]+ "\n")
            self.file.write("Yayıncı:"+books_publisher[i]+"\n")

            self.book_count+=1
            i+=1

        next_url=response.css("a.next::attr(href)").extract_first()
        self.page_count+=1
        if next_url is not None and self.page_count!=5:
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.file.close()            #yield ile json dosyasına değil de bir file a yazdırdığımız için scrapy crawl book yazmak yeterli, -o book.json eklemeye gerek yok



