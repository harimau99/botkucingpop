from selenium import webdriver
import time
def main():
    #driverPath = r"/Users/<yourpath^secondary/Documents/liker/chromedriver_mac"
    driver = webdriver.Chrome(executable_path="<your path>") # Chrome
    driver.get("https://popcat.click/")
    while True: 
        driver.find_element_by_xpath("//*[@id='app']").click()
main()
