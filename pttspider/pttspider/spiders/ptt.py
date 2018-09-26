import scrapy
from datetime import datetime
from pttspider.items import PttspiderItem

MAX_PAGES = 2


class PTTSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.cc']

    def __init__(self, board=None):
        self.pages = 0
        self.board = 'C_Chat' if board is None else board
        self.start_urls = ('https://www.ptt.cc/bbs/{0}/index.html'.format(self.board),)

    def parse(self, response):
        self.pages += 1
        for href in response.css('.r-ent > div.title > a::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_post)

        if self.pages < MAX_PAGES:
            next_page = response.xpath(
                '//div[@id="action-bar-container"]//a[contains(text(), "上頁")]/@href')
            if next_page:
                url = response.urljoin(next_page[0].extract())
                print('follow {}'.format(url))
                yield scrapy.Request(url, self.parse)
            else:
                print('no next page')
        else:
            print('max pages reached')

    def parse_post(self, response):
        item = PttspiderItem()
        item['title'] = response.xpath(
            '//meta[@property="og:title"]/@content')[0].extract()
        item['author'] = response.xpath(
            '//div[@class="article-metaline"]/span[text()="作者"]/following-sibling::span[1]/text()')[
            0].extract().split(' ')[0]
        datetime_str = response.xpath(
            '//div[@class="article-metaline"]/span[text()="時間"]/following-sibling::span[1]/text()')[
            0].extract()
        item['date'] = datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %Y')

        item['content'] = response.xpath('//div[@id="main-content"]/text()')[
            0].extract()

        yield item
