*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***

Set Correct Information For Inproceedings Reference
    Select Dropdown By Value  book
    Check Form Is Loaded
    Set Reference Id  foh225
    Set Author  Robert Jordan
    Set Title  Fires of Heaven
    Set Year  2002
    Set Publisher  Tor Books
    Submit Information
    Adding Reference Should Succeed

Delete Reference Just Added
    Go To References Page
    Click Button  foh225
    References Page Should Be Open
    Page Should Not Contain  Fires of Heaven

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    publisher
