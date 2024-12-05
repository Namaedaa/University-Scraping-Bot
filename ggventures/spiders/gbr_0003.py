from spider_template import GGVenturesSpider

class Gbr0003Spider(GGVenturesSpider):
    name = 'gbr_0003'
    country = 'United Kingdom'
    start_urls = ["https://www.aston.ac.uk/bss/aston-business-school"]
    # eventbrite_id = 47699605203
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Aston University,Aston Business School"
    static_logo = "https://a.storyblok.com/f/45434/170x93/020f174dcf/logo.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.aston.ac.uk/events"

    university_contact_info_xpath = "//h2[text()='Contact Us']/.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath='''//div[contains(text(),'no current')]''')
            # self.ClickMore(click_xpath="//div[contains(@class,'cal_load-button')]/button",run_script=True)
            # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='List Calendar View']")))
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//h3/a",next_page_xpath="//a[text()='>>']",get_next_month=True):
            for link in self.events_list(event_links_xpath="(//div[@class='view-content'])[2]//div[@class='news_body']/a"):
                self.logger.debug(f"LINK: |{link}|")
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['aston.ac.uk']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='content']//div[contains(@class,'body')]"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[text()='Date: ']/following-sibling::span"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[text()='Time: ']/following-sibling::span"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dt[@class='custom-field-contact']/.."],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)