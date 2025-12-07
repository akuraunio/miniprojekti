*** Settings ***
Resource         resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database


*** Test Cases ***

Add DOI Reference Test
    Go To    ${HOME_URL}/add?type=article
    Input Text    name=doi    10.1177/1475921708089823
    Click Button    xpath=//button[@value="doi"]

    ${title_value}=    Get Value    name=title
    Should Not Be Empty    ${title_value}
    
    Input Text    name=key    123
    
    Click Button    xpath=//button[@type="submit" and @value="lisää"]
    
    Page Should Contain    ${title_value}
    

