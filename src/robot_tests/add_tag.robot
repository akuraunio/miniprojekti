*** Settings ***
Resource         resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Template    Add Tag
Test Setup       Reset Database

*** Test Cases ***
ARTICLE Tag Test      article
BOOK Tag Test         book
BOOKLET Tag Test      booklet


