import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


name = ""
#Сокрытие браузера при парсинге
# chrome_options = Options()
# chrome_options.add_argument('--headless')

# Установка веб-драйвера (например, для Chrome)
driver = webdriver.Chrome()

# Зайти на страницу аутентификации
#driver.get('https://fs.utmn.ru/adfs/ls?SAMLRequest=lZJPb9swDMXv%2BxSG7rEc%2F1kDIXYRpChQoAOKNN1hl4GVmNaAJXkineXjT3Ya1Id16K4U%2BR7fj1pfn2yXHDFQ610tlmkmEnTam9a91OJpf7tYievmy5rAdr3aDPzqdvhrQOJkQ4SB49jWOxoshkcMx1bj0%2B6%2BFq%2FMPSkpIU6k1hscKPXhRWpvrXdjVSQ3UaV1wJPzZeBA6cDWpWGQYA4kOxLJrQ8aJ%2B9aHKAjFMndTS1%2BYvFcmqqAoipwiWB0WVW5KYuyyp6z7KqMbfQARO0R3weJBrxzxOC4FnmWF4vlcpGt9tmVqlYq%2B5oWq%2FKHSL5fkOQjkgjJkZog1GIITnmglpQDi6RYq8fNt3sVO1UfPHvtO9G8IZv8wucF4EJVNB8xHFVyaZHBAIOkXo7EFtHarOXc9bxD3qu3k6GZIMZ7MZ442XrbQ2hpTIkn0DzPmf9fUDVX3nYxxQ4PM7lPh%2F5nm1Z6lI7l8ay%2FfTAPcQ3UMdk%2BgKPeBz4j%2BOs%2BzfntIyDNhd78mzd%2FAA%3D%3D&RelayState=8fd7c8c4-6880-4455-80be-0a15250ddb22&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=2FOBG5CU3kvJl0C3pVYvgG1TzWKB7Y7inwa%2FoukluC6qjGz5GeocUs4arb3GEJnN3j9OdCVdG3tr17VkRGauS%2BDsmyrZOsX78GLZR0SuXVJH7JKhrJnk78gJgyAf2LY%2FwrRBCc6dPiIOLnTLVAteiG7toVmkc2vHgWhzv9a4I7v47Oo7gY37%2BJ%2Bred0ZENX9Y1etiq6HT81s3tJBQfb%2BWphonnxFutQhItLk%2B2juRO7FJ6Ot%2FKEd%2F8MO6ZCPlIOXCXMUVci99lPNonwZ5dHGHhKBG%2BdqnVNprtTKuyN42BhoIVo7YwbmU%2BEVnzRsoH9LyAVgxuhubhGqU5f2m9Eh1A%3D%3D')
driver.get('https://utmn.modeus.org/schedule-calendar/my?timeZone=%22Asia%2FTyumen%22&calendar=%7B%22view%22:%22agendaWeek%22,%22date%22:%222023-11-07T18:43:41%22%7D&selectedEvent=%22%22')
# Заполнить форму аутентификации (замените на свои данные)
username_input = driver.find_element('name', 'UserName')
password_input = driver.find_element('name', 'Password')

username_input.send_keys('')
password_input.send_keys('')


# Нажать на кнопку "Войти"
enter_button = driver.find_element('id', 'submitButton')
enter_button.click()

time.sleep(5)
#Клик по кнопке фильтров
filter_button = driver.find_element('class', 'btn-filter')
filter_button.click()

#Клик по кнопке выбора участника
participant_button = driver.find_element_by_css_selector('.ng-tns-c56-10.ui-multiselect.ui-widget.ui-state-default.ui-corner-all')
participant_button.click()

name_input = driver.find_element_by_css_selector('.ui-inputtext.ui-widget.ui-state-default.ui-corner-all.search-field.ng-valid.ng-touched.ng-dirty')
name_input.send_keys(name)
time.sleep(5)
schedule_page = driver.page_source

# Завершить сеанс Selenium
driver.quit()



# Теперь в переменной schedule_page содержится весь HTML-код страницы после авторизации
soup = BeautifulSoup(schedule_page, 'html.parser')

# Создайте и записать HTML-код в текстовый файл
with open('web_page.html', 'w', encoding='utf-8') as file:
    file.write(schedule_page)

