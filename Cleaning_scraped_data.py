# Cleaning scraped data explanation

# Disclaimer: There are many ways to do this. But this will explain the code in start.py
# The project is focused on "working" with python. Due to the interest of time, we have to skip "learning" python.


# Table of contents:
# 1. Spliting a string
# 2. Dictionary
# 3. Identifying the pattern to clean the script
# 4. Bonus - Exercise Assessment
# 5. Answer


# 1. Spliting a string

# Based on the starter.py we have the variable "details" pull our needed text from the xpath
# When we use the function "print" for details.text, we can observe the following the contexts below (without the ''' '''. This is called a doc-string)


'''
Full
$1,099 $1,299
Queen
$1,199 $1,399
King
$1,599 $1,799
Split King
$1,798 $1,998
Cal King
$1,599 $1,799
Split Cal King
$1,799 $1,999
'''

# to a machine, details will be intrepret the text as:
details = 'Full\n$1,099 $1,299\nQueen\n$1,199 $1,399\nKing\n$1,599 $1,799\nSplit King\n$1,798 $1,998\nCal King\n$1,599 $1,799\nSplit Cal King\n$1,799 $1,999'
print(details)

# We notice '\n' is recognized as new line (Note: '\t' is tab space, and '\s' has no functionality). The '\' represents the following character will be a special character
# Our objective is to format this data to be datatable friendly

# 2. Dictionary

# We will use a dictionary to acheive our goal. The following is an exmample from the W3 website
link = 'https://www.w3schools.com/python/python_dictionaries.asp'
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

# Ex column names using keys()
print( thisdict.keys() )
# Ex data using values()
print(thisdict.values() )
# Ex with column name and their respecting value grouped as a tuple using items()
print(thisdict.items() )
# Getting the text "Ford"
print(thisdict['brand'])

# Adding "new" information to our dictionary
# Lets add "Toyota Rav4 2020" to our dict
thisdict['brand'] = 'Toyota'
thisdict['model'] = 'Rav4'
thisdict['year'] = 2020
print(thisdict.items())
# We see the information from Ford was overwritten, we will come back to this concept when reviewing starter.py


# 3. Identifying the pattern to clean the script

# Lets start by dissecting the code we have
'''
        details = driver.find_element_by_xpath('//ul[@class="dropdown__list is-open"]')
        print(details.text)
        price = {}

        clean_details = details.text.split('\n')
        line = 1
        while line <= len(clean_details):
            price['brand'] = clean_details[line-1]
            price['details'] = clean_details[line]
            writer.writerow(price.values())
            line+=2
'''
# We start by spliting the string in details by '\n'. This will result in a list of strings
clean_details = details.split('\n')
print( clean_details )
print( type(clean_details) )


# We have a blank dictionary "price"... but dictionary "price" is werid so we will use "mattress"
mattress = {}

# We see there is a "while" loop. Actions will continue to loop while a condition stays "True".
# The while loop condition is "line <= len(clean_details)"
line = 1
print( len(clean_details) )
# the function "len()" counts the number of objects in the provided "object" (this is "clean_details"). It can count lists, dictionaries, tuples etc.
# Before the while loop is executed "line" is set as 1 and the length of clean_details is 12
# line "1" is less than or equal to len(clean_details) "12" so the condition is "True"

print( clean_details[line-1] )
# We see "Full", how did we get this?
# line-1 is equal to 1 - 1 which equals to 0. 
# the brackets [] represents pulling the object of the list based on its index number
# Every object in a list is assigned an index number starting at 0
print( clean_details)
# The first object in the clean_details list is "Full"
print( clean_details[0] )

print( clean_details[line] )
# We can assume the prices for associated with "Full". We can confirm this is true by looking at the website.

mattress['size'] = clean_details[line-1]
mattress['price'] = clean_details[line]
print( mattress)
# We have set the "size" and "price" and writes the information on the csv file using: writer.writerow()

line += 2
# This is a feature with python, it is equivalent to line = line + 2.
# We are at the end of the loop, the machine confirms if the condition is still "True"
print('line is equal to {}').format(line)
print( line <= len(clean_details) )
# The condition is still True, The following script is executed once again

mattress['size'] = clean_details[line-1]
mattress['price'] = clean_details[line]
print( mattress )
line+=2
# This time it is for "Queen" instead of "Full"
# We now understand the "line" was increased by 2 for formatting reasons. 


# WARNING: when working with While loops it is very easy to go on an infinite loop. Interupt the karnel or hit "control+c"



# 4. Bonus - Assessment excersize

# In the demo the clean_details is still "dirty" we want old price and the sale price. 
# Using the dictionary "mattress", print each mattress size with its regular price and its sale price.
# Bonus: transform the prices to either an integer or float

print(clean_details)
mattress = {}
line = 1

# Hints: try google the following

# python splicing
# python split function
# python while loop
# python int() 
# python float()






###############
## 5. ANSWER ##
###############

line = 1
while line <= len(clean_details):
    mattress['size'] = clean_details[line-1]
    
    prices = clean_details[line]
    print('Before cleaning:', prices)
    clean_prices = prices.split(' ')

    mattress['reg_price'] = clean_prices[1]
    mattress['sale_price'] = clean_prices[0]
    print('After cleaning',mattress)

    thousand_num = clean_prices[1][1]
    one2hund_num = clean_prices[1][-3:]
    mattress['reg_price'] = int(thousand_num + one2hund_num)

    thousand_num = clean_prices[0][1]
    one2hund_num = clean_prices[0][-3:]
    mattress['sale_price'] = int(thousand_num + one2hund_num)
    print('Bonus:',mattress)

    line+=2

