*** Settings ***
Resource         resource.robot
Suite Setup    Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${TEST_TITLE}     Test Reference
${TEST_AUTHOR}    Test Author

*** Test Cases ***
