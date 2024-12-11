*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Homepage

*** Test Cases ***

Navigate To Homepage
    Click Link  Homepage
    Homepage Should Succeed

Navigate To Added References
    Click Link  Added references
    Added References Page Should Succeed

Navigate To Added References In Bibtext Form
    Click Link  Added references in bibtex form
    Added References In Bibtext Form Page Should Succeed

Navigate To New Reference And Show Required Fields
    Click Link  Add new reference
    Add New Reference Page Should Succeed
    Page Should Contain    *

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    booktitle

Homepage Should Succeed
    Home Page Should Be Open

Added References Page Should Succeed
    References Page Should Be Open

Added References In Bibtext Form Page Should Succeed
    Bib References Page Should Be Open

Add New Reference Page Should Succeed
    Add Reference Page Should Be Open
