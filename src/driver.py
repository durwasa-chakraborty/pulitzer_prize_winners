from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from url_caller import call_url
from div_processor import get_category_list, get_winners_list
from core_logic import execute_core_logic
from util import write_dict_to_csv_with_data_dir_creation
import time

URL="https://www.pulitzer.org/prize-winners-by-year/2023"

def main():
    driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
    driver = call_url(driver, URL)
    time.sleep(5) # required to wait for page load

    # get category list

    categories = get_category_list(driver)
    winners = get_winners_list(driver)

    map_of_csv = execute_core_logic(categories, winners)

    driver.quit()

    path = write_dict_to_csv_with_data_dir_creation(URL, map_of_csv)
    return path

if __name__ == '__main__':
    main()
