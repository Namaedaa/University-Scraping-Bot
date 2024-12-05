from spider_template import GGVenturesSpider


class Usa0030Spider(GGVenturesSpider):
    name = 'usa_0030'
    start_urls = ["https://business.gmu.edu/about/contact-us"]
    country = 'US'
    # eventbrite_id = 6221361805

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "George Mason University,The School of Management"
    
    static_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/George_Mason_University_logo.svg/1280px-George_Mason_University_logo.svg.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://business.gmu.edu/about/school-business-events"

    university_contact_info_xpath = "//body"
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True
    # TRANSLATE = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
    
            # self.check_website_changed(upcoming_events_xpath="//p[text()='No events are currently published.']",empty_text=False)
            
            # self.ClickMore(click_xpath="//a[text()='View more events...']",run_script=True)
            self.Mth.WebDriverWait(self.driver, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//div[@id='trumba.spud.4']/iframe")))
              
            # for link in self.multi_event_pages(num_of_pages=8,event_links_xpath="//span[@class='twRyoPhotoEventsDescription']/a",next_page_xpath="//td[@style='vertical-align:middle;']/a[2]",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True,iframe_xpath="//div[@id='trumba.spud.4']/iframe"):
            for link in self.events_list(event_links_xpath="//span[@class='twRyoPhotoEventsDescription']/a"):
                self.getter.get(link)
                self.Mth.WebDriverWait(self.getter, 10).until(self.Mth.EC.frame_to_be_available_and_switch_to_it((self.Mth.By.XPATH,"//div[@id='trumba.spud.4']/iframe")))
                
                if self.unique_event_checker(url_substring=["https://business.gmu.edu/about/"]):
                    
                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()
                    
                    item_data['event_link'] = link

                    item_data['event_name'] = self.scrape_xpath(xpath_list=["//span[@role='heading']"])
                    item_data['event_desc'] = self.scrape_xpath(xpath_list=["//div[@class='twCustomFields']"],enable_desc_image=True)
                    item_data['event_date'] = self.scrape_xpath(xpath_list=["//span[@class='twEDStartEndRange']"],method='attr')
                    item_data['event_time'] = self.scrape_xpath(xpath_list=["//span[@class='twEDStartEndRange']"],method='attr',error_when_none=False)
                    item_data['startups_contact_info'] = self.scrape_xpath(xpath_list=["//strong[text()='Contact Info']/.."],method='attr',error_when_none=False)

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
