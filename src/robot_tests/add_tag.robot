*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Add Article With Tag
    Reset Database
    Add Reference With Tag    article    kandityö
    Page Should Contain    Test Text

Add Book With Tag
    Reset Database  
    Add Reference With Tag    book    gradu
    Page Should Contain    Test Text

*** Keywords ***
Add Reference With Tag
    [Arguments]    ${reference_type}    ${tag_value}
    Go To    ${HOME_URL}/add?type=${reference_type}
 
    ${elements}=    Get WebElements    xpath=//input[@type="text"] | //input[@type="number"] | //textarea
    FOR    ${field}    IN    @{elements}
        ${type}=    Get Element Attribute    ${field}    type  
        ${name}=    Get Element Attribute    ${field}    name
        IF    "${name}" != "doi"
            Input Text    ${field}    ${FIELD_VALUES["${type}"]}
        END
    END

    Select From List By Value    name=tag    ${tag_value}

    Click Button    xpath=//button[@type="submit" and @value="lisää"]
