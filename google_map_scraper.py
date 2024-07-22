from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import json
import pandas as pd
import os

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

g_map_link = input("Enter the link you want to scrape from: ")

try: 
    driver.get(g_map_link)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form:nth-child(2)"))).click()
    except Exception:
        pass

    scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
    driver.execute_script("""
        var scrollableDiv = arguments[0];
        function scrollWithinElement(scrollableDiv) {
            return new Promise((resolve, reject) => {
                var totalHeight = 0;
                var distance = 1000;
                var scrollDelay = 3000;
                
                var timer = setInterval(() => {
                    var scrollHeightBefore = scrollableDiv.scrollHeight;
                    scrollableDiv.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeightBefore) {
                        totalHeight = 0;
                        setTimeout(() => {
                            var scrollHeightAfter = scrollableDiv.scrollHeight;
                            if (scrollHeightAfter > scrollHeightBefore) {
                                return;
                            } else {
                                clearInterval(timer);
                                resolve();
                            }
                        }, scrollDelay);
                    }
                }, 200);
            });
        }
        return scrollWithinElement(scrollableDiv);
    """, scrollable_div)

    items = driver.find_elements(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction]')

    results = []
    for item in items:
        data = {}

        try:
            data['title'] = item.find_element(By.CSS_SELECTOR, ".fontHeadlineSmall").text
        except Exception:
            data['title'] = None

        try:
            data['link'] = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        except Exception:
            data['link'] = None

        try:
            data['website'] = item.find_element(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction] div > a').get_attribute('href')
        except Exception:
            data['website'] = None
        
        try:
            rating_text = item.find_element(By.CSS_SELECTOR, '.fontBodyMedium > span[role="img"]').get_attribute('aria-label')
            rating_numbers = [float(piece.replace(",", ".")) for piece in rating_text.split(" ") if piece.replace(",", ".").replace(".", "", 1).isdigit()]

            if rating_numbers:
                data['stars'] = rating_numbers[0]
                data['reviews'] = int(rating_numbers[1]) if len(rating_numbers) > 1 else 0
            else:
                data['stars'] = None
                data['reviews'] = None
        except Exception:
            data['stars'] = None
            data['reviews'] = None

        try:
            text_content = item.text
            phone_pattern = r'((\+?\d{1,2}[ -]?)?(\(?\d{3}\)?[ -]?\d{3,4}[ -]?\d{4}|\(?\d{2,3}\)?[ -]?\d{2,3}[ -]?\d{2,3}[ -]?\d{2,3}))'
            matches = re.findall(phone_pattern, text_content)

            phone_numbers = [match[0] for match in matches]
            unique_phone_numbers = list(set(phone_numbers))

            data['phone'] = unique_phone_numbers[0] if unique_phone_numbers else None   
        except Exception:
            data['phone'] = None

        if data.get('title'):
            results.append(data)

finally:
    time.sleep(60)
    driver.quit()


print("Select the file format to save the data:")
print("1. JSON")
print("2. CSV")
print("3. Excel")
file_format = input("Enter the number of the file format you want: ").strip()

if file_format == '1':
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
elif file_format == '2':
    df = pd.DataFrame(results)
    df.to_csv('results.csv', index=False)
elif file_format == '3':
    df = pd.DataFrame(results)
    df.to_excel('results.xlsx', index=False)
else:
    print("Invalid selection. No file will be saved.")
