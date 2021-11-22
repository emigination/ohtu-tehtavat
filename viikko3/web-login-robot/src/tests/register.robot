*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Registration Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kissa
    Set Password  karvapall0
    Set Password Confirmation  karvapall0
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  karvapall0
    Set Password Confirmation  karvapall0
    Submit Credentials
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kisu
    Set Password  hiir1
    Set Password Confirmation  hiir1
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kissimirri
    Set Password  karvapall0
    Set Password Confirmation  mjauuuuuu1
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
