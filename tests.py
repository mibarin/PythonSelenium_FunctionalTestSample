import unittest
from selenium import webdriver
import page
from locators import Locators
import time


class TestCNNUSPage(unittest.TestCase):

   def setUp(self):
       site = "cnn.com"
       self.user_country = "Austraria"
       self.upsel_upgrade_dir = "http://www.alexa.com/plans"

       self.upsel_upgrade_dir_dict = \
           {
               'http://www.alexa.com/plans': ('audience overlap tool', 'competitor keyword matrix'),
               'http://www.alexa.com/plans\?ax_atid=': ('upgrade to view', 'advanced plan only')
           }

       self.num_related_links = 10
       self.driver = webdriver.Firefox()
       self.driver.delete_all_cookies()
       self.driver.get("http://www.alexa.com/siteinfo/" + site)
       self.driver.set_window_size(1580,850)
       self.page = page.BasicPlanPage(self.driver)

  # c.	All upgrade/upsell links lead to /plans (sometimes there will be additional URL params)
   def test_is_upgrade_link_dir_correct(self):
       urls = self.upsel_upgrade_dir_dict.keys()
       link_texts = self.upsel_upgrade_dir_dict.values()
       num_urls = len(urls)
       url_counter = 0
       for url in urls:
           print url
           link_texts_for_url = link_texts[url_counter]
           num_link_texts = len(link_texts)
           print num_link_texts
           link_counter = 0
           while link_counter < num_link_texts:
               print link_texts_for_url[link_counter]
               print "hello"
               assert self.page.is_link_dir_correct(url, link_texts_for_url[link_counter]), "Flaws in " + link_texts_for_url[link_counter]
               link_counter = link_counter + 1

           url_counter = url_counter +1
        #assert self.page.is_link_dir_correct(self.upsel_upgrade_dir, 'upgrade to view'), "Upgrade to View links have a flaw."
        #assert self.page.is_link_dir_correct(self.upsel_upgrade_dir, 'advanced plan only'), "Advanced Plan Only links have a flaw."
        #assert self.page.is_link_dir_correct(self.upsel_upgrade_dir, 'audience overlap tool'), "Audience Overlap Tool links have a flaw."
        #assert self.page.is_link_dir_correct(self.upsel_upgrade_dir, 'competitor keyword matrix'), "Competitor Keyword Matrix links have a flaw."



   def tearDown(self):
        #print("done")
        self.driver.quit()


'''
  # a.	Sites linking in is larger than 100,000.
   def test_is_sites_linking_over_ahundredk (self):
        assert self.page.get_total_site_link() > 100000, "Sites linking is equal to or less than 100,000."

  # b.	At least 5% of visitors are from Australia.
   def test_is_visitors_at_least_5percent(self):
        table_element = self.driver.find_element(*Locators.VISITORS_BY_COUNTRY_TABLE)
        assert self.page.get_visitor_ratio(self.user_country, table_element, "td") >= 5, "Ratio of visitor from " + self.user_country + " is less than 5%"

  # d.	That there are 10 related links in the "Related Links" table.
   def test_is_num_related_links_correct(self):
        table_element = self.driver.find_element(*Locators.RELATED_LINKS_TABLE)
        assert self.page.is_num_links_in_table_correct(self.num_related_links, table_element), "The number of related links is not" + str(self.num_related_links) + "."

'''
if __name__ == '__main__':
    unittest.main(verbosity=2)

#suite = unittest.TestLoader().loadTestsFromTestCase(TestCNNUSPage)
#unittest.TextTestRunner(verbosity=1).run(suite)
