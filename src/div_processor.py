from selenium.webdriver.common.by import By


def get_category_list(driver):
    category_id = '//a[@ng-bind="::category.name"]'
    category_list = driver.find_elements(By.XPATH, category_id)
    return [element.text for element in category_list]

def get_winners_list(driver):
    winner_id = 'winner'
    winner_list = driver.find_elements(By.CLASS_NAME, winner_id)
    return [element.text for element in winner_list]
