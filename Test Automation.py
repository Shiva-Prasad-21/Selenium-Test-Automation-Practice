from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifiations")

driver=webdriver.Chrome(ops)
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://testautomationpractice.blogspot.com/")

# Name Feild
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Shiva Prasad")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("shivashankara9724@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[id='phone']").send_keys("9390444361")

# Radio Buttons
# driver.find_element(By.XPATH,"//label[@for='male']").click()
driver.find_element(By.XPATH,"//label[@for='female']").click()

# Drop Downs
collection=driver.find_element(By.XPATH,"//select[@id='country']")
one_option=Select(collection)
one_option.select_by_visible_text("India")

Data=driver.find_elements(By.XPATH,"//select[@id='country']")
for i in Data:
    print(i.text)

week=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(week))
for i in week:
    i.click()

collection2=Select(driver.find_element(By.XPATH,"//select[@class='form-control' and @id='colors']"))
collection2.select_by_visible_text("Red")

collection3=Select(driver.find_element(By.XPATH,"//select[@class='form-control' and @id='animals']"))
collection3.select_by_visible_text("Dog")
collection3.select_by_visible_text("Lion")

# Date
date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
date.click()
date.send_keys("24/03/2004")

driver.find_element(By.XPATH,"//input[@id='txtDate']").click()

month=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
month.select_by_visible_text("Mar")

year=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
year.select_by_visible_text("2016")

date_picker=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
select_date="24"

for i in date_picker:
    if i==select_date:
        i.click()
        break

# Alerts
driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()

driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
alert2=driver.switch_to.alert
print(alert2.text)
alert2.accept()
# alert2.dismiss()

alert_window=driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
alert3=driver.switch_to.alert
alert3.send_keys("Shiva Prasad")
print(alert3.text)
alert3.accept()

website_all_links=driver.find_elements(By.XPATH,"//a")
print(f"The Total Links Available in Website:{len(website_all_links)} ")

# Window handles 
# driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
# window_id=driver.window_handles
# parent_window=window_id[0]
# child_window=window_id[1]

# driver.switch_to.window(child_window)
# print(driver.title)
# driver.switch_to.window(parent_window)
# print(driver.title)

# driver.find_element(By.XPATH,"//button[@id='PopUp']").click()
# driver.switch_to.default_content()

# Action Chains 
act=ActionChains(driver)

button=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
mobile_link=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
laptop_link=driver.find_element(By.XPATH,"//a[normalize-space()='Laptops']")
act.move_to_element(button).move_to_element(mobile_link).move_to_element(laptop_link).click().perform()


feild1=driver.find_element(By.XPATH,"//input[@id='field1']")
feild1.clear()
feild1.send_keys("Shiva Prasad")
copy_button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act.double_click(copy_button).perform()

Drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
act.drag_and_drop(Drag,drop).perform()


# one_links=driver.find_element(By.XPATH,"//a[@class='link']")

# act.key_down(Keys.CONTROL).click(one_links).key_up(Keys.CONTROL).perform()
# driver.switch_to.window(driver.window_handles[2])
# print(driver.title)

parent = driver.current_window_handle

all_links = driver.find_elements(By.XPATH, "//a[@class='link']")
total_links = len(all_links)

for i in range(total_links):
    # Re-fetch elements every time
    links = driver.find_elements(By.XPATH, "//a[@class='link']")
    links[i].click()
    print(driver.title)
    driver.back()
    driver.switch_to.window(parent)

# Output of the For Loop
# Apple
# Lenovo Official Site | Laptops, Desktop PCs, Tablets, Monitors | Lenovo India
# Computers, Monitors & Technology Solutions | Dell India
# 401 - Unauthorized: Access is denied due to invalid credentials.
# 403 - Forbidden: Access is denied.
# 404 - File or directory not found.
# 500 - Internal server error.
# 502 - Web server received an invalid response while acting as a gateway or proxy server.

for link in links:
    act.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

time.sleep(3)

for tab in driver.window_handles:
    driver.switch_to.window(tab)
    print(driver.title)
# Output
# Automation Testing Practice
# Computers, Monitors & Technology Solutions | Dell India

# 404 - File or directory not found.

# 502 - Web server received an invalid response while acting as a gateway or proxy server.
# Apple
# 500 - Internal server error.
# 401 - Unauthorized: Access is denied due to invalid credentials.
# Lenovo Official Site | Laptops, Desktop PCs, Tablets, Monitors | Lenovo India

# 403 - Forbidden: Access is denied.

driver.switch_to.window(parent)
print(driver.title)

input=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
input.send_keys("Python")
input.submit()

res=driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']")


for i in res:
    i.click()
windowID=driver.window_handles
for handle in windowID:
     driver.switch_to.window(handle)
     print(driver.title)

time.sleep(5)
driver.quit()
