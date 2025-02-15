*** Settings ***
Library  RequestsLibrary

*** Test Cases ***
Check API Response
    ${response}=  GET  https://jsonplaceholder.typicode.com/posts/1
    Log  ${response.json()}
