from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc


options = Options()
options.headless = False
options.add_argument("--incognito")
browser = uc.Chrome(options=options)

# navigate to Google
browser.get('https://www.google.com/')

# find the search box element and enter a search query
search_box = browser.find_element(By.NAME, 'q')
search_box.send_keys('Что можно поискать в гугле?')
search_box.send_keys(Keys.RETURN)

# wait for the search results to load
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'search')))
#try closing the cookie window
try:
    cookie_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]')))
    cookie_button.click()
except:
    pass

#All Results
all_results = ""

for page in range(1, 4):
    #get the results
    search_results = browser.find_elements(By.CSS_SELECTOR, 'div.g')

    #format and print
    tmp_page_number_text = "Номер страницы: {}\n".format(page)
    all_results = all_results + tmp_page_number_text
    print(tmp_page_number_text)

    for result in search_results:
        title = result.find_element(By.TAG_NAME, 'h3')
        url = result.find_element(By.TAG_NAME, 'a')
        tmp_result = str(f'{title.text} - {url.get_attribute("href")}')
        print(tmp_result)
        all_results = all_results + tmp_result + "\n"
    print("\n")
    all_results = all_results + "\n"
    next_button = browser.find_element(By.CSS_SELECTOR, 'a#pnnext')
    next_button.click()

print("_________________________")
with open("Results.txt", "w") as f:
    # Write the string to the file
    f.write(all_results)
input()