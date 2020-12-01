from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import os
import sys

def get_participants(id, driver):
    participants_element = driver.find_element_by_xpath('//*[@id="meeting_list"]/tbody/tr[' + str(id) + ']/td[12]')
    participants_element.click()
    time.sleep(1)
    try:
        export_meeting_data_element = driver.find_element_by_xpath('//*[@id="withMeetingHeader"]')
        export_meeting_data_element.click()
    except ElementNotInteractableException:
        print('Error: Could not add meeting data to file.')
    time.sleep(.25)
    try:
        export_data_button = driver.find_element_by_xpath('//*[@id="btnExportParticipants"]')
        export_data_button.click()
    except ElementNotInteractableException:
        print("Error: Failed to download report data.")
    try:
        unique_users_element = driver.find_element_by_xpath('//*[@id="selectUniqueDiv"]')
        unique_users_element.click()
    except ElementNotInteractableException:
        print('Error: Could not select unique users.')
    try:
        close_element = driver.find_element_by_xpath('//*[@id="attendees_dialog"]/div/div/div[1]/button')
        close_element.click()
    except ElementNotInteractableException:
        print("Error: Failed to close report box.")
    time.sleep(1)

def pull_reports():
    options = Options()
    options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"
    options.add_argument("user-data-dir=/Users/benwoodman/Library/Application Support/Google/Chrome Beta/Default")
    driver = webdriver.Chrome(options=options, executable_path="/Users/benwoodman/Downloads/chromedriver", )
    driver.get("https://unc.zoom.us/account/my/report?from=11/01/2020&to=11/22/2020")

    input("<enter> when logged in")

    for x in range(200):
        for id in range(200):
            try:
                get_participants(id + 1, driver)
            except NoSuchElementException:
                print("Finished page!")
                response = input("Click next page or select new dates and then <enter> to continue. Type 'exit' to exit.")
                if (response == "exit"):
                    exit
                break

def merge_reports(dir):
    out = ""
    reports = os.listdir(dir)
    for f in reports:
        with open(dir + '/' + f) as infile:
            info = ""
            for i, line in enumerate(infile, 0):
                if (i == 1):
                    info = line[0:(len(line) - 1)]
                elif not(i == 0 or i == 2 or i == 3):
                    out += info + line

    # print(*out, sys.stdout)
    # print(out, file = sys.stdout)
    sys.stdout.write(out)