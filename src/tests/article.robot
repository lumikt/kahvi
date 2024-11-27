*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Add Reference Page

*** Test Cases ***
Set Correct Information For Article Reference
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

*** Keywords ***
Adding Reference Should Succeed
    Add Reference Page Should Be Open

Adding Reference Should Fail With Message
    [Arguments]  ${message}
    Add Reference Page Should Be Open
    Page Should Contain  ${message}

Submit Information
    Click Button  Add reference
    
*** Keywords ***
Reset Application And Go To Add Reference Page
    Reset Application
    Go To Add Reference Page