# -*- coding: utf-8 -*-
import scrapy
import urllib.request


class GeocrawlerSpider(scrapy.Spider):
    name = 'geocrawler'
    allowed_domains = ['ftp.ncbi.nlm.nih.gov']
    base_url = 'https://ftp.ncbi.nlm.nih.gov/geo/series/%s/%s/matrix/'

    def start_requests(self):
        with open("../../../log_err.txt") as f:
            for i in f:
                first_part = i[:5] + "nnn"
                start_urls = self.base_url % (first_part, i[:8])
                yield scrapy.Request(start_urls, self.parse, meta = {"item": i[:8], "first_part": first_part})

        # pegar o topo e remover o valor da lista
        # baixar o documento pegar o link para download
        # descompactar e salvar na pasta de data

    def parse(self, response):
        links = response.css("a::attr(href)").extract()[1:]
        item = response.meta["item"]
        first_part = response.meta["first_part"]
        count = 0
        download_fail = []
        for link in links:
            try:
                url = self.base_url % (first_part, item) + link
                count += 1
                file_name = "../../../data/err_files/{0}_series_matrix{1}.txt.gz".format(item, count)
                urllib.request.urlretrieve(url, file_name)  
            except Exception as error:
                print(error)
                count -= 1
                download_fail.append(item)

        print("downloads finalizados")
        self.log_err(download_fail)

    def log_err(self, download_fail):
        #build file to sabe err
        log_err = open("../../../log_err_from_err.txt", "a")
        for i in download_fail:
            log_err.write(i + "\n")
        log_err.close()
