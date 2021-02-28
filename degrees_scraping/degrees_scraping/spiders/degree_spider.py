import scrapy

class DegreeSpider(scrapy.Spider):
    name = 'degrees'
    start_urls = [
        'http://www.studyguideindia.com/Courses/UG-courses.asp'
    ]

    def parse(self, response):
        title = response.css('title').extract()
        yield {'titletext': title}
