#!/usr/bin/env python3
# encoding: utf-8

import sys
import urllib.parse

import selenium.webdriver

def exit():
	driver.quit()
	sys.exit(0)

driver = selenium.webdriver.Firefox()
# for some reason, detectportal.firefox.com and connectivitycheck.gstatic.com are not blocked
# therefore, they cannot be used to detect connectivity
# we instead visit another site that is known not to ever have TLS
driver.get('http://neverssl.com')
if 'neverssl.com' in urllib.parse.urlparse(driver.current_url).netloc:
	exit()

driver.find_element_by_css_selector('label[for="promo_button"]').click()
driver.find_element_by_css_selector('input[alt="Next"]').click()
driver.find_element_by_css_selector('#PromotionCode').send_keys('lobby18')
driver.find_element_by_css_selector('input[alt="Connect"]').click()
exit()
