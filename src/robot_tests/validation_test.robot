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

*** Test Cases ***
Number Field Rejects Non-Numeric
    FOR    ${reference_type}    IN    @{REFERENCE_TYPES}
        Reset Database
        Go To    ${HOME_URL}/add?type=${reference_type}

        ${num_count}=    Get Element Count    xpath=//input[@type='number']

        IF    ${num_count} > 0
            Input Text    xpath=(//input[@type='number'])[1]    not-a-number
            Click Button    xpath=//button[@type='submit']
            Wait Until Page Contains    täytyy olla numero
        END
    END

Number Field Rejects Negative
    [Documentation]
    FOR    ${reference_type}    IN    @{REFERENCE_TYPES}
        Reset Database
        Go To    ${HOME_URL}/add?type=${reference_type}

        ${num_count}=    Get Element Count    xpath=//input[@type='number']
        IF    ${num_count} > 0
            Input Text    xpath=(//input[@type='number'])[1]    -5
            Click Button    xpath=//button[@type='submit']
            Wait Until Page Contains    Vuosi ei voi olla negatiivinen
        END
    END

Text Field Rejects Only Special Chars
    FOR    ${reference_type}    IN    @{REFERENCE_TYPES}
        Reset Database
        Go To    ${HOME_URL}/add?type=${reference_type}
        ${text_count}=    Get Element Count    xpath=//input[@type='text'] | //textarea
        IF    ${text_count} > 0
            Input Text    xpath=(//input[@type='text'] | //textarea)[1]    !!!@@@###
            Click Button    xpath=//button[@type='submit']
            Wait Until Page Contains    ei voi sisältää vain erikoismerkkejä
        END
    END

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