# If you are having errors with pandas, you need to install numpy and then pandas.
# pip install numpy
# pip install pandas


# Python needs to know what you are trying to achive, so we pull commands by importing libraries
from selenium import webdriver
import time
import re
import pandas as pd
import datetime


# Step 0: Set up your defealt settings and map our your objective
# SETTINGS ADJUST THE FOLLOWING: (avoid using spaces, use underscores instead)
company = 'Saatva'
urls = ["https://www.saatva.com/"]
header = ['date','company','link','promotion'] 



# [2022 Project]

# Step 1: Scrape Data
# Open a new CHROME brower
driver = webdriver.Chrome(r'C:\Users\User\chromedriver.exe')                   # Windows users need to specify the path to chrome driver you just downloaded.
# driver = webdriver.Chrome()                                                  # For MAC

try:
    driver.get(urls[0])             # Opens the first link in "urls"
    time.sleep(2)                   # Waits for 2 secs
    driver.refresh()                # Refreshes the page to remove pop up ad
    scrape_text = driver.find_element_by_xpath('//div[@class="container bannerBase__content bannerSitewide__content"]/div[@class="bannerBase__text"]/span[@class="u-hidden--md-down"]').text
    print('Scraped: {0}'.format(scrape_text))

except Exception as e:
    print(e)

driver.close()

# Step 2: Format scraped data into a datatable

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Datetime is based on your computer's time and timezone
df = pd.DataFrame(columns=header)          # A blank table with the header as the column names
row = {}                                   # Blank dictionary to organize our information
try:
    row['date'] = now
    row['company'] = company
    row['link'] = urls[0]
    row['promotion'] = scrape_text
    print('\n row has: \n')
    print(row)
    df = df.append(row,ignore_index=True)      # Adds the "row" dictionary data to our dataframe
    print('\n df has: \n')
    print(df)

except Exception as e:
    print(e)


# Step 3: Store data

# Method 1: save locally
# Our file name will almost be unique because it is stringing company name and today's date

file_name = company+ '_' + str(datetime.date.today()) + '.csv'
try: df.to_csv(file_name,index=False)
except Exception as e: print(e)

# Method 2: Google API
# Prereq: You need to set up your Google API creditionals on your Saatva Email
import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials

key = {

}

def upload_data(sheetname,df, append = False):
    gp = gs.service_account_from_dict(key)      #Authenticate Google service account
    print('Complete: Google API connection')

    if append == False:
        sheet = gp.create(sheetname)
        sheet.share('yasuhiro.s@saatvamattress.com',perm_type='user',role='writer',notify=True)
        sheet.sheet1.update([df.columns.values.tolist()])

    else:
        sheet = gp.open(sheetname)
    row_num = 'A' +str(len(sheet.sheet1.get_all_values()) + 1)
    sheet.sheet1.update(row_num,df.values.tolist())


    print('Complete: upload_data')

sheetname = '2022 UT Capstone Demo'
upload_data(sheetname,df,append=True)

# [2021 Project]

# USED FROM AWS s3 bucketing
# pip install boto3
# import boto3
# from io import StringIO

# Used if you are not going to use pandas
# import csv
# csv_file = open(file_name, 'w', encoding='utf-8', newline='')
# writer = csv.writer(csv_file)

# When setting the column names in price_header, use the following names in the header list.
# old_price_header = ['date','company','product','size','original_price','discounted_price']
# old_header = ['date','company','product','size','comparable_saatva_product','original_price','discounted_price','discount_rate','discount_value']

# for link in urls:
#     try:
#         # Go to the page that we want to scrape, refresh to remove pop up
#         driver.get(link)
#         time.sleep(2)
#         driver.refresh()

#         # Experiment to find correct xpath
#         driver.find_element_by_xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]').click() # Click "Select Size" box
#         time.sleep(1)
        
#         details = driver.find_element_by_xpath('//ul[@class="dropdown__list is-open"]') # Highlight all details in the box
#         clean_details = details.text.split('\n')                         # ['Twin', '$799', 'Queen', ' $1,199 $1,399', ...]
#         print(clean_details)
#         df = pd.DataFrame(columns=price_header)                          # blank dataframe. A blank table
#         line = 1                                                         # Starting variable for our WHILE loop
#         while line <= len(clean_details):                                # 1 <= 10, 3<=10. Is the "line" less than or eqal to the length of "clean_details"
#             price = {}                                                   # blank dict to store our information
#             price_list = clean_details[line].split(' ')                  # Splits based on the space. There were 3 objects in this list " ", '$1,599','$1,799'
            
#             price['date'] = now                                          # dict[col] = today_date
#             price['company'] = company
#             price['product'] = 'saatva-classic'
#             price['size'] = clean_details[line-1]                        # dict[col] = list[3-1] = list[2] = "queen"

#             if len(price_list) == 3:                                     # IF the LENgth of price list is 3 execute the next 2 lines. There were 3 objects in this list " ", '$1,599','$1,799'
#                 ori_price = price_list[-1]                               # The last object in price_list is original price
#                 ori_price = ori_price.replace('$','').replace(',','')    # Removes "$" and the comma
#                 price['original_price'] = float(ori_price)               # This sets our string to be a number known as a float
                
#                 dis_price = price_list[-2]                               # the second to last object in price_list on is our discounted price
#                 dis_price = dis_price.replace('$','').replace(',','')    # Removes "$" and the comma to be a number
#                 price['discounted_price'] = float(dis_price)             # This sets our string to be a number known as a float

#             else:                                                        # OTHERWISE when the length is not 3 execute the next line INSTEAD. In this case, twin $ twinXL
#                 ori_price = price_list[-1]                               # The last object in price_list is original price
#                 ori_price = ori_price.replace('$','').replace(',','')    # Removes "$" and the comma 
#                 price['original_price'] = float(ori_price)               # This sets our string to be a number known as a float

#             df = df.append(price,ignore_index=True)                      # Adds the "price" dictionary data to our dataframe
#             #writer.writerow(price.values())
#             line = line+2                                                # line = 3 then 5, 7. Each iteration "line" increases by 2

#             # While loop ends here and rechecks it the condition statement is still true.
#             # If it is true, it repeats, other wise moves on

#     except Exception as e:
#         print(e)
#         break

# driver.close()
# # csv_file.close()

# print(df)
# df.to_csv(file_name,index=False) # Locally saved


# # Comment the following until the df is in the correct format.

# def write_to_s3(df,key):
#     client = boto3.client('s3')                                         # connects to S3 server using our AWS CLI defealt creditionals
#     out_buffer = StringIO()                                             # Buffering platform
#     df.to_csv(out_buffer, sep=',', index=False)                         # to_csv is set to a directory location OR buffering platform as memory
#     client.put_object(Bucket='ut-capstone-scraper', Key=key, Body=out_buffer.getvalue()) # uploads the data to S3 bucket "ut-captstone-scraper"


# write_to_s3(df=df,key = file_name) 

