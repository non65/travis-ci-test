# Dependencies
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to http://espn.go.com/
driver.get("http://espn.go.com/")

# Find the NFL > Scores link
inputElement = driver.find_element_by_name("&lpos=sitenavdefault&lid=sitenav_nfl")

# Click the found link
inputElement.click()

# Print the page title:
print driver.title

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("NFL"))

    # Verify the page title
    assert driver.title == 'NFL Football Teams, Scores, Stats, News, Standings, Rumors - National Football League - ESPN'

finally:
    driver.quit()
