*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Homepage

*** Test Cases ***

*** Keywords ***

Reset Application And Go To Homepage
    Reset Application
    Go To Homepage
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    booktitle