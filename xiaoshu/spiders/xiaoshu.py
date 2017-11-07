import scrapy


class xiaoShu(scrapy.Spider):
    name = 'xiaoshu'
    start_urls = ["https://book.qidian.com/info/1010698093#Catalog"]

    def parse(self, response):
        li_list = response.xpath("//div[@class='volume']/ul[@class='cf']/li")
        # url_list = response.xpath("//div[@class='volume']/ul[@class='cf']/li/a/@href").extract()[0]
        li_list.reverse()
        for li in li_list:
            href ='https:' + li.xpath(".//a/@href").extract()[0]
            text = li.xpath(".//a/text()").extract()[0]
            print(text)
            yield scrapy.Request(href,
                                 callback=self.download,
                                 meta={'text':text})
    def download(self,response):
        content = response.xpath("//div[@class='read-content j_readContent']/p")
        text = response.meta['text']
        with open('xiaoshu.txt', 'a') as f:
            f.write(text + '\n')
            f.close()
        for p in content:
            pcon = p.xpath(".//text()").extract()[0]
            with open('xiaoshu.txt', 'a') as f:
                f.write(pcon+ '\n')