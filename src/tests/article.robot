*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***
Adding Reference With Correct Information Succeeds
    Select Dropdown By Value    article
    Check Form Is Loaded
    Set Reference Id  1
    Set Author  Donald E. Knuth
    Set Title  Pythn Programming
    Set Journal  The Computer Journal
    Set Year  1984
    Set Number  2
    Set Pages  97-111
    Set DOI  knuth:1984
    Submit Information
    Adding Reference Should Succeed

Adding Reference With Missing Information Fails
    Select Dropdown By Value    article
    Check Form Is Loaded
    Set Reference Id  2
    Set Title  Booktitle
    Set Journal  Science journal
    Set Year  1999
    Set Tag  Kandi
    Submit Information
    Adding Reference Should Fail

Adding Reference With Incorrect Information Type Fails
    Select Dropdown By Value    article
    Check Form Is Loaded
    Set Reference Id  2
    Set Title  Booktitle
    Set Journal  Science journal
    Set Year  nineteen ninety nine
    Set Tag  Kandi
    Submit Information
    Adding Reference Should Fail

*** Keywords ***
Check Form Is Loaded
    Wait Until Keyword Succeeds    30s    2s    Page Should Contain Element    journal