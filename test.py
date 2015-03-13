# Dependencies
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
sauce_url = "http://betweenbrain:e2007f7b-afd4-43a3-af7f-c5087c82199a@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(10)
# End Saucelabs

# Navigate to http://espn.go.com/
driver.get("http://espn.go.com/")

# Find the NFL > Scores link
inputElement = driver.find_element_by_name("&lpos=sitenavdefault&lid=sitenav_nfl")

# Click the found link
inputElement.click()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("NFL"))

    # Verify the page title
    assert driver.title == 'NFL Football Teams, Scores, Stats, News, Standings, Rumors - National Football League - ESPN'

finally:
    driver.quit()
