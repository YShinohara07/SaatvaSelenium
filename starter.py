from selenium import webdriver
import time
import re
import csv

# Opens a new CHROME brower
# Windows users need to specify the path to chrome driver you just downloaded.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')

# New: If you are having errors about pandas, you need to install numpy and then pandas
import pandas as pd
import datetime
now = datetime.date.today()
company = 'Saatva'
header = ['Date','Company','Product','Size','Comparable_Saatva_Product','Original_Price','Discounted_Price','Discount_rate','Discount_value']
file_name = company+ '_' + str(now) + '.csv'


urls = ["https://www.saatva.com/mattresses/saatva-classic"]
# csv_file = open(file_name, 'w', encoding='utf-8', newline='')
# writer = csv.writer(csv_file)

driver = webdriver.Chrome()
for link in urls:
    try:
        # Go to the page that we want to scrape, refresh to remove pop up
        driver.get(link)
        time.sleep(2)
        driver.refresh()

        # Click "Select Size" box
        # Experiment to find correct xpath
        # attempt1 = driver.find_element_by_xpath('//select[@class="dropdown__select"]').click()
        # Prompt from attempt above gave us a suggested xpath so we will use that
        driver.find_element_by_xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]').click()

        # Highlight all details in the box
        # attempt1 = driver.find_elements_by_xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]')
        price = {}
        
        details = driver.find_element_by_xpath('//ul[@class="dropdown__list is-open"]')
        print(details.text)
        
        clean_details = details.text.split('\n')
        line = 1
        while line <= len(clean_details):
            price['date'] = now
            price['brand'] = clean_details[line-1]
            price['details'] = clean_details[line]
            # writer.writerow(price.values())
            line+=2

    except Exception as e:
        print(e)
        break

driver.close()

df = pd.DataFrame(data=price, index=[0])
print(price)
print(df)
df.to_csv(file_name,index=False)
# csv_file.close()
