*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
ARTICLE Tag Test
    Clear Contents From Table Reference
    Add Tag Reference  article  kandityö
    Go To Home Page  
    Search With Tag  kandityö
    Page Should Contain  Test Text

BOOK Tag Test
    Clear Contents From Table Reference
    Add Tag Reference  book  kandityö
    Go To Home Page  
    Search With Tag  kandityö
    Page Should Contain  Test Text

BOOKLET Tag Test
    Clear Contents From Table Reference
    Add Tag Reference  booklet  kandityö
    Go To Home Page  
    Search With Tag  kandityö
    Page Should Contain  Test Text
