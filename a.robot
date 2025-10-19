*** Settings ***
Documentation     Example using the space separated format.
Library           OperatingSystem
Library    SeleniumLibrary
Variables  resources/variables.py
Library    resources/CustomKeywords.py


*** Variables ***
${MESSAGE}        Hello, world!
${URL}         https://www.demoblaze.com/index.html
${BROWSER}     chrome

*** Test Cases ***
Sign Up New User
    Open Site    ${URL}
    ${USERNAME}    ${PASSWORD}=    Sign Up To Demoblaze    user
    Log    Зарегистрирован новый пользователь: ${USERNAME}
    CustomKeywords.Close Browser

Login And Logout
    [Documentation]   Login
    Open Site    ${URL}
    Login To Demoblaze    ${USERNAME}    ${PASSWORD}
    Verify Login Successful    ${USERNAME}
    #Click Element    id:login2
    Sleep    3s
    Log Out From Demoblaze
    CustomKeywords.Close Browser

Login Buy And Logout
    Open Site    ${URL}
    ${USERNAME}    ${PASSWORD}=    Sign Up To Demoblaze    autotest
    CustomKeywords.Close Browser
    Open Site    ${URL}
    Login To Demoblaze    ${USERNAME}    ${PASSWORD}
    Verify Login Successful    ${USERNAME}
    Buy Product From Demoblaze    Samsung galaxy s6
    Log Out From Demoblaze
    CustomKeywords.Close Browser

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}