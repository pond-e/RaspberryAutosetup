import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
os.chdir("c:\\your-execpath\\login_sample")
import logging
import logging.config
# ログ出力設定　※本件では詳細割愛
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
logging.debug("AUTO LOGIN START")
# 自動ログイン関数を宣言
#
#
def AutoLogin():
  # 起動するブラウザを宣言します
  browser = webdriver.Firefox(executable_path='/usr/lib/firefox')
  # ログイン対象のWebページURLを宣言します
  url = "web-auth.akashi.ac.jp"
  # 対象URLをブラウザで表示します。
  browser.get(url)
  # ログインIdとパスワードの入力領域を取得します。
  login_id = browser.find_element_by_xpath("//input[@id='user_login']")
  login_pw = browser.find_element_by_xpath("//input[@id='user_pass']")
  # ログインIDとパスワードを入力します。
  userid = "wp-users"
  userpw = "wp-pwxxxxxx"
  login_id.send_keys(userid)
  login_pw.send_keys(userpw)
  # ログインボタンをクリックします。
  login_btn = browser.find_element_by_xpath(".//input[@id='wp-submit']")
  login_btn.click()

# AutoLogin関数を実行します。
#
ret = AutoLogin()
