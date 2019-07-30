# -*- coding: utf-8 -*-
import scrapy

class LegoSetSpider(scrapy.Spider):
    name = "lego_spider"
    start_urls = ['http://brickset.com/sets/year-2019']

    def parse(self, response):

        SET_SELECTOR = 'article.set'
        for legoset in response.css(SET_SELECTOR):

            CODE_SELECTOR = 'h1 a span::text'
            NAME_SELECTOR = 'h1 a:nth-child(1)::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            PRICE_SELECTOR = './/dl[dt/text() = "RRP"]/dd[2]/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'code': legoset.css(CODE_SELECTOR).extract_first().strip(": "),
                'name': legoset.css(NAME_SELECTOR).extract_first().strip(" "),
                'pieces': legoset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': legoset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'prices': legoset.xpath(PRICE_SELECTOR).extract_first(),
                'image': legoset.css(IMAGE_SELECTOR).extract_first(),
            }