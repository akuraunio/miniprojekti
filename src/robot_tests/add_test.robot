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


    