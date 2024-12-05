from spider_template import GGVenturesSpider


class Aus0025Spider(GGVenturesSpider):
    name = 'aus_0025'
    start_urls = ["https://www.newcastle.edu.au/school/newcastle-business-school/people/people/Professional-staff"]
    country = "Australia"
    # eventbrite_id = 12790629019

    handle_httpstatus_list = [301,302,403,404,410]

    static_name = "University of Newcastle - Australia,Graduate School of Business"
    
    static_logo = "https://www.newcastle.edu.au/__data/assets/file/0011/661727/uon-logo-square.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.newcastle.edu.au/school/newcastle-business-school/news-and-events"

    university_contact_info_xpath = "//div[@class='body-content']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//p[@class='calendar-eventTitle']/a",next_page_xpath="//i[text()='chevron_right']/parent::a",get_next_month=True,click_next_month=False,wait_after_loading=True,run_script=False):
            for link in self.events_list(event_links_xpath="//div[@id='events']//h3/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.newcastle.edu.au/events/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='body-content']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//div[@class='uon-news-meta-social']"],method='attr',error_when_none=False)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//div[@class='uon-news-meta-social']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//h5[text()='Contact']/following-sibling::*"],method='attr',error_when_none=False,wait_time=5)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)