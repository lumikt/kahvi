*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Add Reference Page

*** Test Cases ***

Set Correct Information For Inproceedings Reference
    Select Dropdown By Value  book
    Wait For Form To Load
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

Reset Application And Go To Add Reference Page
    Reset Application
    Go To Add Reference Page