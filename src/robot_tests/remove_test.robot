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
    
    Wait Until Page Contains Element    xpath=//wa-details    timeout=5s
    ${details_element}=    Get WebElement    xpath=//wa-details
    Scroll Element Into View    ${details_element}
    Click Element    ${details_element}

    Wait Until Page Contains Element    xpath=//wa-button[contains(text(),"Poista")]    timeout=5s
    Execute Javascript    document.evaluate("//wa-button[contains(text(),'Poista')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    
    Wait Until Page Contains Element    xpath=//wa-button[@type="submit" and contains(text(),"Kyllä, poista")]    timeout=5s
    Execute Javascript    document.evaluate("//wa-button[@type='submit' and contains(text(),'Kyllä, poista')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    
    Location Should Be    ${HOME_URL}/

    Page Should Not Contain    Test Text