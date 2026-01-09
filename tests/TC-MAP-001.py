import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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


def test_tc_map_001_search_pickup_point_by_address(driver):
    """
    TC-MAP-001 — Поиск пункта выдачи по полному и частичному адресу
    """

    wait = WebDriverWait(driver, 20)

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

    # 2. Найти кнопку «Mapa výdejních míst» по href и проскроллить к ней
    map_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@href,'/mapa-vydejnich-mist')]")
        )
    )
    ActionChains(driver).move_to_element(map_button).perform()

    # 3. Нажать на кнопку «Mapa výdejních míst»
    map_button.click()

    # 4. Ввести ПОЛНЫЙ адрес
    address_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Hledejte')]")
        )
    )
    address_input.clear()
    address_input.send_keys("Budějovická 1126, Praha")

    # 5. Выбрать первый результат из автодополнения
    first_autocomplete_result = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(@class,'control-panel__search-results-item')])[1]")
        )
    )
    first_autocomplete_result.click()

    # 6. Клик по первому пункту в списке результатов слева
    first_pickup_point = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(@class,'result__link')])[1]")
        )
    )
    first_pickup_point.click()

    # 7. Проверка отображения карточки пункта
    pickup_card = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'detail')]")
        )
    )
    assert pickup_card.is_displayed(), "Карточка пункта выдачи не отображается"

    # 8. Вернуться на главную страницу
    driver.get("https://www.ppl.cz")

    # 9. Снова перейти в «Mapa výdejních míst»
    map_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href,'/mapa-vydejnich-mist')]")
        )
    )
    map_button.click()

    # 10. Ввести ЧАСТИЧНЫЙ адрес
    address_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Hledejte')]")
        )
    )
    address_input.clear()
    address_input.send_keys("Budějovická")

    # 11. Выбрать первый результат из автодополнения
    first_autocomplete_result = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(@class,'control-panel__search-results-item')])[1]")
        )
    )
    first_autocomplete_result.click()

    # 12. Финальная проверка — что появились пункты выдачи
    markers_after = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//button[contains(@class,'result__link')]")
        )
    )
    assert len(markers_after) > 0, "После частичного поиска пункты выдачи не отобразились"