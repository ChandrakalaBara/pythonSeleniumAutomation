from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")

driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.141.0\IEDriverServer.exe")

driver.maximize_window()

driver.get("https://www.hotstar.com/")

print(driver.current_url) # Returns the URL of the page

print(driver.title)    # Title of the page

print(driver.page_source)  # HTML code for the page



driver.close()    # Close the browser