from spider_template import GGVenturesSpider


class Usa0140Spider(GGVenturesSpider):
    name = 'usa_0140'
    start_urls = ["https://www.uvm.edu/business/contact_us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "University of Vermont,School of Business Administration"
    
    static_logo = "https://www.uvm.edu/sites/default/files/Grossman-School-of-Business/SI-MBA/SIMBA_logo_green.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.uvm.edu/business/grossman-school-events"

    university_contact_info_xpath = "//div[@class='field-body']"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[@rel='next']",run_script=True)
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//div[@class='search-result--content']//a",next_page_xpath="//a[@rel='next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//h3[@class='summary']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=["https://calendar.utk.edu/event"]):
                    
            for link in self.driver.find_elements(self.Mth.By.XPATH,"//div[@class='item-list']"):
                        
                self.Func.print_log(f"Currently scraping --> {self.driver.current_url}","info")

                item_data = self.item_data_empty.copy()
                
                item_data['event_link'] = self.driver.current_url

                item_data['event_name'] = link.find_element(self.Mth.By.XPATH,".//strong[@class='field-content']").text
                # item_data['event_desc'] = link.find_element(self.Mth.By.XPATH,".//tbody")
                item_data['event_date'] = link.find_element(self.Mth.By.XPATH,"./h3").text
                item_data['event_time'] = link.find_element(self.Mth.By.XPATH,".//li").text
                # item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//dd[@class='custom-field-contact_email']/.."],method='attr',error_when_none=False,wait_time=5)

                yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
