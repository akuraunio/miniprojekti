*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Reference App Should Load
    Go To  http://localhost:5000
    Title Should Be  Viitteet
    Page Should Contain  Viitteet
    Page Should Contain  Lisää viite