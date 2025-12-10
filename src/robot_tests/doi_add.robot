*** Settings ***
Resource         resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database


*** Test Cases ***

Add DOI Reference Test
    Go To    ${HOME_URL}/add?type=article
    
    Type Text Into WebAwesome Input    wa-input[name="doi"]    10.1177/1475921708089823

    Click Element    xpath=//wa-button[@value="doi"]

    ${title_value}=    Get Value    name=title
    Should Not Be Empty    ${title_value}
