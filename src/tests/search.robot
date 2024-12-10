*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To References Page

*** Test Cases ***
Search Shows Correct Results
    Set Keyword  heaven
    Click Button  Search
    References Page Should Be Open
    Page Should Contain  Robert

Keyword That Does Not Appear In Any Reference Should Not Give Results
    Set Keyword  rainbow
    Click Button  Search
    References Page Should Be Open
    Page Should Not Contain  Robert

***Keywords***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    booktitle

Set Keyword
    [Arguments]  ${query}
    Input Text  query  ${query}