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
    Go To    ${HOME_URL}
    Click Link    xpath=//a[text()="Poista"]
    Page Should Contain    Haluatko varmasti poistaa tämän viitteen?
    Click Button    xpath=//input[@type="submit" and @value="Poista"]
    Page Should Not Contain    Test Text