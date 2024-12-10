*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To References Page

*** Test Cases ***
Set Correct Information For Article Reference
    Go To Add Reference Page
    Select Dropdown By Value    article
    Check Form Is Loaded
    Set Reference Id  15
    Set Author  Nancy Jackson
    Set Title  How To Learn
    Set Journal  The Psychologist
    Set Year  2014
    Set Number  1
    Set Pages  97-101
    Set DOI  jackson:2014
    Submit Information
    Adding Reference Should Succeed

Search Shows Correct Results
    Go To References Page
    References Page Should Be Open
    Set Keyword  learn
    Set Window Size    1920    1080
    Click Button  search
    References Page Should Be Open
    Page Should Contain  Nancy Jackson

Keyword That Does Not Appear In Any Reference Should Not Give Results
    Set Keyword  rainbow
    Set Window Size    1920    1080
    Click Button  search
    References Page Should Be Open
    Page Should Not Contain  Nancy Jackson

***Keywords***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    journal

Set Keyword
    [Arguments]  ${query}
    Input Text  query  ${query}