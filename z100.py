import os
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
import time

t1=time.time()
display = Display(visible=0, size=(800, 600))
display.start()
#print("displaying")

prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_experimental_option('prefs', prefs)
#driver = webdriver.PhantomJS(service_args=['--load-images=no'])

driver = webdriver.Chrome("/root/chromedriver",chrome_options=options)
driver.get("https://www.iheart.com/live/z100-1469/?pname=whtz-fm&campid=play_bar&cid=index.html")
#print(driver.page_source)
page_source=driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
#section=soup.findAll('div', attrs = {'class':'css-1whwh16'})
section=soup.find('div', attrs = {'class':'css-1whwh16'})
try:
	for i in section.findAll('a'):
		print(i.text)
except:
	pass
driver.quit()
display.stop()
print(f'Time Elapsed in Seconds: {time.time()-t1}')

os.system('pkill chrome')
os.system('pkill Xvfb')
