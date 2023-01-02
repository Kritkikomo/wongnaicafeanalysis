from manage_csv import *
from data_scraping_func import*
from list_edit_func import*

## scrap general data from wongnai
'''
cafe_path = 'datascraping\wongnai'
file_cafe_link ='link_use_1-25_real'
save_path = 'datascraping\wongnai'
file_name = 'data_cafe'
cafe =read_text2dic(cafe_path,file_cafe_link)
cafe_name=list(cafe.keys())
cafe_url =list(cafe.values())
for i in range(401,467): ##ถึงร้านที่ 400 ให้ทำ 401 ต่อ มีทั้งหมด467ร้าน เอา 466 ร้าน เพราะข้อมูลไม่ครบ
    use_url= cafe_url[i]
    url = "https://www.wongnai.com{}".format(str(use_url))
    data=data_scraping(url)
    add_csv(save_path,file_name,data)
    print(i)
'''
#scrap latitude longitude from clicking
cafe_path = 'datascraping\wongnai'
file_cafe_link ='link_use_1-25_real'
save_path = 'datascraping\wongnai'
file_name = 'latitude_longitude'
cafe =read_text2dic(cafe_path,file_cafe_link)
cafe_name=list(cafe.keys())
cafe_url =list(cafe.values())
click_class="StyledButton-sc-1lpnvbj.dfUsxm.ml-8"
driver = selenium_opendriver()  
for i in range(401,467): ##ถึงร้านที่ 100 ให้ทำ 101 ต่อ มีทั้งหมด467ร้าน เอา 466 ร้าน เพราะข้อมูลไม่ครบ
    temp=[]
    use_url= cafe_url[i]
    url = "https://www.wongnai.com{}".format(str(use_url))
    selenium_connection_click(driver,url,click_class)
    link = driver.find_element_by_xpath('//*[@id="ignite-theme-root"]/div[5]/div/div/div/div[2]/div/div[1]/a').get_attribute('href')
    temp.append(str(i))
    temp.append(cafe_name[i])
    temp.append(link) 
    add_csv(save_path,file_name,temp)
    print(i)


