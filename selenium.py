from selenium import webdriver

# Konfigurasi untuk membuka website dengan Google Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--start-maximized')
#chrome_options.add_argument('--incognito')

# Membuka website dengan Google Chrome
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://endpoin.javascriptmining.yanganda.hostsendiri/indexxx.html')

# Menjaga browser terbuka
input('Tekan Enter untuk menutup browser...')

# Menutup browser
driver.quit()
