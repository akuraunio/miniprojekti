***Settings***
Library  SeleniumLibrary

***Variables***
${SERVER}  localhost:5000
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

***Keywords***
Open And Configure Browser
    ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --incognito

    IF  $HEADLESS == 'true'
        Call Method  ${options}  add_argument  --headless
    END
    Open Browser  ${HOME_URL}  ${BROWSER}  options=${options}
    Set Selenium Speed  ${DELAY}

Reset References
    Go To  ${HOME_URL}