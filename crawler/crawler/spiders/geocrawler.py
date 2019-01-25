# -*- coding: utf-8 -*-
import scrapy


class GeocrawlerSpider(scrapy.Spider):
    name = 'geocrawler'
    allowed_domains = ['ftp.ncbi.nlm.nih.gov']
    start_urls = ['http://ftp.ncbi.nlm.nih.gov/']

    def parse(self, response):
        pass
