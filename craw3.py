import bs4
import requests
from selenium import webdriver
import os
import time

keyword = 'home solar battery bank'
imagename = 'home_solar_battery_bank'
folder_name = 'solar_bat'
scroll_page_time = 10 # 5 -> approximately 500 images in total
chromePath='/Users/maggiesun/Desktop/cra/chromedriver'

# ----- Donot need to alter below code ------------------

image_formate_list = ["png", "jpg", "jpeg"]

#creating a directory to save images
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):
    # write image to file
    # print(url)
    if any(substring in url.lower() for substring in image_formate_list):
        try:
            reponse = requests.get(url,timeout=5)
        except:
            print(e) #should I also sys.exit(1) after this?
            return
        if reponse.status_code==200:
            with open(os.path.join(folder_name, imagename+ "_" +str(num)+".jpg"), 'wb') as file:
                file.write(reponse.content)


driver=webdriver.Chrome(chromePath)

search_URL = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'
driver.get(search_URL)


a = input("Waiting...")

# scroll_down

driver.maximize_window()
last_height = driver.execute_script('\
        return document.body.scrollHeight')
     
# while True:
for x in range(scroll_page_time):
    driver.execute_script('\
    window.scrollTo(0,document.body.scrollHeight)')
     
    # waiting for the results to load
    # Increase the sleep time if your internet is slow
    time.sleep(3)
     
    new_height = driver.execute_script('\
    return document.body.scrollHeight')
     
    # click on "Show more results" (if exists)
    try:
        driver.find_element_by_css_selector(".YstHxe input").click()
     
        # waiting for the results to load
        # Increase the sleep time if your internet is slow
        time.sleep(3)
     
    except:
        pass
     
    # checking if we have reached the bottom of the page
    if new_height == last_height:
        break
     
    last_height = new_height
    print("scrolling "+str(x+1)+" times")


page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )

len_containers = len(containers)

print(str(len_containers) + " images in total")

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue

    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    try:
        previewImageElement = driver.find_element_by_xpath(previewImageXPath)
    except:
        print("exception erro")
        continue
    previewImageURL = previewImageElement.get_attribute("src")
    #print("preview URL", previewImageURL)


    driver.find_element_by_xpath(xPath).click()
    
    #It's all about the wait
    timeStarted = time.time()
    while True:

        if driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""").is_displayed() == False:
            continue
        imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
        imageURL= imageElement.get_attribute('src')

        if imageURL != previewImageURL:
            #print("actual URL", imageURL)
            break

        else:
            #making a timeout if the full res image can't be loaded
            currentTime = time.time()

            if currentTime - timeStarted > 10: #break after 10 sec
                print("Timeout! Will download a lower resolution image and move onto the next one")
                break


    #Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total." % (i, len_containers + 1))
        # print("URL: %s" % (imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))

    





