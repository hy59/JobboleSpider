# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # get all articles post urls
        post_urls = response.css('#archive .floated-thumb .post-thumb a::attr(href)').extract()
        for post_url in post_urls:
            print(post_url)
        # title
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # create_date
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·','').strip()
        # parise_nums
        praise_nums = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract()[0]
        #bookmark_nums
        bookmark_nums = response.xpath('//span[contains(@class, "bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*?(\d+).*", bookmark_nums)
        if match_re:
            bookmark_nums = match_re.group(1)
        # comment_nums
        comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        # content
        content = response.xpath('//div[@class="entry"]').extract()[0]
        # tag_list
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)
        pass
