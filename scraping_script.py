from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import numpy as np

# connecting to the browser

print("Connecting to the browser")
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome("/Users/AJEKWE/Downloads/chromedriver_win32/chromedriver.exe")
# defining the url

print("defining the url and entering the url")
url = "https://www.vivino.com/US/en/"
driver.get(url)

print("Successfully entered the URL")

# we will have to navigate to the homepage and then click on the wines link to go to the wines pages before scraping
page = driver.find_element(By.CLASS_NAME, 'menuLink_text__nDfIV').click()

print("after clicking the menu button")



# after navigating into the wines page, we then wait for 15 seconds before scraping
time.sleep(10)
print("Wait for 10 seconds")

# this is where i want to deselect all the types of wines
print("Unclicking the unecessary buttons")
buttons = driver.find_elements(By.CLASS_NAME, 'filterByWineType__pill--DDMJ3')
print(buttons)

# <label class="pill__pill--2AMAs pill__selected--3KX2r filterByWineType__pill--DDMJ3"><input type="checkbox" data-testid="wineTypes_7" value="7"><div class="pill__inner--2uty5"><span class="pill__text--24qI1">Dessert</span></div></label>
# buttons= driver.find_elements_by_xpath('')
time.sleep(5)

not_click = buttons[0]
for button in buttons[:4]:
    if button != not_click:
        button.click()
        time.sleep(3)

# not_click.click()
# time.sleep(3)

print("Clicking the all ratings button")        
# clicking on the all rating radio button to collect all ratings 
driver.find_elements(By.CLASS_NAME, '_2K-I_')[-1].click() 
time.sleep(3)

print("Wait for 3 seconds")

# I want increase the price range for the wine
print("increase the price slider and wait for 3 seconds")
slider = driver.find_element(By.CLASS_NAME, 'rc-slider-handle-2')
ActionChains(driver).move_to_element(slider).perform()
ActionChains(driver).drag_and_drop_by_offset(slider, 200, 0).perform()
ActionChains(driver).release().perform()
# result = driver.find_elements(By.CLASS_NAME, 'wineCard__wineCard--2dj2T')
time.sleep(3)


times=0
while(times < 20) :
    print(f"Scrolling the page {(times + 1)} time(s)")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(8)
    times += 1


result = driver.find_elements(By.CLASS_NAME, 'wineCard__wineCard--2dj2T')
time.sleep(5)
print(f"{len(result)} Red found!")

result_list = []
for item in result:

    try:
        Winery = item.find_element(By.CLASS_NAME, 'wineInfoVintage__truncate--3QAtw').text
    except:
        Winery = np.nan
    try:
        name = item.find_element(By.CLASS_NAME, 'wineInfoVintage__vintage--VvWlU').text
        
    except:
        name = np.nan
        vintage =np.nan
    try:
        location = item.find_element(By.CLASS_NAME, 'wineInfoLocation__wineInfoLocation--BmkcO').text
        Region=location.split(',')[:-1]
        Region=' '.join(Region)
        
        Country = location.split(',')[-1]
    except: 
        Region= np.nan
        Country=np.nan
    try:
        rating = item.find_element(By.CLASS_NAME, 'vivinoRating_averageValue__uDdPM').text
    except:
        rating = np.nan
    try:
        nbr_ratings = item.find_element(By.CLASS_NAME, 'vivinoRating_caption__xL84P').text
        nbr_rating = nbr_ratings.split(' ')[0]
    except:
        nbr_rating = np.nan
    try:
        price = item.find_element(By.CLASS_NAME, 'addToCartButton__price--qJdh4 div:nth-child(2)').text
    except:
        price = item.find_element(By.CLASS_NAME, 'addToCart__ppcPrice--ydrd5').text
        
    temp_dict = {"Winery":Winery, "Name":name, "Region":Region, "Country":Country, "Rating":rating, "Number of Ratings":nbr_rating,"Wine Type":"Red", "Price":price}
    result_list.append(temp_dict)
    print(f"Wine No. {len(result_list)} collected")
    
# convert it to a pandas dataframe so it can be saved to a csv file
df = pd.DataFrame(result_list)
df.to_csv('vivino_wines_dataset_red.csv', index = False)

print("Done Collecting.......You can rest now! COngratulations")

driver.close()