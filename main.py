from selenium import webdriver
from bs4 import BeautifulSoup as bs

target_url = ''  # Put Melon playlist's first page's URL here

for i in range(0, 10):
    driver = webdriver.Chrome()

    driver.get(target_url + str(i * 50 + 1))
    html = driver.page_source
    soup = bs(html, 'html.parser')
    
    for i in range(1, 51):
        title = soup.select(f'#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > div > div > a.fc_gray')
        singer = soup.select(f'#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > div > a:first-child')
        if len(singer) == 0: singer = soup.select(f'#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > div')
        print(title[0].text, '-', singer[0].text)

print('----------End----------')

