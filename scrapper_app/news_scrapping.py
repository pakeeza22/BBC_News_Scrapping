from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv

def scrapping(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    list_of_hrefs = []
    new_section = driver.find_elements(By.CSS_SELECTOR, '#page > section.module.module--promo > div > ul > li')
    for elem in new_section:
        elements = elem.find_elements(By.TAG_NAME, "a")
        for el in elements:
            list_of_hrefs.append(el.get_attribute("href"))
    list_of_hrefs = list(set(list_of_hrefs))

    news = []
    news_details = {}
    for link in list_of_hrefs:
        driver.get(link.format())
        elements = ""
        try:
            heading = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#main-heading'))).text
            
            detail_news = driver.find_elements(By.CSS_SELECTOR, '.ssrcss-11r1m41-RichTextComponentWrapper')
            for elem in detail_news:
                elements += str(elem.text)  

            news_details["url"] = link
            news_details["title"] = heading
            news_details["description"] = elements
            news.append(news_details)
        except:
            pass
    
    return news

def send_to_csv(news):
    with open('news_scrapping_data.csv', 'w', encoding='UTF8') as f:
        fieldnames = ['title', 'url', 'description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for n in news:
            writer.writerow(n)

url = "https://www.bbc.com/"
news = scrapping(url)
send_to_csv(news)