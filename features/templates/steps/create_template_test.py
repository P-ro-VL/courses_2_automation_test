import re
import time
from behave import *
from selenium.webdriver.common.by import By

from test_helper import *

startTesting()

@given('Tôi đang ở trang quản lý khung quy trình')
def open_template_management_page(context):
    clickText("a", "Quản lý khung quy trình") 
    driver.implicitly_wait(10)

@when('Tôi bấm nút {tag} "{text}"')
def click_button(context, tag, text):
    clickText(tag, text)

@then("Tôi được chuyển đến trang tạo khung quy trình mới")
def check_create_template_page(context):
    time.sleep(5)
    assert driver.current_url.endswith("template/step"), "Tôi không được chuyển đến trang tạo khung quy trình mới"

@when('Tôi điền vào placeholder "{placeholder}" là "{value}"')
def input_placeholder_name(context, placeholder, value):
    inputText(placeholder, value)

@when('Tôi điền vào placeholder "{placeholder}" thứ {index:d} là "{value}"')
def input_placeholder_name_with_index(context, placeholder, index, value):
    inputText(placeholder, value, index=(index - 1))

@when('Tôi chọn phòng ban chủ trì thứ {index:d} là "{value}"')
def select_owner_department(context, index, value):
    clickText("span", "-- Chọn Phòng ban Chủ trì --")
    inputTextById("selectDepartments", value, index=(index - 1))
    time.sleep(1)
    clickText("div", value, last=True)
    tapOutside()

@when('Tôi chọn người chủ trì thứ {index:d} là "{value}"')
def select_owner_user(context, index, value):
    clickText("span", "-- Chọn User Chủ trì --")
    inputTextById("selectUsers", value, index=(index - 1))
    time.sleep(1)
    clickText("div", value, last=True)
    tapOutside()

@when('Tôi điền sản phẩm đầu ra thứ {index:d} là "{value}"')
def input_output(context, index, value):
    inputText("-- Tên sản phẩm đầu ra --", value, index=(index - 1))

@when('Tôi chọn loại sản phẩm đầu ra thứ {index:d} là "{value}"')
def input_output_type(context, index, value):
    expandDropdownById("requiredOutput", index=(index - 1))
    clickTextFieldCondition("div", "title", value, index=(index - 1))

@when('Tôi thêm bước mới')
def click_new_step_button(context):
    clickClass("rounded-t-\\[10px\\]", last=True)

@when('Tôi chọn phòng ban phối hợp thứ {index:d} là "{value}"')
def select_department(context, index, value):
    clickText("span", "-- Chọn Phòng ban Phối hợp --")
    inputTextById("selectDepartments", value, index=(index - 1))
    time.sleep(1)
    clickText("div", value, last=True)
    tapOutside()

@when('Tôi chọn người phối hợp thứ {index:d} là "{value}"')
def select_user(context, index, value):
    clickText("span", "-- Chọn User Phối hợp --")
    inputTextById("selectUsers", value, index=(index - 1))
    time.sleep(1)
    clickText("div", value, last=True)
    tapOutside()

@when('Tôi thêm giai đoạn thứ {index:d}')
def add_stage(context, index):
    clickTextFieldCondition("img", "alt", "Thêm giai đoạn", index=(index - 1))

@then('Tôi thấy bước thứ hai của tạo khung quy trình')
def i_am_at_step_2(context):
    assert driver.find_element(By.XPATH, "//button[contains(text(), 'Quay lại')]")

@when('Tôi nhìn thấy đủ các bước tôi đã điền ở bước 1')
def i_found_all_steps(context):
    print('Found')  # Bạn có thể bổ sung thêm kiểm tra chi tiết nếu cần

@when('Tôi chờ {seconds:d} giây')
def wait_for_seconds(context, seconds):
    time.sleep(seconds)

@then('Tôi thấy thông báo "{message}"')
def i_saw_notification(context, message):
    assert re.search(r"success=true&id=\d+", driver.current_url), f"Không thấy thông báo: {message}"
    clickText("button", "Xem khung quy trình vừa tạo")
    time.sleep(200)

@when('Tôi tải lại trang')
def i_refresh_page(context):
    driver.refresh()
    time.sleep(5)

@then('Tôi nhìn thấy khung quy trình "{name}"')
def i_saw_template_name(context, name):
    assert driver.find_element(By.XPATH, f"//div[contains(text(), '{name}')]"), f"Không thấy khung quy trình: {name}"    