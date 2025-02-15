*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Fill Form
    Open Browser    https://formy-project.herokuapp.com/form    chrome
    Input Text    id=first-name    John
    Input Text    id=last-name    Doe
    Input Text    id=job-title    QA Engineer
    Click Element    xpath=//input[@id="radio-button-2"]  # Selects a radio button
    Click Element    xpath=//input[@id="checkbox-1"]  # Selects a checkbox
    Select From List By Label    id=select-menu    Option 3  # Select from dropdown
    Click Button    xpath=//button[@type='submit']  # ✅ Updated locator for Submit
    Sleep    3s
    Close Browser
