import scrapy

class DblpSpider(scrapy.Spider):
    name = "dblp"
    allowed_domains = ["dblp.uni-trier.de"]
    start_urls = [
        # "http://dblp.uni-trier.de/db/journals/",
        "http://dblp.uni-trier.de/db/journals/?pos=701"
    ]
    start_urls2 = [
        # "http://dblp.uni-trier.de/db/journals/",
        "http://dblp.uni-trier.de/db/journals/"
    ]
    custom_settings={
    # 'DOWNLOAD_DELAY':2,
    'COOKIES_ENABLED': False}


    def parse_author(self, response):
        print response.url
        filename = response.url.split("/")[-1] + '.html'
        with open('/home/pami/dblp_author/'+filename, 'wb') as f:
            f.write(response.body)
    def parse_journal(self,response):
        print response.url
        content_list=response.xpath('//div[@id="main"]/ul/li/a/@href').extract()
        for content in content_list:
            print content
            ff=open('/home/pami/dblp_journal_temp/'+str(content).split('/')[-1], 'w')
            ff.write(str(content))
            ff.close()
            yield scrapy.Request(content,self.parse_content)
    def parse_content(self,response):
        print response.url
        filename = response.url.split("/")[-1] + '.html'
        with open('/home/pami/dblp_journal/'+filename, 'wb') as f:
            f.write(response.body)       

    def parse(self, response):
        journal_list=response.xpath('//div[@id="browse-journals-output"]/div[@class="hide-body"]/ul/li/a/@href').extract()
        for journal in journal_list:
             print journal
             if 'pos=' in journal:
                continue
             yield scrapy.Request(journal, self.parse_journal)
        next_url=''
        next_path=response.xpath('//a[contains(@href, "pos")]')
        for path in next_path:
            fetched_next_path=path.xpath('text()').re(r'next*')
            
            if len(fetched_next_path)!=0:
                next_url=self.start_urls2[0]+path.xpath('@href').extract()[0]
                print next_url
                break
        yield scrapy.Request(next_url, self.parse)