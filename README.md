# meapiSearch
Search people by phone number using the ME API

With God's help

This project aims to create an HTTP server that returns the details ME has about a phone number sent to the server

A few things to do before running it on Docker:

######Verification step##### 
1)In line 8 put this the first time you run the script
me = Me(interactive_mode=True)
2)Run python3 app.py
Select an authentication method and authenticate the session
3)If you passed the authentication successfully, the login token will be written to you in the meapi_credentials.json file
4)Change line 8 to
me = Me(phone_number=972000000)
When instead of 972000000 write down the number you verified earlier
5)Now you can upload the docker file


Things you need (or can change):

1)In Dockerfile:
Line 7 and line 13 = you can go to another exit instead of 12345

2)In app.py:
Line 8 = You must pass the verification step
Line 51 = You can switch to another port instead of 12345
3)In the meapi_credentials.json file:
Do not make manual changes to the file


Credit and sources:

https://meapi.readthedocs.io/en/latest/index.html

https://github.com/david-lev