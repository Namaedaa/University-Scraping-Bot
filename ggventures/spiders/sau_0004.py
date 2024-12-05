from spider_template import GGVenturesSpider


class Sau0004Spider(GGVenturesSpider):
    name = 'sau_0004'
    start_urls = ['http://www.kfupm.edu.sa/Default.aspx#']
    country = "Saudi Arabia"
    # eventbrite_id = 6552000185
    TRANSLATE = True

    # handle_httpstatus_list = [301,302,403,404,429]

    static_name = "King Fahd University of Petroleum and Minerals,College of Industrial Management"
    static_logo = "http://www.kfupm.edu.sa/kfupmAssets/images/kfupm_logo_en.png"

    # MAIN EVENTS LIST PAGE
    parse_code_link = "https://news.kfupm.edu.sa/en/events/"

    university_contact_info_xpath = "//h5[text()='Stay in touch']/.."
    # contact_info_text = True
    contact_info_textContent = True
    # contact_info_multispan = True

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)
            # self.check_website_changed(upcoming_events_xpath="//main",empty_text=True)
            # self.ClickMore(click_xpath="//a[contains(@class,'moreListing')]",run_script=True)
            # for link in self.multi_event_pages(num_of_pages=5,event_links_xpath="//h5/a",next_page_xpath="//a[@class='next page-numbers']",get_next_month=True):
            for link in self.events_list(event_links_xpath="//h3/parent::a"):
                self.getter.get(link)
                if self.unique_event_checker(url_substring=['news.kfupm.edu.sa/en']):

                    self.Func.print_log(f"Currently scraping --> {self.getter.current_url}","info")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = self.Mth.WebDriverWait(self.getter,20).until(self.Mth.EC.presence_of_element_located((self.Mth.By.XPATH,"//h1"))).text
                    # item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class'block-paragraph']/pa/rent::div").text
                    try:
                        item_data['event_desc'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='block-paragraph']").text
                        item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='block-paragraph']/parent::div").text
                        item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class='block-paragraph']/parent::div").text
                    except self.Exc.NoSuchElementException as e:
                        self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')

                    # item_data['event_date'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class'block-paragraph']/parent::div").text
                    # item_data['event_time'] = self.getter.find_element(self.Mth.By.XPATH,"//div[@class'block-paragraph']/parent::div").text

                    # item_data['event_date'] = self.get_datetime_attributes("//time",'datetime')
                    # item_data['event_time'] = self.get_datetime_attributes("//time",'datetime')

                    # try:
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'modul-teaser__element')]").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....","debug")
                    #     # logger.debug(f"XPATH not found {e}: Skipping.....")
                    #     item_data['event_date'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text
                    #     item_data['event_time'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'tile__content')]").text

                    # try:
                    #     item_data['startups_contact_info'] = self.getter.find_element(self.Mth.By.XPATH,"//td[text()='Email']/following-sibling::td").text
                    # except self.Exc.NoSuchElementException as e:
                    #     self.Func.print_log(f"XPATH not found {e}: Skipping.....",'debug')
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''
                    item_data['event_link'] = link

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
