# from selenium import webdriver 
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import pandas as pd 

# website ='https://www.thesun.co.uk/sport/football/'
# path ="C:\\Users\\fnac\\Downloads\\chromedriver-win64\\chromedriver.exe"

# #Headless_mode
# options = Options()
# options.headless = True
# ##############
# service = Service(executable_path=path)
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(service=service,options=options)
# driver.get(website)

# containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
# titles = []
# subtitles = []
# links = []
# for container in containers:
#     title = container.find_element(by="xpath",value='./a/span').text
#     subtitle = container.find_element(by="xpath",value='./a/h3').text
#     link = container.find_element(by='xpath',value='./a').get_attribute("href")
#     titles.append(title)
#     subtitles.append(subtitle)
#     links.append(link)

# df_headlines = pd.DataFrame({'title':titles,'subtitle':subtitles,'link':links})
# df_headlines.to_csv('headlines.csv')

# driver.quit()
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd 
from datetime import datetime
import os
import sys

application_path=os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website ='https://www.thesun.co.uk/sport/football/'
path ="C:\\Users\\fnac\\Downloads\\chromedriver-win64\\chromedriver.exe"


options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.accept_insecure_certs = True
options.add_argument("--headless=new")  # Setting headless mode

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service,options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = []

for container in containers:
    try:
        title = container.find_element(by="xpath", value='.//a/span').text
        subtitle = container.find_element(by="xpath", value='.//a/h3').text
        link = container.find_element(by='xpath', value='.//a').get_attribute("href")
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
    except Exception as e:
        print(f"Error: {e}")

df_headlines = pd.DataFrame({'title':titles, 'subtitle':subtitles, 'link':links})
file_name=f'headlines-{month_day_year}.csv'
final_path=os.path.join(application_path,file_name)
df_headlines.to_csv(f'headlines-{month_day_year}.csv', index=False)

driver.quit()

