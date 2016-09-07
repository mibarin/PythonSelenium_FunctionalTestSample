import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re
from locators import Locators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

class BasicPlanPage(BasePage):

    def get_total_site_linking(self):
        try:
            num_site_link = self.driver.find_element(*Locators.TOTAL_SITES_LINKING_IN).text
            return int(num_site_link.replace(',', ''))
        except:
            raise Exception ("total sites linking couldn't be measured.")

        return 0

    def is_visitor_listed(self, country_name):
        try:
            for row in self.driver.find_element(*Locators.VISITORS_BY_COUNTRY_TABLE).find_elements_by_tag_name('tr'):
                country = row.find_element_by_tag_name('a').text.replace(' ', '')
                if country == country_name:
                    return True
        except:
            raise Exception (country_name + " visitor in the list couldn't be validated.")

        return False

    def get_visitor_ratio(self, country_name, table_element, tag_name):
        """
        :param country_name: target country
        :param table_element: Audience Geography table element
        :param tag_name: td or th are expected
        :return: visitor ratio found on the page in float.  If the country is not found, it returns 0.
        """
        print self.is_visitor_listed(country_name)
        if self.is_visitor_listed(country_name):
            row_num = self.get_row_position(table_element, tag_name, country_name)
            counter = 0
            for row in table_element.find_elements_by_tag_name('tr'):
                counter = counter + 1
                if counter == row_num:
                    visitor_ratio = row.find_elements_by_tag_name(tag_name)[1].text
            return float(visitor_ratio.replace("%", ""))
        return 0

    def get_row_position(self, table_element, tag_name, first_column_name):
        nth_row = 0
        try:
            for row in table_element.find_elements_by_tag_name('tr'):
                nth_row = nth_row + 1
                first_column = row.find_elements_by_tag_name(tag_name)[0].text
                if first_column.replace(" ", "") == first_column_name:
                    return nth_row
        except:
            raise Exception ("get_row_position failed.")

        return 0


    def is_link_dir_correct(self, link_dir, link_text):
        #print link_text
        try:
            links = self.driver.find_elements_by_xpath('//a')
            counter = 0
            for link in links:
                if link_text == link.get_attribute('innerHTML').lower():
                    #counter = counter + 1
                    #print '\''+link.get_attribute('innerHTML') + '\''
                    print '\''+link.get_attribute('href') + '\''
                    print re.match(link_dir, link.get_attribute("href"))
                    assert re.match(link_dir, link.get_attribute("href")), "Found wrong link with " + link_text
                    return True
        except:
            raise Exception ("is_link_dir_correct failed.")

        return False

    def is_num_links_in_table_correct(self, num_links, table_element):
        """
        Assumes one table row contains 1 link.
        :param num_links: number of links to be expected
        :param table_element: WebElement of table
        :return: True if the number of rows matches with num_links and each row contains 1 link.  Otherwise, false.
        """
        try:
            row_elements = table_element.find_elements_by_tag_name('tr')
            if len(row_elements) == num_links:
                for row in row_elements:
                    num_links_in_row = len(row.find_elements_by_tag_name('a'))
                    if num_links_in_row != 1:
                        return False
                return True
        except:
            raise Exception ("is_num_links_in_table_correct failed.")

        return False
