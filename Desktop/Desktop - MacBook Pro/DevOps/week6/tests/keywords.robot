*** Keywords ***
Open Google And Search
    [Arguments]  ${query}
    Open Browser  https://www.google.com  chrome
    Input Text  name=q  ${query}
    Press Keys  name=q  RETURN
    Sleep  3s
    Close Browser
