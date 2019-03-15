"""
This spider search in imdb webpage, extracting films by genre
"""

from scrapy import Spider, Request


class FilmSpider(Spider):
    name = 'FilmSpider'

    def __init__(self):

        self.TARGET_GENRES = ['action', 'drama']  # Target genres we want to scrape films from
        self.BASE_URL = 'https://www.imdb.com'

    def start_requests(self):
        urls = [
            self.BASE_URL + '/search/title?title_type=feature&%s=action&explore=genres&view=simple' % genre
            for genre in self.TARGET_GENRES]

        for url in urls:
            yield Request(url=url, callback=self.collect_films)

    def collect_films(self, response):
        """We get the links to the specific webapage of each film and make the requests"""

        try:

            film_urls = response.xpath(
                '//div[@class="lister-list"]/div/div[@class="lister-item-content"]//span/a/@href').extract()

            for url in film_urls:
                yield Request(url=self.BASE_URL + url, callback=self.parse_film)

        except Exception as err:
            print("Some unexpected error happened")
            print(err)

    def parse_film(self, response):
        """Parse the film information from the html and map into item"""

        print("hye")
        print("hye")
        print("hye")
        print("hye")

        # TODO: parse film to item

    # TODO: add comment crawling and extracion to items

    # TODO: add proper logs
