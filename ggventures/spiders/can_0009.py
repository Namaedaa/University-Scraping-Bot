from spider_template import GGVenturesSpider


class Can0009Spider(GGVenturesSpider):
    name = "can_0009"
    start_urls = ["https://www.mbaib.gsbs.tsukuba.ac.jp/contact-us/"]
    country = "Canada"
    # eventbrite_id = 8447939505
# 
    handle_httpstatus_list = [301,302,403,404]

    static_name = "Queen's University,Queen's School of Business"
    
    static_logo = "https://smith.queensu.ca/_templates/images/content/grad_studies/mma/smith-logo-white.svg"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.queensu.ca/innovationcentre/upcoming-events"

    university_contact_info_xpath = "//footer"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//div[starts-with(@class,'events-container')]",empty_text=True)
            
            # self.ClickMore(click_xpath="//button[text()='View More']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='post_meta']/h2/a",next_page_xpath="//th[@class='next']",get_next_month=False,click_next_month=True,wait_after_loading=False,run_script=True):
            for link in self.events_list(event_links_xpath="//h5[@class='card-title']/a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=["https://www.queensu.ca/innovationcentre"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//h1"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='container event-details-window']"],enable_desc_image=True,error_when_none=False)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//p[text()='Date']/.."],method='attr',error_when_none=False,wait_time=5)
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//p[text()='Date']/.."],method='attr',error_when_none=False,wait_time=5)
                    # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//div[contains(@class,'Contact')]"],method='attr',error_when_none=False,wait_time=5)
# 
                    yield self.load_item(item_data=item_data,item_selector=link)

        ###################
        except Exception as e:
            self.exception_handler(e)
