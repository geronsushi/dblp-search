import scrapy
next_path=''
class DblpSpider(scrapy.Spider):
    name = "dblp"
    allowed_domains = ["dblp.uni-trier.de"]
    start_urls = [
        "http://dblp.uni-trier.de/pers/?pos=1500201"
    ]
    start_urls2 = [
        "http://dblp.uni-trier.de/pers/"
    ]
    custom_settings={
    # 'DOWNLOAD_DELAY':2,
    'COOKIES_ENABLED': False}


    def parse_author(self, response):
        if 'pos=' in response.url:
            return
        print response.url

        filename = response.url.split("/")[-1] + '.html'
        with open('/home/pami/dblp_author/'+filename, 'wb') as f:
            f.write(response.body)
            print next_path

    def parse(self, response):
        author_list=response.xpath('//div[@class="columns hide-body"]/div[@class="column min20"]/ul/li/a/@href').extract()
        for author in author_list:
            if 'pos=' in author:
                continue
            print author
            ff=open('/home/pami/dblp_author_temp/'+str(author).split('/')[-1], 'w')
            ff.write(str(author))
            ff.close()
            # yield scrapy.Request(author, self.parse_author)
        next_url=''
        next_path=response.xpath('//a[contains(@href, "pos")]')
        for path in next_path:
            fetched_next_path=path.xpath('text()').re(r'next*')
            
            if len(fetched_next_path)!=0:
                next_url=self.start_urls2[0]+path.xpath('@href').extract()[0]
                print next_url
                break
        yield scrapy.Request(next_url, self.parse)