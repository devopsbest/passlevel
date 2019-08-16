from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import re

import sys
import time


Max_Time_Out = 30
Time_Out = 10
Mini_Time_Out = 3
pass_score = "80"

load_btn_id = "btnLoad"
load_txt_id = "txtMemberId"
score_txt_id = "txtUnitScore"
score_btn_id = "btnUnitScore"
level_txt_id = "txtLevelTestScore"
level_btn_id = "btnLevelTestScore"
course_select_id = "dpCourseList"
level_select_id = "dpLevelList"
toke_id = "token"
course_type = "GE"
end_circle = 7


def get_url(driver,host):
    url = "https://{}.englishtown.com/services/api/school/_tools/SubmitScoreHelper.aspx".format(host)
    if host == "staging":
        driver.get("https://staging.englishtown.com/services/oboe2/Areas/ServiceTest/MemberSiteSetting.aspx")
        token = find_element(toke_id).text
        print(token)
        url = "https://staging.englishtown.com/services/api/school/_tools/SubmitScoreHelper.aspx?token={}".format(
            token)

    if host == "live":
        driver.get("https://e1.englishtown.com/services/oboe2/Areas/ServiceTest/MemberSiteSetting.aspx")
        token = find_element(toke_id).text
        print(token)
        url = "https://www.englishtown.com/services/api/school/_tools/SubmitScoreHelper.aspx?token={}".format(token)

    return url


def open_url(driver,host):
    url = get_url(driver,host)
    driver.set_page_load_timeout(Max_Time_Out)
    try:
        driver.get(url)
    except TimeoutError:
        print("cannot open the page for {} seconds".format(Max_Time_Out))
        driver.execute_script('window.stop()')


def find_element(driver,obj):
    WebDriverWait(driver, Time_Out).until(EC.visibility_of_element_located((By.ID, obj)))
    element = WebDriverWait(driver, Time_Out).until(lambda x: driver.find_element(By.ID, obj))
    return element


def type(driver,obj, value):
    find_element(driver,obj).clear()
    find_element(driver,obj).send_keys(value)


def clickat(driver,obj):
    WebDriverWait(driver, Time_Out).until(EC.element_to_be_clickable((By.ID, obj)))
    find_element(driver,obj).click()


def pass_6_units(driver,memberid):
    type(driver,load_txt_id, memberid)
    clickat(driver,load_btn_id)

    course = find_element(driver,course_select_id)
    get_start_course = Select(course)

    print(get_start_course.first_selected_option.text)

    level = find_element(driver,level_select_id)
    get_start_level = Select(level)

    print(get_start_level.first_selected_option.text)

    if "General English" in get_start_course.first_selected_option.text:
        course_type = "GE"
        end_circle = 7


    elif "Business English" in get_start_course.first_selected_option.text:
        course_type = "BE"
        end_circle = 4

    else:
        print("don't know the course type")

    print("current course is {}".format(course_type))

    units = find_element(driver,'dpUntiList')
    get_start_unit = Select(units)

    start_unit = re.search("\d", get_start_unit.first_selected_option.text).group()

    for i in range(int(start_unit), end_circle):
        type(driver,score_txt_id, pass_score)
        clickat(driver,score_btn_id)
        clickat(driver,load_btn_id)
        print("Save progress for unit {}".format(i))


def pass_level_test(driver):
    type(driver,level_txt_id, pass_score)
    clickat(driver,level_btn_id)
    print("pass unit test")


def pass_whole_progress(env,memberid):
    # env = "mobilefirst"
    # memberid = 23989807

    option = webdriver.ChromeOptions()

    option.add_argument('disable-infobars')
    # option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(Time_Out)

    open_url(driver,env)
    pass_6_units(driver,memberid)
    if course_type == "GE":
        pass_level_test(driver)

    driver.quit()


if __name__ == '__main__':
    pass_whole_progress("mobilefirst", 23989912)


# if __name__ == '__main__':
#     driver.implicitly_wait(Time_Out)
#     p = pass_six_units()
#     p.open_url()
#     p.pass_6_units()
#     if p.course_type == "GE":
#         p.pass_level_test()
#
#     driver.quit()
