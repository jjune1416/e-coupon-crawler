#
# product_crawler.py
# Created by Ghost on 11/05/2019.
#

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
'''

def find_lotteGiftCard() :
    #try :
    url_lotte_card = "https://www.lottecard.co.kr/app/LPCDAJD_V100.lc"
    driver.get(url_lotte_card)
    
    try :
        driver.find_element_by_partial_link_text('기프트').click()
    except NoSuchElementException :
        print ('Not found 롯데 기프트 카드')
        return []

    print ('Found 롯데 기프트 카드')
    return ['롯데 기프트 카드']

def get_target_list(market_name) :
    target_list = ['컬쳐랜드', '해피머니', '도서문화', '북앤라이프', '국민관광', '갤러리아', '롯데', '현대', '신세계', '갤러리아', '홈플러스', '이마트', '펀라이프']
    return target_list

def get_url(market_name) :
    switcher = {
        '티몬': "http://www.tmon.co.kr/deallist/68090000",
        '11번가': "http://deal.11st.co.kr/browsing/DealAction.tmall?method=getCategory&dispCtgrNo=1019281",
        'G마켓': "http://corners.gmarket.co.kr/BestSellers?viewType=C&largeCategoryCode=100000048",
        '옥션' : "http://corners.auction.co.kr/corner/CategoryBest.aspx?category=86050000",
        'G9' : "http://www.g9.co.kr/Display/Category/400000082/500000366"
    }
    return switcher.get(market_name, "Invalid market name")

def get_element_list(market_name) :
    if market_name == '티몬' :
        return driver.find_elements_by_class_name("info")
    elif market_name == '11번가' :
        return driver.find_elements_by_class_name("prd_info")
    elif market_name == 'G마켓' :
        return driver.find_elements_by_xpath("//div[@class='best-list']/ul/li")
    elif market_name == '옥션' :
        return driver.find_elements_by_xpath("//li/div/div[@class='info']")
    elif market_name == 'G9' :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return driver.find_elements_by_xpath("//div/ul/li/div[@class='itemcard ']")
    
    print ("Invalid market name")
    return None

def get_product_name(market_name, element) :
    if market_name == '티몬' :
        return element.find_element_by_class_name('title_name').text
    elif market_name == '11번가' :
        return element.find_element_by_xpath(".//span[@class='fs_16']").text
    elif market_name == 'G마켓' :
        return element.find_element_by_xpath(".//a[@class='itemname']").text
    elif market_name == '옥션' :
        return element.find_element_by_xpath(".//em/a").text
    elif market_name == 'G9' :
        return element.find_element_by_xpath(".//span[@class='itemcard__info__title ellipsis']").text
    
    print ("Invalid market name")
    return None

def get_price(market_name, element) :
    if market_name == '티몬' :
        return element.find_element_by_xpath(".//div[@class='price_area']/span[@class='price']").text.split('\n')[-1].replace('~','')
    elif market_name == '11번가' :
        return element.find_element_by_xpath(".//strong[@class='sale_price']").text
    elif market_name == 'G마켓' :
        return element.find_element_by_xpath(".//div[@class='s-price']").text
    elif market_name == '옥션' :
        return element.find_element_by_xpath(".//span[@class='sale']").text
    elif market_name == 'G9' :
        return element.find_element_by_xpath(".//span[@class='format-price']").text.split('\n')[0]+'원'
    
    print ("Invalid market name")
    return None

def find_e_coupon(market_name) :
    target_list = get_target_list(market_name)
    url = get_url(market_name)
    result_list = []
    driver.get(url)
    for element in get_element_list(market_name) :
        #print (element.text)
        product_name = get_product_name(market_name, element)
        price = get_price(market_name, element)
        #print (product_name)

        for target in target_list :
            if target in product_name :
                result = market_name + ' ' + product_name + ' ' + price
                print ('Found ' + result)
                result_list.append(result)
                break
    return result_list

driver = webdriver.Chrome('../bin/chromedriver')
driver.implicitly_wait(3)

#print (find_lotteGiftCard())
print (find_e_coupon('G9'))


driver.close()

'''
ssl._create_default_https_context = ssl._create_unverified_context

url_lotte_card = "https://www.lottecard.co.kr/app/LPCDAJD_V100.lc"
html = urlopen(url_lotte_card)
bsObject = BeautifulSoup(html, "html.parser")


print(bsObject) # 웹 문서 전체가 출력됩니다
'''
