from spider_template import GGVenturesSpider


class Idn0003Spider(GGVenturesSpider):
    name = 'idn_0003'
    start_urls = ['https://ipmi.ac.id/']
    country = "Indonesia"
    # eventbrite_id = 30819498834
    # TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404]

    static_name = "Indonesian Institute for Management Development,IPMI Business School"
    static_logo = "https://ipmi.ac.id/assets/images/logo.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://ipmi.ac.id/news-events"

    university_contact_info_xpath = "//div[@class='col-lg-4']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            self.mat_select_dropdown('//mat-select',"//span[text()='Upcoming Events']",wait_after_loading=True)
            self.check_website_changed(upcoming_events_xpath="//div[contains(text(),'No News & Events Foun')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=6,event_links_xpath="//div[@class='def-box-item-content']/a",next_page_xpath="//a[@aria-label='Next']",get_next_month=False,click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@class='def-box-item-content']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=['ipmi.ac.id/news-events']):
            #
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).text
            #         item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'news-content')]").text
            #         # try:
            #         #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event__body')]").text
            #         # except self.Exc.NoSuchElementException as e:
            #         #     # self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
            #         #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='event__description']").text
            #
            #         try:
            #             item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@id,'register-counter')]").text
            #             item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@id,'register-counter')]").text
            #         except self.Exc.NoSuchElementException as e:
            #             self.Func.print_log(f"XPATH not found {e}: Skipping ENTIRE EVENT.....",'debug')
            #             continue
            #
            #         # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='register-counter']").text
            #         # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@id='register-counter']").text
            #
            #         # item_data['event_date'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')
            #         # item_data['event_time'] = self.get_datetime_attributes("//span[@class='date-display-range']/span",'content')
            #
            #         # try:
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....","debug")
            #         #     # logger.debug(f"XPATH not found {e}: Skipping.....")
            #         #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #         #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
            #
            #         # try:
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(@class,'ppl-info-line')]").get_attribute('textContent')
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
            #         # item_data['startups_link'] = ''
            #         # item_data['startups_name'] = ''
            #         item_data['event_link'] = link
            #
            #         yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
