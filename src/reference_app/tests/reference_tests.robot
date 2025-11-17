*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Reference App Should Load
    Go To  http://localhost:5000  timeout=10s
    Title Should Be  Viitteet  timeout=5s
    Page Should Contain  Viitteet  timeout=5s
    Page Should Contain  Lisää viite  timeout=5s