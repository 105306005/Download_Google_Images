import bs4
import requests
from selenium import webdriver
import os
import time

keyword = 'house street view'
imagename = 'house_street_view'
folder_name = 'street_view'
# scroll_page_time = 1 # 5 -> approximately 500 images in total
image_num = 1500
chromePath='/Users/maggiesun/Desktop/cra/chromedriver'

# ----- Donot need to alter below code ------------------

image_formate_list = ["png", "jpg", "jpeg"]

#creating a directory to save images
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):
    # write image to file
    # print(url)
    # if any(substring in url.lower() for substring in image_formate_list):
    try:
        reponse = requests.get(url,timeout=5)
    except:
        print(e) #should I also sys.exit(1) after this?
        return
    if reponse.status_code==200:
        with open(os.path.join(folder_name, imagename+ "_" +str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)


driver=webdriver.Chrome(chromePath)

search_URL = "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word="+keyword+"&step_word=&hs=0&pn=0&spn=0&di=7077213605308923905&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1880429803%2C3522493819&os=1191767024%2C3867661713&simid=3479929286%2C329112680&adpicid=0&lpn=0&ln=1696&fr=&fmq=1650934803167_R&fm=index&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fs2.sinaimg.cn%2Fmw690%2F001yybhBzy76g4X7zLr01%26690%26refer%3Dhttp%3A%2F%2Fs2.sinaimg.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1653526819%26t%3Dc7077eb5f3ace1f4d989b48e97ba2cfa&fromurl=ippr_z2C%24qAzdH3FAzdH3Fks52_z%26e3Bftgw_z%26e3Bv54_z%26e3BvgAzdH3F7AzdH3Fccalc9cua8ado6u1&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined"


driver.get(search_URL)

time.sleep(1)


for i in range(1, image_num):

    # if i < 170:
    #     right = driver.find_element_by_xpath("""//*[@id="container"]/span[2]/span""")
    #     right.click()
    #     print("pass")
    #     continue

    imageElement = driver.find_element_by_xpath("""//*[@id="currentImg"]""")
    imageURL= imageElement.get_attribute('src')
    # print(imageURL)

    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total." % (i, len_containers + 1))
        # print("URL: %s" % (imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))

    right = driver.find_element_by_xpath("""//*[@id="container"]/span[2]/span""")

    right.click()
    # time.sleep(1)
    

# /html/body/div/div/div/div[2]/div[1]/div[1]/a[2]
# //*[@id="imgArea"]/a[2]



# all_img = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul")
# print(all_img)
# li_list = all_img.find_elements_by_tag_name("li")

# for each_li in li_list:
#     if  each_li.find_element_by_class_name("img-layout").is_displayed() == False:
#         continue
#     test = each_li.find_element_by_class_name("img-layout")
#     ee_img = test.find_element_by_tag_name("img")

#     # ee_img = each_li.find_element_by_tag_name("img")
#     print(ee_img.get_attribute("src"))

# firstimg = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/ul/li[1]/div/a[1]/img");
# # button.click()
# print(firstimg)

# firstimg_url = firstimg.get_attribute("src")
# print(firstimg_url)




     
# while True:
# for x in range(scroll_page_time):
#     driver.execute_script('\
#     window.scrollTo(0,document.body.scrollHeight)')
     
#     # waiting for the results to load
#     # Increase the sleep time if your internet is slow
#     time.sleep(5)
     
#     new_height = driver.execute_script('\
#     return document.body.scrollHeight')
     
#     # click on "Show more results" (if exists)
#     try:
#         driver.find_element_by_css_selector(".YstHxe input").click()
     
#         # waiting for the results to load
#         # Increase the sleep time if your internet is slow
#         time.sleep(5)
     
#     except:
#         pass
     
#     # checking if we have reached the bottom of the page
#     if new_height == last_height:
#         break
     
#     last_height = new_height
#     print("scrolling "+str(x+1)+" times")


# page_html = driver.page_source
# pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
# containers = pageSoup.findAll('div', {'class':"img-layout"} )

# len_containers = len(containers)

# print(str(len_containers) + " images in total")

# # for i in range(1, len_containers+1):
# for container in containers:
#     if i % 25 == 0:
#         continue

    # xPath = """//*[@id="picPc"]/div/div[2]/div/ul/li[%s]"""%(i)


    # previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
#     try:
#         previewImageElement = driver.find_element_by_xpath(previewImageXPath)
#     except:
#         print("exception erro")
#         continue
#     previewImageURL = previewImageElement.get_attribute("src")
#     #print("preview URL", previewImageURL)


    # driver.find_element_by_xpath(xPath).click()
    # print(container.img)
    # print("-------------------")
    # each_img = container.find_element_by_tag_name("img")
    # print(each_img.get_attribute("src"))
    
#     #It's all about the wait
#     timeStarted = time.time()
#     while True:

#         # if driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""").is_displayed() == False:
#         #     break
#         try:
#             imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
#         except:
#             break

#         imageURL= imageElement.get_attribute('src')

#         if imageURL != previewImageURL:
#             #print("actual URL", imageURL)
#             break

#         else:
#             #making a timeout if the full res image can't be loaded
#             currentTime = time.time()

#             if currentTime - timeStarted > 10: #break after 10 sec
#                 print("Timeout! Will download a lower resolution image and move onto the next one")
#                 break


#     #Downloading image
#     try:
#         download_image(imageURL, folder_name, i)
#         print("Downloaded element %s out of %s total." % (i, len_containers + 1))
#         # print("URL: %s" % (imageURL))
#     except:
#         print("Couldn't download an image %s, continuing downloading the next one"%(i))

    





