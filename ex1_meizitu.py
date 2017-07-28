import requests
from bs4 import BeautifulSoup
import os

head = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = "http://www.mzitu.com/all"
response = requests.get(all_url, headers=head)
soup = BeautifulSoup(response.text, 'lxml')
li_list = soup.find('div', class_='all').find_all('a')
for li in li_list:
    text = li.get_text()
    folder_name = str(text).strip().replace('?', "")
    os.makedirs(os.path.join("D:\meizitu", folder_name))
    os.chdir("D:\meizitu\\" + folder_name)
    href = li['href']
    img_response = requests.get(href, headers=head)
    img_soup = BeautifulSoup(img_response.text, 'lxml')
    max_imgNUm = img_soup.find(
        'div', class_='pagenavi').find_all('span')[-2].get_text()
    for imgNum in range(1, int(max_imgNUm) + 1):
        href_img = href + "/" + str(imgNum)
        imgNum_response = requests.get(href_img, headers=head)
        imgNum_soup = BeautifulSoup(img_response.text, 'lxml')
        img_url = imgNum_soup.find(
            'div', class_='main-image').find('img')['src']
        real_img = requests.get(img_url, headers=head)
        img_name = img_url[-9:-4]
        f = open(img_name + 'jpg', 'ab')
        f.write(real_img.content)
        f.close()
