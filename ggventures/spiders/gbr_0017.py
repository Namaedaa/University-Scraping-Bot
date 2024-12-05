from spider_template import GGVenturesSpider

class Gbr0017Spider(GGVenturesSpider):
    name = 'gbr_0017'
    country = 'United Kingdom'
    start_urls = ["https://www.lboro.ac.uk/contact/"]
    # eventbrite_id = 47699605203
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Loughborough University,Business School"
    static_logo = "https://www.lboro.ac.uk/media/wwwlboroacuk/external/styleassets/img/megamenu/LU-logo-white.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.lboro.ac.uk/departments/sbe/events/"

    university_contact_info_xpath = "//section[@id='main-content']"
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
            for link in self.events_list(event_links_xpath="//h3[@class='event-title']/a"):
                self.logger.debug(f"LINK: |{link}|")
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['lboro.ac.uk']):
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    # self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//iframe[@title='Event Detail']")))

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h3[@class='event-title']"],method='attr')
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//section//div[@class='content-wrapper']"],method='attr')
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//h5[@class='event-date']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//li[@class='time']"],method='attr')

                    # item_data['event_date'] = self.get_datetime_attributes("//div[@class='calendar']//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//p[@class='time']/time",'datetime')

                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//section[contains(@class,'contact')]"],method='attr',error_when_none=False)
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)