import time

from components.components import WebElement
from conftest import browser
from conftest import add_rows
from pages.web_tables import WebTables


def test_tables(browser):
    webtables_page = WebTables(browser)

    webtables_page.visit()
    assert not webtables_page.no_data.exist()

    while webtables_page.btn_delete_rows.exist():
        webtables_page.btn_delete_rows.click()
    print(f"Кнопка удаления существует: {webtables_page.btn_delete_rows.exist()}")

    time.sleep(2)
    assert webtables_page.no_data.exist()


def test_add(browser):
    tables = WebTables(browser)

    tables.visit()
    tables.btn_add.click()
    assert tables.reg_form.exist()
    tables.btn_submit.click()
    time.sleep(2)
    assert "was-validated" in tables.user_form.get_dom_attribute("class"), \
        "Атрибут class формы не содержит 'was-validated'"

    name = 'A'
    last_name = 'B'
    mail = 'ad@as.com'
    age = 31
    salary = 42
    department = 'Gak'

    tables.first_name.send_keys(name)
    tables.last_name.send_keys(last_name)
    tables.email.send_keys(mail)
    tables.age.send_keys(age)
    tables.salary.send_keys(salary)
    tables.department.send_keys(department)
    tables.btn_submit.click()
    time.sleep(2)
    assert not tables.reg_form.exist()

    rows = tables.row.find_elements()
    added_row_found = False

    for row in rows:
        if (name in row.text and last_name in row.text and mail in row.text
                and str(salary) in row.text and str(age) in row.text and department in row.text):
            added_row_found = True
            break

    assert added_row_found, "Добавленная запись не найдена в таблице"

    for row in rows:
        if mail in row.text:
            tables.edit.locator = f"[id^='edit-record-{rows.index(row) + 1}']"
            tables.edit.click()
            time.sleep(2)
    assert tables.reg_form.exist()

    new_name = 'Abc'
    tables.first_name.clear()
    tables.first_name.send_keys(new_name)
    tables.btn_submit.click()
    time.sleep(2)

    for row in rows:
        if new_name in row.text:
            text_is_changed = True
            assert text_is_changed, "Not changed"
            tables.btn_delete_rows.locator = f"[id^='delete-record-{rows.index(row) + 1}']"
            tables.btn_delete_rows.locator_type = 'css'
            assert tables.btn_delete_rows.find_element()
            tables.btn_delete_rows.click()
            time.sleep(2)

    for row in tables.row.find_elements():
        assert mail not in row.text, "Запись не удалена"


def test_pagination(browser, add_rows):
    page = WebTables(browser)

    assert page.next.get_dom_attribute('disabled')
    assert page.previous.get_dom_attribute('disabled')

    fields = [page.first_name, page.last_name, page.email, page.age, page.salary, page.department]
    params_1 = ["Kris", "Tina", "asteria@mail.com", 21, 400000, "mail"]
    params_2 = ["Abby", "Stone", "cracali@mail.com", 74, 40450, "staff"]
    params_3 = ["GH", "UHB", "lmanai@mail.com", 7, 450, "f"]

    assert page.btn_add.find_element()
    page.btn_add.force_click()
    time.sleep(2)
    assert page.reg_form.visible()
    assert page.reg_form.exist()
    WebElement.fill_form(fields, params_1)
    page.btn_submit.click()
    time.sleep(2)

    assert page.btn_add.find_element()
    page.btn_add.force_click()
    time.sleep(2)
    assert page.reg_form.visible()
    assert page.reg_form.exist()
    WebElement.fill_form(fields, params_2)
    page.btn_submit.click()
    time.sleep(2)

    assert page.btn_add.find_element()
    page.btn_add.force_click()
    time.sleep(2)
    assert page.reg_form.visible()
    assert page.reg_form.exist()
    WebElement.fill_form(fields, params_3)
    page.btn_submit.click()
    time.sleep(2)

    assert page.total_pages.get_text() == "2"
    assert not page.next.get_dom_attribute('disabled')

    page.next.click()
    time.sleep(2)
    assert page.page_number.get_dom_attribute('value') == '2'

    page.previous.click()
    time.sleep(2)
    assert page.page_number.get_dom_attribute('value') == '1'
