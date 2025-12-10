*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Add Article With Tag
    Reset Database
    Add Reference With Tag    article    kandityö
    Page Should Contain    Test Text
    Click Element    xpath=//wa-details
    Page Should Contain    Kandidaatintutkielma

Add Book With Tag
    Reset Database  
    Add Reference With Tag    book    gradu
    Page Should Contain    Test Text
    Click Element    xpath=//wa-details
    Page Should Contain    Pro gradu -tutkielma

*** Keywords ***
Add Reference With Tag
    [Arguments]    ${reference_type}    ${tag_value}
    Go To    ${HOME_URL}/add?type=${reference_type}

    Click Element    xpath=//wa-details
 
    Type Text Into All WebAwesome Inputs    wa-input[type="text"]:not([name="doi"])    ${FIELD_VALUES["text"]}
    Type Text Into All WebAwesome Inputs    wa-input[type="number"]:not([name="doi"])    ${FIELD_VALUES["number"]}
    Type Text Into All WebAwesome Inputs    wa-textarea:not([name="doi"])    ${FIELD_VALUES["textarea"]}

    Click Element    xpath=//wa-select[@name="tag"]
    Click Element    xpath=//wa-option[@value="${tag_value}"]

    Click Element    xpath=//wa-button[@type="submit" and @value="tallenna"]
    Location Should Be    ${HOME_URL}/