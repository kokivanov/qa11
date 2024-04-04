import pytest
from selenium.webdriver.common.by import By
from .DynamicButtonsPages import SearchHelper
from .conftest import WebDriverSetup  # За умовою припускаємо імпорт


@pytest.mark.usefixtures("browser")
class TestsDynamicButtons:
    def test_dynamic_buttons(self):
        # Ініціалізація класу пошукового помічника з передачею веб-драйвера
        search_helper = SearchHelper(self.driver)

        # Перехід на сторінку з динамічними кнопками
        search_helper.go_to_site()

        # Виклик методів кліків по кнопкам та перевірка тексту
        search_helper.click_button_zero()
        search_helper.click_button_one()
        search_helper.click_button_two()
        search_helper.click_button_three()
        assert "All Buttons Clicked" in search_helper.verify_all_buttons_clicked_text(
        ), "Не всі кнопки були натиснуті"
