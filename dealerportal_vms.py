##---------- DEALER PORTAL - VMS FE INTEGRATION----------##
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://stg-portal.cnh.com/DPLogin/")
time.sleep(5)
driver.maximize_window()
time.sleep(3)
first_tab_handle = driver.current_window_handle
time.sleep(5)
login = "userID"
password = "password"
element = driver.find_element(By.ID,"userID")
element.send_keys('nar130')
element = driver.find_element(By.ID,"password")
element.send_keys('Forward21')
time.sleep(4)
element = driver.find_element(By.ID,"btn-submit").click()
time.sleep(3)
element = driver.find_element(By.ID,"CybotCookiebotDialogBodyButtonAccept").click()
time.sleep(5)
def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

root1 = driver.find_element(By.TAG_NAME,'nova-nav-bar')
shadow_root1 = expand_shadow_element(root1)
work = shadow_root1.find_element(By.CSS_SELECTOR,"div > nav > div.nova-c-nav-bar--center > ul > li:nth-child(2)")
work.click()
time.sleep(5)
element1 = driver.execute_script("window.scrollTo(0,document.body.scrollHeight / 4)")
time.sleep(5)

root2 = driver.find_element(By.TAG_NAME,'nova-taxonomy-filter')
shadow_root2 = expand_shadow_element(root2)
work1 = shadow_root2.find_element(By.CSS_SELECTOR,"div > div:nth-child(1) > div.nova-c-taxonomy-filter__results > div > div:nth-child(4) > nova-lazy-component > nova-small-card > nova-card > div > div.nova-small-card__text-container.nova-js-card__content.sc-nova-small-card > a > h4")
work1.click() 
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
element = driver.execute_script("window.scrollTo(0,document.body.scrollHeight / 3)")
time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR,"body > vms-root > div > mat-sidenav-container > mat-sidenav-content > vms-home > main > nav > ul > li:nth-child(2) > vms-home-nav-button").click()
time.sleep(7)
driver.get("https://euevoawam010.azurewebsites.net/setupprofile")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-setup-profile/div/div/fieldset/div[2]/form/div/div[1]/div/mat-form-field/div/div[1]/div[3]/input").send_keys("120103T")
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-setup-profile/div/div/fieldset/div[2]/form/div/div[1]/div/mat-form-field/div/div[1]/div[4]/button/span[1]/mat-icon").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-setup-profile/div/div/fieldset/div[2]/form/div/div[7]/div[2]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[5]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-setup-profile/div/div/fieldset/div[2]/form/div/button").click()
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-home/main/nav/ul/li[2]/vms-home-nav-button/div").click()
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/mat-toolbar/vms-search/form/mat-form-field[1]/div/div[1]/div/mat-select/div/div[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/mat-toolbar/vms-search/form/mat-form-field[2]/div/div[1]/div[2]/input").send_keys("JJABCH11223556777")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/mat-toolbar/vms-search/form/mat-form-field[2]/div/div[1]/div[1]/button/span[1]/mat-icon").click()
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/div/vms-vehicle-list/div/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span[1]/div/div[2]/div/div/span").click()
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/div/vms-vehicle-list/div/mat-accordion/mat-expansion-panel/div/div/vms-device-list/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span/div/div[1]/div[3]/button/span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/vms-device-activate/mat-dialog-content/mat-dialog-actions/button[2]/span[1]").click()
time.sleep(20)
driver.find_element(By.XPATH,"//*[@id='mat-dialog-0']/vms-device-activate/mat-dialog-content/mat-dialog-actions/button").click()
time.sleep(300)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/div/vms-vehicle-list/div/mat-accordion/mat-expansion-panel/div/div/vms-device-list/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span/div/div[2]/div/mat-icon").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/vms-root/div/mat-sidenav-container/mat-sidenav-content/vms-company-details/div/vms-vehicle-list/div/mat-accordion/mat-expansion-panel/div/div/vms-device-list/mat-accordion/mat-expansion-panel/div/div/vms-product-bundle/mat-tree/mat-tree-node[1]/span/div/div[1]/div[4]/vms-purchase-button/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/vms-product-activate/mat-dialog-content/vms-product-purchase-confirm/div/footer/button[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/vms-product-activate/mat-dialog-content/vms-product-purchase-success/div/mat-dialog-actions/button/span[1]").click()
time.sleep(60)
driver.refresh()
