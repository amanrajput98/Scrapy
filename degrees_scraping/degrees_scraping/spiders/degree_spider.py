import scrapy
import csv
from pathlib import Path

class DegreeSpider(scrapy.Spider):
    name = 'degrees'
    start_urls = [
        'http://www.studyguideindia.com/Courses/UG-courses.asp'
    ]
    # field names  
    fields = ['full_degree_name','short_degree_name']  
    # data rows of csv file  
    rows = list()
    def parse(self, response):
        degree_result = response.css('div.tab_inner_full_2col ul.PB6 li a::text').extract()
        final_result = [degree.replace(u'\xa0', u' ').strip() for degree in degree_result if isinstance(degree,str) and degree]
        with open(Path(__file__).parent / "../data/degree_names.csv", 'a', newline='') as f:
            # degrees_scraping\degrees_scraping\data\degreeNames.csv
            deg_f = csv.writer(f)
            deg_f.writerow(self.fields)
            for degree in final_result:
                if '(' in degree:
                    self.rows.append([degree.split('(')[0].strip(), degree.split('(')[1].strip()[:-1]])
            deg_f.writerows(self.rows)
        yield {'response_text': final_result}
