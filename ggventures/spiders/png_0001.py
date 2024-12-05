from spider_template import GGVenturesSpider


class Png0001Spider(GGVenturesSpider):
    name = 'png_0001'
    start_urls = ['https://www.dwu.ac.pg/en/']
    country = "Papua New Guinea"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "Divine Word University (DWU),Faculty of Business and Management"
    static_logo = "https://www.dwu.ac.pg/en/images/theme_imgs/Website-logo2.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://www.dwu.ac.pg/en/index.php/294-general-dwu/222-upcoming-events"

    university_contact_info_xpath = "//div[@id='bottom2']"
    contact_info_text = True
    # contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            self.check_website_changed(upcoming_events_xpath="//div[contains(@class,'extra-upcoming-slider')]//div[contains(text(),'Has no item to show')]")
            # self.ClickMore(click_xpath="//a[contains(@class,'btn--load-more')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=3,event_links_xpath="//a[contains(@class,'fc-day-grid-event')]",next_page_xpath="//button[@class='btn btn-primary next']",click_next_month=True,wait_after_loading=True,run_script=True):
            # for link in self.events_list(event_links_xpath="//div[@data-id='eventon']//div[@class='evo_event_schema']/a"):
            #     self.getter.get(link)
            #     if self.unique_event_checker(url_substring=['www.ulatina.edu.pa/events']):
            #
            #         self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")
            #
            #         item_data = self.item_data_empty.copy()
            #
            #         item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//span[contains(@class,'evcal_event_title')]"))).get_attribute('textContent')
            #         item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@itemprop='description']").get_attribute('textContent')
            #         # try:
            #         #     item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[contains(@class,'event-desc')]").text
            #         # except self.Exc.NoSuchElementException as e:
            #         #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
            #
            #         item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(@class,'evo_eventcard_time')]").get_attribute('textContent')
            #         item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(@class,'evo_eventcard_time')]").get_attribute('textContent')
            #
            #         # item_data['event_date'] = self.get_datetime_attributes("//span[@class='date-display-single']",'content')
            #         # item_data['event_time'] = self.get_datetime_attributes("//span[@class='date-display-single']",'content')
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
            #         #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//span[contains(text(),'Contact')]/parent::li").get_attribute('textContent')
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
