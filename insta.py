from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
import urllib

username = raw_input("Enter username: ")

chromedriver = "/home/vicodin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1120, 550)
url = 'https://instagram.com/'+ username
browser.get(url)
time.sleep(3)

body = browser.find_element_by_tag_name("body")

while True:
	body.send_keys(Keys.END)
	time.sleep(3)
	more = body.find_element_by_tag_name('button')
	disabled_btn = more.get_attribute('class')
	if disabled_btn == 'PhotoGridMoreButton pgmbDisabled':
		print "disabled button found"
		break
	else:
		more.click()

print "all photos loaded"
count = 0

photos = body.find_elements_by_class_name('pgmiThumb')
for link in photos:
	photo_src = link.get_attribute('src')
	if photo_src != None:
		photo_name = str(count)+".jpg"
		urllib.urlretrieve(photo_src, photo_name)
	else:
		pass
	count += 1
print count

html_source = browser.page_source


browser.quit()