*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***

Set Correct Information For Book Reference
    Select Dropdown By Value  book
    Check Form Is Loaded
    Set Reference Id  dd313
    Set Author  Donald D. Duck
    Set Title  Hannu Hanhi Is A D*ck
    Set Editor  Scrooge McDuck
    Set Year  1984
    Set Publisher  Duckburg publishing
    Set Tag  Hupsuja juttuja
    Submit Information
    Adding Reference Should Succeed

Try Adding Book Reference With Missing Information
    Select Dropdown By Value  book
    Check Form Is Loaded
    Set Reference Id  dd313
    Set Title  Hannu Hanhi Is A D*ck
    Set Editor  Scrooge McDuck
    Set Year  1984
    Set Publisher  Duckburg publishing
    Submit Information
    Adding Reference Should Fail

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    editor