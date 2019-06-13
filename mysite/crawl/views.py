from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from selenium import webdriver

def crawl() :
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("crawl/chromedriver", chrome_options=options)
    driver.get("https://naver.com")
    driver.find_element_by_xpath('//*[@id="query"]').send_keys("화장품")
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()
    titles = driver.find_elements_by_css_selector("a.lnk_tit")

    res = []

    for title in titles:
        res.append({"text" : title.text, "link" : title.get_property("href")})

    return res

def index(request):
    titles = crawl()
    context = {'titles': titles}
    return render(request, 'crawl/index.html', context)
