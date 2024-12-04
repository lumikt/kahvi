*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***
Add Reference With Several Tags
    Select Dropdown By Value  book
    Check Form Is Loaded
    Set Reference Id  mb04
    Set Author  Brandon Sanderson
    Set Title  Mistborn
    Set Editor  Peter
    Set Year  2004
    Set Publisher  Tor publishing
    Set Tag  cosmere
    Set Tag  Mistborn Era 1
    Check Form Is Loaded
    Submit Information
    Adding Reference Should Succeed
    Page Should Contain    cosmere
    Page Should Contain    Mistborn Era 1

Add Book Reference With Tag
    Select Dropdown By Value  book
    Check Form Is Loaded
    Set Reference Id  row21
    Set Author  Brandon Sanderson
    Set Title  Rhythm of War
    Set Editor  Peter
    Set Year  2022
    Set Publisher  Tor publishing
    Set Tag  cosmere
    Submit Information
    Adding Reference Should Succeed
    Page Should Contain    cosmere

View Added Tag
    Go To References Page
    Page Should Contain  cosmere
    Page Should Contain  Mistborn Era 1

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    editor
