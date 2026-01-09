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


def test_tc_nav_001_main_menu_navigation(driver):
    """
    TC-NAV-001 — Проверка структуры главного меню и навигации по пунктам
    """

    wait = WebDriverWait(driver, 20)

    # 1. Открыть сайт
    driver.get("https://www.ppl.cz")

    # 2. Принять cookies
    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_button.click()
    except:
        pass

    # 3. Пункты меню
    menu_items = [
        ("O nás", "//a[@href='https://www.ppl.cz/o-nas']"),
        ("Vyhledat zásilku", "//a[@href='https://www.ppl.cz/vyhledat-zasilku']"),
        ("Chci poslat balík", "//a[@href='https://www.ppl.cz/poslat-zasilku']"),
        ("Kariéra", "//a[@href='https://ppl.jobs.cz/']"),
        ("Zákaznický servis", "//a[@href='https://www.ppl.cz/zakaznicky-servis']"),
    ]

    base_url = "https://www.ppl.cz/"

    # 4. Проверка количества пунктов меню
    assert len(menu_items) == 5, "Количество пунктов меню не соответствует требованиям"

    # 5. Проверка наличия и ТЕКСТА пунктов меню
    for name, xpath in menu_items:
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        assert element.is_displayed(), f"Пункт меню не отображается: {name}"
        assert element.text.strip() == name, (
            f"Текст пункта меню не совпадает. "
            f"Ожидалось: '{name}', получено: '{element.text.strip()}'"
        )

    # 6. Проверка переходов по каждому пункту меню
    for name, xpath in menu_items:

        menu_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        main_window = driver.current_window_handle
        existing_windows = driver.window_handles

        menu_link.click()

        # Отдельная логика для Kariéra (открывается в новой вкладке)
        if name == "Kariéra":
            wait.until(lambda d: len(d.window_handles) > len(existing_windows))

            new_window = [w for w in driver.window_handles if w != main_window][0]
            driver.switch_to.window(new_window)

            wait.until(lambda d: "jobs" in d.current_url.lower())
            assert "jobs" in driver.current_url.lower(), "Раздел 'Kariéra' не открылся"

            driver.close()
            driver.switch_to.window(main_window)

        # Все остальные пункты открываются в этой же вкладке
        else:
            wait.until(lambda d: d.current_url != base_url)

            assert driver.current_url != base_url, (
                f"После клика по '{name}' переход не произошёл"
            )

            # Проверка наличия КОНТЕНТА на открытой странице
            page_body = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            assert page_body.is_displayed(), (
                f"После перехода по '{name}' контент страницы не загрузился"
            )

            # Возврат на главную страницу
            driver.back()
            wait.until(EC.url_to_be(base_url))