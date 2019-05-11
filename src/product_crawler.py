#
# product_crawler.py
# Created by Ghost on 11/05/2019.
#

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
        '11번가': "http://deal.11st.co.kr/browsing/DealAction.tmall?method=getCategory&dispCtgrNo=1019281"
    }
    return switcher.get(market_name, "Invalid market name")

def get_element_list(market_name) :
    switcher = {
        '티몬': driver.find_elements_by_class_name("info"),
        '11번가' : driver.find_elements_by_class_name("prd_info")
    }
    return switcher.get(market_name, "Invalid market name")

def get_product_name(market_name, element) :
    switcher = {
        '티몬': element.find_element_by_class_name('title_name').text,
        '11번가' : element.find_element_by_xpath(".//span[@class='fs_16']").text
    }
    return switcher.get(market_name, "Invalid market name")

def get_price(market_name, element) :
    switcher = {
        '티몬': element.find_element_by_xpath(".//div[@class='price_area']/span[@class='price']").text.split('\n')[-1].replace('~',''),
        '11번가' : element.find_element_by_xpath(".//strong[@class='sale_price']").text
    }
    return switcher.get(market_name, "Invalid market name")

def find_e_coupon(market_name) :
    target_list = get_target_list(market_name)
    url = get_url(market_name)
    result_list = []

    driver.get(url)
    for element in get_element_list(market_name) :
        product_name = get_product_name(market_name, element)
        price = get_price(market_name, element)
        
        for target in target_list :
            if target in product_name :
                result = market_name + ' ' + product_name + ' ' + price
                print ('Found ' + result)
                result_list.append(result)
                break
    return result_list

def find_11st_e_coupon() :
    target_list = ['컬쳐랜드', '해피머니', '도서문화', '북앤라이프', '국민관광', '갤러리아', '롯데', '현대', '신세계', '갤러리아', '홈플러스', '이마트', '펀라이프']
    url_11st_e_coupon = "http://deal.11st.co.kr/browsing/DealAction.tmall?method=getCategory&dispCtgrNo=1019281"

    result_list = []

    driver.get(url_11st_e_coupon)
    for element in driver.find_elements_by_class_name("prd_info") :
        product_name = element.find_element_by_xpath(".//span[@class='fs_16']").text
        price = element.find_element_by_xpath(".//strong[@class='sale_price']").text
        
        for target in target_list :
            if target in product_name :
                result = '11번가 ' + product_name + ' ' + price
                print ('Found ' + result)
                result_list.append(result)
                break

    return result_list

def find_gmarket_e_coupon() :
    target_list = ['컬쳐랜드', '해피머니', '도서문화', '북앤라이프', '국민관광', '갤러리아', '롯데', '현대', '신세계', '갤러리아', '홈플러스', '이마트', '펀라이프']
    url_gmarket_e_coupon = "http://corners.gmarket.co.kr/BestSellers?viewType=C&largeCategoryCode=100000048"

    result_list = []
    
    driver.get(url_gmarket_e_coupon)
    for element in driver.find_elements_by_xpath("//div[@class='best-list']/ul/li") :
        product_name = element.find_element_by_xpath(".//a[@class='itemname']").text
        price = element.find_element_by_xpath(".//div[@class='s-price']").text
        
        for target in target_list :
            if target in product_name :
                result = 'g마켓 ' + product_name + ' ' + price
                print ('Found ' + result)
                result_list.append(result)
                break

    return result_list

driver = webdriver.Chrome('../bin/chromedriver')
driver.implicitly_wait(3)

#print (find_lotteGiftCard())
#print (find_timon_e_coupon())
#print (find_11st_e_coupon())
#print (find_gmarket_e_coupon())
#print (find_auction_e_coupon())
print (find_e_coupon('11번가'))


driver.close()

'''
ssl._create_default_https_context = ssl._create_unverified_context

url_lotte_card = "https://www.lottecard.co.kr/app/LPCDAJD_V100.lc"
html = urlopen(url_lotte_card)
bsObject = BeautifulSoup(html, "html.parser")


print(bsObject) # 웹 문서 전체가 출력됩니다
'''
