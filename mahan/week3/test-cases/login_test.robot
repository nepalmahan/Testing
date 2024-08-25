*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     http://localhost:8000  # Replace with the URL where your HTML file is served
${BROWSER}  chrome  # You can change to 'firefox' or any other supported browser

*** Test Cases ***
Valid Login Test
    [Documentation]    Test valid login credentials
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=username    testuser
    Input Text    id=password    testpassword
    Click Button    xpath=//button[@type='submit']
    # Add assertions here to verify the result, e.g., checking a success message or redirection
    Close Browser
