from binaries import logger

from spider_template import GGVenturesSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Aus0034Spider(GGVenturesSpider):
    name = 'aus_0034'
    start_urls = ["https://www.westernsydney.edu.au/schools/sobus/contacts"]
    country = 'Australia'
    # eventbrite_id = 1412983127

    # USE_HANDLE_HTTPSTATUS_LIST = False

    static_name = "University of Western Sydney,College of Business"
    
    static_logo = "https://www.westernsydney.edu.au/content/dam/digital/images/badges-and-logos/WSU_Logo_LeftAligned_Centred_RGB.png"

    parse_code_link = "https://www.uow.edu.au/business-law/events/"

    university_contact_info_xpath = "//div[@class='nav-content']/div[2]"
    contact_info_text = True
    # contact_info_textContent = False

    def parse_code(self,response):
        try:
        ####################
            self.driver.get(response.url)

            for link in self.events_list(event_links_xpath="//a[starts-with(@class,'uw-event-cell')]"):

                self.getter.get(link)

                if self.unique_event_checker(url_substring="https://www.uow.edu.au/events/2022/"):

                    logger.info(f"Currently scraping --> {self.getter.current_url}")

                    item_data = self.item_data_empty.copy()

                    item_data['event_name'] = WebDriverWait(self.getter,20).until(EC.presence_of_element_located((By.XPATH,"//h1[starts-with(@class,'cell')]"))).get_attribute('textContent')
                    item_data['event_link'] = link
                    try:
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//hr/following-sibling::section//div[starts-with(@class,'uw-text-block')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        item_data['event_desc'] = self.getter.find_element(By.XPATH,"//div[contains(@class,'structured-content-rich-text')]").text

                    try:
                        item_data['event_date'] = self.getter.find_element(By.XPATH,"//li[starts-with(@class,'date')]").text
                        item_data['event_time'] = self.getter.find_element(By.XPATH,"//li[starts-with(@class,'date')]").text
                    except NoSuchElementException as e:
                        logger.debug(f"Error: {e}. Using an Alternate Scraping XPATH....")
                        # item_data['event_date'] = self.getter.find_element(By.XPATH,"").text
                        # item_data['event_time'] = self.getter.find_element(By.XPATH,"").text

                    item_data['startups_contact_info'] = self.getter.find_element(By.XPATH,"//span[text()='Contact Details']/..").text
                    # item_data['startups_link'] = ''
                    # item_data['startups_name'] = ''

                    yield self.load_item(item_data=item_data,item_selector=link)

        ####################
        except Exception as e:
            self.exception_handler(e)
