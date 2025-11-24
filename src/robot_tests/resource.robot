*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${DELAY}     0.5 seconds
${HOME_URL}  http://localhost:5001
${RESET_URL}  http://localhost:5001/reset_db
${BROWSER}   chrome
@{REFERENCE_TYPES}    BOOK    ARTICLE    THESIS  
${TEST_VALUE}    Test Value
&{FIELD_VALUES}
...    text=Test Text
...    number=123
...    textarea=Test Textarea

*** Keywords ***
Open And Configure Browser
    Set Selenium Speed  ${DELAY}
    Open Browser  browser=${BROWSER}
    Maximize Browser Window

Close Browser
    Close All Browsers

Reset Database
    Go To    ${RESET_URL}

Add Reference
    [Arguments]    ${reference_type}
    Go To    ${HOME_URL}/add?type=${reference_type}

    ${elements}=    Get WebElements    xpath=//input[@type="text"] | //input[@type="number"] | //textarea
    FOR    ${field}    IN    @{elements}
        ${type}=    Get Element Attribute    ${field}    type
        Input Text    ${field}    ${FIELD_VALUES["${type}"]}
    END

    Click Button    xpath=//button[@type="submit"]

    Page Should Contain    Test Text

