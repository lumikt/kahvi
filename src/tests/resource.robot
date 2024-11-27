*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Library    XML

*** Variables ***
${SERVER}       localhost:5001
${DELAY}        0.5 seconds
${ADD_REFERENCE_URL}  http://${SERVER}
${BROWSER}      chrome
${HEADLESS}     false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Add Reference Page Should Be Open
    Title Should Be  Latex Reference App - Add reference

References Page Should Be Open
    Title Should Be  Latex Reference App - References

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Go To References Page
    Click Link  Added references

Adding Reference Should Succeed
    References Page Should Be Open

Adding Reference Should Fail
    Add Reference Page Should Be Open

Adding Reference Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Information
    Click Button  Add reference
    
Select Dropdown By Value
    [Arguments]  ${value}
    Select From List By Value  id=chosen_ref  ${value}

Set Reference Id
    [Arguments]  ${citation_key}
    Input Text  citation_key  ${citation_key}
    
Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Number
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set DOI
    [Arguments]  ${DOI}
    Input Text  doi  ${DOI}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

