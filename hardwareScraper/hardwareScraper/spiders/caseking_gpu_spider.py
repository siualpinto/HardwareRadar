import logging
import scrapy

from ..utilities.email_sender import EmailSender


class CaseKingGpuSpider(scrapy.Spider):
    name = 'caseking_gpu_spider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1: +http://www.google.com/bot.html)',
    }
    allowed_domains = ["pcdiga.com"]
    start_urls = [
        'https://www.caseking.de/en/pc-components/graphics-cards/nvidia/geforce-rtx-3060-ti?sPage=1&sPerPage=48']
    # 'https://www.caseking.de/en/pc-components/graphics-cards/nvidia/geforce-rtx-3070?sPage=1&sPerPage=48']
    counter = 0
    email_counter = 0
    email_sender = EmailSender()

    async def parse(self, response, **kwargs):
        gpu_found = response.xpath("//div[@class='Physical']/following::div[@class='status2']")

        if gpu_found:
            if self.counter % 5 == 0:
                self.email_counter += 1
                await self.email_sender.send_graphic_founded_email(self.start_urls[0])
        logging.info(self.name + "<Emails Sent:" + str(self.email_counter) + ">")
        self.counter += 1
        yield response.follow(self.start_urls[0], callback=self.parse, dont_filter=True)
