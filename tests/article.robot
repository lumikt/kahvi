*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application
Library    ../.venv/lib/python3.10/site-packages/robot/libraries/OperatingSystem.py

*** Test Cases ***
Set Correct Information
    Set Authors  Donald E. Knuth
    Set Title  Literate Programming
    Set Journal  The Computer Journal
    Set Year  1984
    Set Number  2
    Set Pages  97-111
    Set DOI  knuth:1984
    Submit Information
    Adding Reference Should Succeed

*** Keywords ***
Adding Reference Should Succeed
    Add Reference Page Should Be Open

Adding Reference Should Fail With Message
    [Arguments]  ${message}
    Add Reference Page Should Be Open
    Page Should Contain  ${message}

Submit Information
    Click Button  Lisää viite

Set Authors
    [Arguments]  ${kirjoittajat}
    Input Text  kirjoittajat  ${kirjoittajat}

Set Title
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Set Journal
    [Arguments]  ${julkaisu}
    Input Text  julkaisu  ${julkaisu}

Set Year
    [Arguments]  ${vuosi}
    Input Text  vuosi  ${vuosi}

Set Number
    [Arguments]  ${julkaisunumero}
    Input Text  julkaisunumero  ${julkaisunumero}

Set Pages
    [Arguments]  ${sivut}
    Input Text  sivut  ${sivut}

Set DOI
    [Arguments]  ${doi}
    Input Text  doi  ${doi}
