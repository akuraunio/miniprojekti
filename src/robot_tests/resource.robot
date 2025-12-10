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
        Evaluate    $options.add_argument('--headless')
        Evaluate    $options.add_argument('--start-maximized')
        Open Browser    ${HOME_URL}    ${BROWSER}   options=${options}
    ELSE
        Open Browser   ${HOME_URL}    ${BROWSER}
        Maximize Browser Window
    END
    Set Selenium Speed  ${DELAY}

Close Browser
    Close All Browsers

Reset Database
    Go To    ${RESET_URL}

Add Reference
    [Arguments]    ${reference_type}
    Go To    ${HOME_URL}/add?type=${reference_type}
    
    Click Element    xpath=//wa-details
    
    Type Text Into All WebAwesome Inputs    wa-input[type="text"]:not([name="doi"])    ${FIELD_VALUES["text"]}
    Type Text Into All WebAwesome Inputs    wa-input[type="number"]:not([name="doi"])    ${FIELD_VALUES["number"]}
    Type Text Into All WebAwesome Inputs    wa-textarea:not([name="doi"])    ${FIELD_VALUES["textarea"]}

    Click Element    xpath=//wa-button[@type="submit" and @value="tallenna"]

    Location Should Be    ${HOME_URL}/
    Page Should Contain    Test Text

Edit Reference
    [Arguments]    ${reference_type}
    Add Reference    ${reference_type}

    Click Element    xpath=//wa-details

    Click Element    xpath=//wa-button[contains(text(),"Muokkaa")]

    Type Text Into All WebAwesome Inputs    wa-input[type="text"]:not([name="doi"])    Edited
    Type Text Into All WebAwesome Inputs    wa-input[type="number"]:not([name="doi"])    456
    Type Text Into All WebAwesome Inputs    wa-textarea:not([name="doi"])    Edited

    Click Element    xpath=//wa-select[@name="tag"]
    Click Element    xpath=//wa-option[@value="gradu"]

    Click Element    xpath=//wa-button[@type="submit" and @value="tallenna"]
    
    Location Should Be    ${HOME_URL}/
    Page Should Contain    Edited

    Click Element    xpath=//wa-details
    Page Should Contain    Pro gradu -tutkielma

Clear Contents From Table Reference
    Reset Database

Go To Home Page
    Go To    ${HOME_URL}

Search With Tag
    [Arguments]    ${tag}
    Select From List By Value    xpath=//select[@name='tag']    ${tag}
    Click Button    xpath=//button[text()='Hae']

Type Text Into All WebAwesome Inputs
    [Arguments]    ${selector}    ${text}
    
    Execute Javascript    const elements = document.querySelectorAll('${selector}'); elements.forEach(elem => { const shadow = elem.shadowRoot; const inner = shadow.querySelector("input, textarea"); inner.value = '${text}'; inner.dispatchEvent(new Event('input', { bubbles: true })); });

Type Text Into WebAwesome Input
    [Arguments]    ${selector}    ${text}

    Execute Javascript    const elem = document.querySelector('${selector}'); const shadow = elem.shadowRoot; const inner = shadow.querySelector("input, textarea"); inner.value = '${text}'; inner.dispatchEvent(new Event('input', { bubbles: true }));