*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${HOME_URL}    http://localhost:5001
${RESET_URL}   http://localhost:5001/reset_db
${BROWSER}     chrome
${DELAY}       0.1 seconds
@{REFERENCE_TYPES}    BOOK    ARTICLE    THESIS
${TEST_VALUE}    Test Value
${HEADLESS}   false
&{FIELD_VALUES}
...    text=Test Text
...    number=123
...    textarea=Test Textarea

${TEST_TITLE}     Test Reference
${TEST_AUTHOR}    Test Author

*** Test Cases ***
Search Returns Added Reference (All fields)
    Reset Database
    Go To    ${HOME_URL}

    Input Text    name=query    ${TEST_TITLE}
    Click Button  xpath=//button[normalize-space(.)="Hae"]

    Wait Until Page Contains    Hakutulokset
    Wait Until Page Contains    ${TEST_TITLE}

Search Returns Existing Test Reference (Title field)
    Reset Database
    Go To    ${HOME_URL}

    Input Text    name=query    ${TEST_TITLE}
    Select From List By Value    id=field    title
    Click Button  xpath=//button[normalize-space(.)="Hae"]

    Wait Until Page Contains    Hakutulokset
    Wait Until Page Contains    ${TEST_TITLE}
    Wait Until Page Contains    Kentässä:

Search Returns No Results When Not Found
    Reset Database
    Go To    ${HOME_URL}/?query=__this_should_not_exist_12345__

    Page Should Not Contain    ${FIELD_VALUES["text"]}

*** Keywords ***
Open And Configure Browser
    IF    '${HEADLESS}' == 'true'
        ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
        Call Method    ${options}    add_argument    --headless
        Open Browser    ${HOME_URL}    ${BROWSER}    options=${options}
    ELSE
        Open Browser    ${HOME_URL}    ${BROWSER}
    END
    Set Selenium Speed    ${DELAY}
    Maximize Browser Window

Close Browser
    Close All Browsers

Reset Database
    Go To    ${RESET_URL}

Valid Input Adds Reference
    [Arguments]    ${reference_type}
    Go To    ${HOME_URL}/add?type=${reference_type}

    ${elements}=    Get WebElements    xpath=//input[@type="text"] | //input[@type="number"] | //textarea
    FOR    ${field}    IN    @{elements}
        ${type}=    Get Element Attribute    ${field}    type
        Input Text    ${field}    ${FIELD_VALUES["${type}"]}
    END

    Click Button    xpath=//button[@type="submit"]

    Page Should Contain    Test Text