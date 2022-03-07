import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                "titulos": filmes.css('.titleColumn a::text').get(),
                "anos": filmes.css('.secondaryInfo::text').get(),
                "avalicao": response.css('strong::text').get()
            }

        pass
