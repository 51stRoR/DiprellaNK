## DiprellaNK

test project

### 1. usage:

pytest -v test/test_allure.py --alluredir=path/to/dir/for/reportfiles [browser] --input-data=path/to/input_data.csv

browser options:

--firefox 

--chrome

Depends on chosen browser will be used related webdriver from web_drivers package

in case of using Linux, you should make driver file exacutable:
chmod +x web_drivers/linux/geckodriver
chmod +x web_drivers/linux/chromedriver

### 2. input_data.csv structure:
[url of webapp to test],[correct user email],[correct user password],[incorrect email],[incorrect password]

### 3. generating allure report
..\utils\allure-2.7.0\bin\allure.bat serve path/to/dir/for/reportfiles
