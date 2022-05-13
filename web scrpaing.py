from selenium import webdriver
url="https://www.youtube.com/watch?v=lNLmk7CPtOw"
browser = webdriver.Edge()
browser.get(url)
browser.find_element(by=By.XPATH, value='//*[@id="base-js"]').click()
