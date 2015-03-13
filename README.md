[![Build Status](https://travis-ci.org/betweenbrain/travis-ci-test.svg?branch=develop)](https://travis-ci.org/betweenbrain/travis-ci-test)

Simple POC for integrating a Python Selenium test, to be run at Sauce Labs, using Travis CS.

### Important links to note:
[Getting started - Sauce Labs](https://docs.saucelabs.com/ci-integrations/travis-ci/#adding-credentials-for-a-public-github-repo) provides a simple tool for creating encrypted authentication details for `.travis.yml`. For example as:
 
 ````
env:
  global:
    - secure: "Secure username token goes here!"
    - secure: "Secure access key token goes here!"
 
addons:
  sauce_connect: true
 ````
 
[Python Basic Setup - Sauce Labs](https://docs.saucelabs.com/tutorials/python/) provides a good, working example of setting up a browser in Python. 
 
 ````
from selenium import webdriver

sauce_url = "http://betweenbrain:e2007f7b-afd4-43a3-af7f-c5087c82199a@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
 'platform': "Mac OS X 10.9",
 'browserName': "chrome",
 'version': "31",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                       command_executor=sauce_url)
driver.implicitly_wait(10)
 ````

### Notes
* Lint your `.travis.yml` - installs as a Ruby Gem `$ sudo gem install travis-lint`

* For some reason, having three version of Python listed in `.travis.yml` caused `Response: {"error": "Too many active tunnels: 5; allowed: 5"}` . This might simply be a Travis bug with it not closing open tunnels in a timely manner. It now works with three versions listed again.