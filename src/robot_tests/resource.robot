*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${DELAY}     0.1 seconds
${HOME_URL}  http://localhost:5001
${RESET_URL}  http://localhost:5001/reset_db
${BROWSER}   chrome
@{REFERENCE_TYPES}    BOOK    ARTICLE    THESIS  
${TEST_VALUE}    Test Value
${HEADLESS}   true
&{FIELD_VALUES}
...    text=Test Text
...    number=123
...    textarea=Test Textarea

*** Keywords ***
Open And Configure Browser
    IF  $HEADLESS == "true"
        ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
        Call Method    ${options}    add_argument    --headless
        Open Browser    ${HOME_URL}    ${BROWSER}   options=${options}
    ELSE
        Open Browser   ${HOME_URL}    ${BROWSER}
    END
    Set Selenium Speed  ${DELAY}
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
    
    Wait Until Element Is Visible    xpath=//button[@type="submit" and @value="lisää"]    timeout=5s
    
    Scroll Element Into View    xpath=//button[@type="submit" and @value="lisää"]
    Select From List By Value    xpath=//select[@name="tag"]    kandityö

    Click Button    xpath=//button[@type="submit" and @value="lisää"]
    Page Should Contain    Test Text

Edit Reference
    [Arguments]    ${reference_type}
    Add Reference    ${reference_type}

    Go To   ${HOME_URL}
    Click Link    xpath=(//a[contains(@href, "/edit/")])[1]

    ${inputs}=    Get WebElements    xpath=//input[@type="text"] | //input[@type="number"]
    FOR    ${field}    IN    @{inputs}
        ${type}=    Get Element Attribute    ${field}    type
        Input Text    ${field}    ${FIELD_VALUES}[${type}]
    END

    ${areas}=    Get WebElements    xpath=//textarea
    FOR    ${field}    IN    @{areas}
        Input Text    ${field}    ${FIELD_VALUES}[textarea]
    END
    
    Select From List By Value    xpath=//select[@name="tag"]    gradu
    Page Should Contain    Test Text

Add Tag Reference
    [Arguments]    ${reference_type}    ${tag}
    Go To    ${HOME_URL}/add?type=${reference_type}
    ${elements}=    Get WebElements    xpath=//input[@type="text"] | //input[@type="number"] | //textarea
    FOR    ${field}    IN    @{elements}
        ${type}=    Get Element Attribute    ${field}    type
        Input Text    ${field}    ${FIELD_VALUES["${type}"]}
    END
    
    Select From List By Value    xpath=//select[@name='tag']    ${tag}
    
    Wait Until Element Is Visible    xpath=//button[@type="submit" and @value="lisää"]    timeout=5s
    
    Scroll Element Into View    xpath=//button[@type="submit" and @value="lisää"]

    Click Button    xpath=//button[@type="submit" and @value="lisää"]

Clear Contents From Table Reference
    Reset Database

Go To Home Page
    Go To    ${HOME_URL}

Search With Tag
    [Arguments]    ${tag}
    Select From List By Value    xpath=//select[@name='tag']    ${tag}
    Click Button    xpath=//button[text()='Hae']
