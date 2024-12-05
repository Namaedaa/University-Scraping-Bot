from spider_template import GGVenturesSpider

class Gbr0027Spider(GGVenturesSpider):
    name = 'gbr_0027'
    country = 'United Kingdom'
    start_urls = ["https://www.rgu.ac.uk/contact-us"]
    # eventbrite_id = 155395205
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Robert Gordon University,Aberdeen Business School"
    static_logo = "https://www.rgu.ac.uk/templates/rgu/images/rgu_logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.rgu.ac.uk/events"

    university_contact_info_xpath = "//div[@id='gwInfo']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//div[@id='content-bottom']//a",checking_if_none=True)
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//div[@class='preview-text']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['rgu.ac.uk']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@id='article-content']","//div[@id='article-panel']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='publish-date']","//div[@class='publish-date']/p","//div[@id='article-content']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='publish-date']","//div[@class='publish-date']/p","//div[@id='article-content']"],method='attr')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=[''])
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)