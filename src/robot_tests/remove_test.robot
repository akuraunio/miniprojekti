*** Settings ***
Resource         resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database


*** Test Cases ***
Delete Reference Test
    Remove Reference


*** Keywords ***
Remove Reference
    Add Reference    article
    Page Should Contain    Test Text

    Go To    ${HOME_URL}

    Click Element    xpath=//wa-details

    Click Element    xpath=//wa-button[contains(text(),"Poista")]

    Click Element    xpath=//wa-button[@type="submit" and contains(text(),"Kyllä, poista")]
    
    Location Should Be    ${HOME_URL}/

    Page Should Not Contain    Test Text