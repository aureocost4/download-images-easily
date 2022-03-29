from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import io
import os, os.path
from PIL import Image

from script import files

wd = Service(files.CHROMEDRIVER_PATH)
option = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=wd, options=option)

pagination = 3
max_pagination = 4
max_images = 100


def run():
    files.directory_exists()
    get_images(pagination)


def scroll_down(updatedScroll):  
    browser.execute_script(f'''window.scrollTo("0", "{updatedScroll}")''')


def click_event(name):
    button = browser.find_element(By.CLASS_NAME, name)
    button.click()   


def get_images(pagination):
    
    print("current pagination = " + str(pagination))   
    
    URL = "https://br.freepik.com/search?format=search&page=" + str(pagination) + "&query=pessoa&type=photo"      
    browser.get(URL)
    
    image_urls = set()
    index = 1
    updatedScroll = 0
    scrollHeight = int(browser.execute_script("return document.body.scrollHeight"))
    
    while index < 90:
        
        images = browser.find_elements(By.CLASS_NAME, "loaded")
        
        updatedScroll = int((scrollHeight * index) / 100)    
        
        scroll_down(updatedScroll)
        
        for image in images:
            
            if len(image_urls) <= max_images:
            
                try:
                    image_urls.add(image.get_attribute('src'))                
                except:
                    continue
        index += 10
    
    download_images(image_urls, pagination)


def download_images(images, pagination):
    for i, item in enumerate(images):    

        image_name = files.get_random_hash()        
        try:
            image_content = requests.get(item).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)
            file_path = files.DOWNLOAD_PATH + str(image_name) + ".jpg"
            
            with open(file_path, "wb") as f:
                image.save(f, "JPEG")               
            print("Success")
            
        except Exception as e:
            print('FAILED - ', e)
              
    pagination += 1
    
    if pagination <= max_pagination:
        click_event("pagination__next")
        get_images(pagination)

    else:
        print("\nFinish")
        browser.quit()
