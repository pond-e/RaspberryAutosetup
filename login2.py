from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome('C:\\Users\\harut\\RaspberryAutosetup/geckodriver.exe')
type(browser)

#Webサイト1 ユーザー名・パスワード入力欄はtextBoxでid有り
browser.get('web-auth.akashi.ac.jp')
usr_name_el = browser.find_element_by_id('//*[@id="loginform"]/tbody/tr[1]/td[2]/input')
usr_name_el.send_keys('e1904')
usr_pass_el = browser.find_element_by_id('//*[@id="loginform"]/tbody/tr[2]/td[2]/input')
usr_pass_el.send_keys('akashi6814')
usr_pass_el.submit()
#ログイン後、あるボタンを押してトップページ遷移させたいサイトのため下記コード。
# ログインボタンをクリックします。
login_btn = browser.find_element_by_xpath('//*[@id="loginform"]/tbody/tr[3]/td/input[2]')
login_btn.click()

'''
#Webサイト2
#ユーザー名入力欄はtextBoxでid有り、パスワードはidとclassが無いのでxpathで検索
browser.execute_script( 'window.open()' )　#新規タブ開く
browser.switch_to.window(browser.window_handles[-1])　#新規タブに移動
browser.get('Webサイト2')
usr_name_el = browser.find_element_by_id('対象のID')
usr_name_el.send_keys('ユーザー名')
usr_pass_el = browser.find_element_by_xpath('対象のパス。開発者ツールからコピーするのが楽')
usr_pass_el.send_keys('パスワード')
usr_pass_el.submit()
'''
