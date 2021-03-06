import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logging import getLogger
# Chromeを起動する関数
def set_driver(headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）の設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与


    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(ChromeDriverManager().install(), options=options)

# tableタグの中のthタグが引数のtargetと一致した場合に、tdのテキストを返す関数
def find_table_target_word(th_elems, td_elems, target: str):
    for th_elem, td_elem in zip(th_elems, td_elems):
        if th_elem.text == target:
            return td_elem.text

# main処理
def main():
    search_keyword = "高収入"
    # driverを起動
    driver = set_driver(False)
    driver.get('https://google.com')
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # -------

    wait = WebDriverWait(driver, 10)
    # -------
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(1)
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(1)
    except:
        pass
    
    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()

    try:
        driver.execute_script('document.querySelector(".karte-close").click()')
        time.sleep(1)
    except:
        pass

    """ 課題2-1
    name_list = driver.find_element_by_class_name("cassetteRecruit__name")
    exp_name_list.append(name_list.text)
    print(exp_name_list.text)
    """
    
    path = './task2.csv'
    file = pd.read_csv(path)
    exp_name_list = []
    exp_table_list = []
    exp_job_list = []
    exp_money_list = []

    while True:
        name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
        table_list = driver.find_elements_by_class_name('tableCondition')
        for (name, table) in zip(name_list, table_list):
            exp_name_list.append(name.text)
            exp_table_list.append(table.text)
            job_list = find_table_target_word(
                table.find_elements_by_tag_name("th"),
                table.find_elements_by_tag_name("td"),
                '仕事内容'
                )        
            money_list = find_table_target_word(
                table.find_elements_by_tag_name("th"),
                table.find_elements_by_tag_name("td"),
                '初年度年収'
                )
            exp_job_list.append(job_list)
            exp_money_list.append(money_list)

        next_page = driver.find_element_by_class_name('iconFont--arrowLeft')
        time.sleep(5)
        driver.get(next_page.get_attribute("href"))
        print(len(exp_name_list))

        # --- 課題2-5 ---
        df = pd.DataFrame({
            '企業名': exp_name_list,
            '仕事内容': exp_job_list,
            '初年度年収': exp_money_list,
        })
        df.to_csv(path, mode='w', encoding='utf-8')


        # --- 課題2-2 ---
        print(df.head(3))

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()


