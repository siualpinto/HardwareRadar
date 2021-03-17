import scrapy

from ..utilities.email_sender import EmailSender


class GraphicCardSpider(scrapy.Spider):
    name = 'graphic_card_spider'
    allowed_domains = ["pcdiga.com"]
    start_urls = ['https://www.pcdiga.com/componentes/placas-graficas/placas-graficas-nvidia?in-stock=0&z_gpu_model=6486-6485']
    counter = 0

    async def parse(self, response, **kwargs):

        no_graphic_cards_found = response.xpath("//div[@class='message info empty']")

        if not no_graphic_cards_found:
            print(GraphicCardSpider.counter)
            #await EmailSender().send_graphic_founded_email(self.start_urls[0])

        if GraphicCardSpider.counter <= 100:
            GraphicCardSpider.counter += 1
            yield response.follow(self.start_urls[0], callback=self.parse)

