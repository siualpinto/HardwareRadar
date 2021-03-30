from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hardwareScraper.spiders.caseking_gpu_spider import CaseKingGpuSpider
from hardwareScraper.spiders.pcdiga_gpu_spider import PcDigaGpuSpider

process = CrawlerProcess(get_project_settings())

process.crawl(PcDigaGpuSpider)
process.crawl(CaseKingGpuSpider)
process.start()
# the script will block here until the crawling is finished
