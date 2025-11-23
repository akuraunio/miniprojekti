*** Settings ***
Resource         resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Template    Add Reference
Test Setup       Reset Database


*** Test Cases ***
ARTICLE Test          article
#BOOK Test             BOOK
#BOOKLET Test          BOOKLET
#INBOOK Test           INBOOK
#INPROCEEDINGS Test    INPROCEEDINGS
#MANUAL Test           MANUAL
#MASTERSTHESIS Test    MASTERSTHESIS
#MISC Test             MISC
#PHDTHESIS Test        PHDTHESIS
#PROCEEDINGS Test      PROCEEDINGS
#TECHREPORT Test       TECHREPORT
#UNPUBLISHED Test      UNPUBLISHED


*** Keywords ***
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
    