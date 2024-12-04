*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***

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
    Press Keys    tag-input    ENTER
    Submit Information
    Adding Reference Should Succeed
    Page Should Contain    cosmere

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    editor
