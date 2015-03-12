# Dependencies
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver
username = os.environ["betweenbrain"]
access_key = os.environ["e2007f7b-afd4-43a3-af7f-c5087c82199a"]
capabilities["tunnel-identifier"] = os.environ["TRAVIS_JOB_NUMBER"]
hub_url = "%s:%s@localhost:4445" % (username, access_key)
driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://%s/wd/hub" % hub_url)

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
