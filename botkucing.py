from selenium import webdriver

driver = webdriver.Edge("lib\edgedriver_win32\msedgedriver.exe")
driver.get("https://popcat.click/")

while True:
    driver.execute_script('const app=document.querySelector("#app").__vue__;function click(){app.accumulator=800,app.bot=!1,app.sequential_max_pops=0,pop()}function pop(){for(var e=0;e<=800;e++)setTimeout(()=>{d
