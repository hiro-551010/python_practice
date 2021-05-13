import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chromeを起動する関数


def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
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
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)

# main処理


def main():
    search_keyword = "高収入"
    # driverを起動
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://google.com')
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    
    wait = WebDriverWait(driver, 10)
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
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()

    """ 課題2-1
    name_list = driver.find_element_by_class_name("cassetteRecruit__name")
    exp_name_list.append(name_list.text)
    print(name_list.text)
    """
    
    path = './task2.csv'
    file = pd.read_csv(path)
    exp_name_list = list(file['company'])
    next_page_link = []

    while True:
        name_list = driver.find_elements_by_class_name("cassetteRecruit__name")
        for name in name_list:
            try:
                for name in name_list:
                    exp_name_list.append(name.text)
            except:
                Chrome.close

        next_page = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"iconFont--arrowLeft")))
        next_page_link.append(next_page)
        if len(next_page_link) >= 1:
            next_page_url = next_page_link[0].get_attribute("href")
            driver.get(next_page_url)
        else:
            print('終わりました')
            break


    df = pd.DataFrame(data=exp_name_list, columns=['company'])
    df.to_csv(path, mode='w', encoding='utf-8')


    # --- 課題2-2 ---
    print(df.head(3))

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
