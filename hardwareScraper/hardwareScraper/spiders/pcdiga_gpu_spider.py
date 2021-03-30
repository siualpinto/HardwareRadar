import scrapy
import logging

from ..utilities.email_sender import EmailSender


class PcDigaGpuSpider(scrapy.Spider):
    name = 'pcdiga_gpu_spider'
    allowed_domains = ["pcdiga.com"]
    start_urls = [
        'https://www.pcdiga.com/componentes/placas-graficas/placas-graficas-nvidia?in-stock=1&z_gpu_model=6486-6485']
    counter = 0
    email_counter = 0
    email_sender = EmailSender()

    async def parse(self, response, **kwargs):
        no_graphic_cards_found = response.xpath("//div[@class='message info empty']")

        if not no_graphic_cards_found:
            if self.counter % 5 == 0:
                self.email_counter += 1
                await self.email_sender.send_graphic_founded_email(self.start_urls[0])
        logging.info(self.name + "<Emails Sent:" + str(self.email_counter) + ">")
        self.counter += 1
        yield response.follow(self.start_urls[0], callback=self.parse, dont_filter=True)
