import logging
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings


class EmailSender:
    settings = get_project_settings()

    async def send_graphic_founded_email(self, url):
        mailer = MailSender.from_settings(self.settings)
        await mailer.send(to=["lsmoreira77@gmail.com"], subject="The spiders found new meat, me lord", body="You can check here:"+url+"")
        logging.info("<Email Sent>")


