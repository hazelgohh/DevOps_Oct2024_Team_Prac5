*** Settings ***
Library  SeleniumLibrary
Resource  variables.robot

*** Test Cases ***
Search Google With Variable
    [Documentation]    Open Google and search using a variable
    Open Browser    https://www.google.com    ${BROWSER}
    Input Text    name=q    ${SEARCH_TERM}
    Press Keys    name=q    RETURN
    Sleep    3s
    Close Browser
