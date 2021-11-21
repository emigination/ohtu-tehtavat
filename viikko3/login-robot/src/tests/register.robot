*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  karvapall0
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kissa  karvapall0
    Input New Command
    Input Credentials  kissa  tiikerikiss4
    Output Should Contain  Username alreayd taken

Register With Too Short Username And Valid Password
    Input Credentials  k  karvapall0
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  kissa  hiir1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissa  karvapallo
    Output Should Contain  Password must contain a character that is not a letter