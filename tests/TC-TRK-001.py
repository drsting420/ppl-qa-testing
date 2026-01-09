import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_tc_trk_001_valid_tracking_number(driver):
    """
    TC-TRK-001 — Проверка ввода действительного номера посылки
    """

    wait = WebDriverWait(driver, 15)

    # 1. Открыть сайт https://www.ppl.cz
    driver.get("https://www.ppl.cz")

    # 1.1 Принять cookies
    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_button.click()
    except:
        pass

    # 2. Нажать на кнопку «Vyhledat zásilku» в главном блоке
    search_button_main = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/vyhledat-zasilku']")
        )
    )
    search_button_main.click()

    # 3. Найти поле ввода трек-номера
    tracking_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='shipmentId']"))
    )

    assert tracking_input.is_enabled()

    # 4. Ввести действительный (валидный) номер посылки
    valid_tracking_number = "46198704540"
    tracking_input.clear()
    tracking_input.send_keys(valid_tracking_number)

    # 5. Проверить, что ввод не вызвал ошибок до отправки формы
    error_elements = driver.find_elements(By.CLASS_NAME, "c-help-block")
    assert len(error_elements) == 0

    # 6. Нажать на кнопку «Vyhledat zásilku» на форме трекинга
    search_button_form = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and contains(@class,'btn-primary')]")
        )
    )
    search_button_form.click()

    # 7. Убедиться, что после отправки не появилось сообщений об ошибке
    error_after_submit = driver.find_elements(By.CLASS_NAME, "c-help-block")
    assert len(error_after_submit) == 0

    # 8. Проверить, что произошёл переход на страницу деталей
    tracking_status_title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Stav vaší zásilky')]")
        )
    )

    assert tracking_status_title.is_displayed(), "Заголовок со статусом посылки не отображается"
    assert valid_tracking_number in driver.page_source, (
        "Номер посылки не отображается на странице результатов"
    )