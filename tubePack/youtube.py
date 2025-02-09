import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def tubeStart(driver) :
    # Navigate to YouTube
    driver.get("https://www.youtube.com/")


def tubeSearch(search_query, driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_box.clear()

    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )

def tubePlay(driver,num):
    time.sleep(2)

    try:
        videos = driver.find_elements(By.ID, "video-title")
        if len(videos) >= num:
            player_video = videos[num - 1]  # Adjusted for zero-based indexing
            player_video.click()  # Play the video
        else:
            print(f"Less than {num} videos found in the search results.")
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(5)  # Give enough time for the video to start