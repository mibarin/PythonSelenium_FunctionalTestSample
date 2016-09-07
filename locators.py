from selenium.webdriver.common.by import By

class Locators(object):

    TOTAL_SITES_LINKING_IN = (By.CSS_SELECTOR, '.font-4.box1-r')
    VISITORS_BY_COUNTRY_TABLE = (By.CSS_SELECTOR, '#demographics_div_country_table>tbody')
    UPGRADE_TO_VIEW_LINKS = (By.LINK_TEXT, 'Upgrade to view') # Get all links with the name
    ADVANCED_PLAN_ONLY_LINKS = (By.LINK_TEXT, 'Advanced Plan only') # Get all links with the name
    RELATED_MORE_LINK = (By.XPATH, ".//*[@id='related-content']/div[1]/span[1]/div")
    RELATED_LINKS_TABLE = (By.CSS_SELECTOR, '#related_link_table > tbody')
