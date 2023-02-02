# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# wait for a certain condition 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Action chain 
from selenium.webdriver.common.action_chains import ActionChains
import time 
#condition 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd 

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/manchesterunited/photos/a.411767862745/10159940615537746")

time.sleep(5)

# a function to check weather an element exists or not by xpath
def element_exists(driver, Xpath) : 
    try:
        driver.find_element(By.XPATH, Xpath  )
        return True
    except NoSuchElementException:
        return False

#most relevant

mostRelavent= driver.find_element(By.XPATH,'.//*[@class="x6s0dn4 x78zum5 xdj266r x11i5rnm xat24cr x1mh8g0r xe0p6wg"]' )

mostRelavent.click()


#all comments
allComments = driver.find_element(By.XPATH ,'.//*[@class="xu06os2 x1ok221b"]' )
allComments.click()


time.sleep(5)

#click on more comment





while  True: 
    try:

        moreComments = WebDriverWait(driver ,2).until(EC.presence_of_element_located((By.XPATH,'.//*[@class="x78zum5 x1w0mnb xeuugli"]' )))
        moreComments.click()
        #sleep 2 sec every click for loading
    except: 
        break

time.sleep(5)

# take all the comments (except the replies ) 


commentList = driver.find_elements(By.XPATH , '//div[@class="x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
comment_table = [ ]
i =0 
for cmt in commentList: 

    poster = cmt.find_element(By.CLASS_NAME, 'x3nfvp2')
    if element_exists(cmt , './/*[@class="x1lliihq xjkvuk6 x1iorvi4"]' ) == True : 
        comment= cmt.find_element(By.XPATH, './/*[@class="x1lliihq xjkvuk6 x1iorvi4"]')
    else: 

        continue
    cmt_tag = { 
        'Poster': poster.text , 
        'comment': comment.text 
    }
    comment_table.append(cmt_tag)

result= pd.DataFrame(comment_table)
print(result)
print('finished !!!')
    

driver.close()



