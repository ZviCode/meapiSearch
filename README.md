# meapiSearch
Searching people by phone number using the ME API

With God's help

This project aims to create an HTTP server that returns the details ME has about a phone number sent to the server

A few things to do before running it in Docker:

######The verification phase#######

1) Edit the cell phone number through which you will perform the search in the app.py file in line 6
2)Run python3 app.py
3)Perform the verification as it says there (via WhatsApp/Telegram)
4)If you passed the authentication successfully, the login token will be written to you in the config.json file
5)Now you can run it properly with an HTTP server


Things that need (or can be changed):

1) in the Dockerfile:
Line 3 = Change to the location of the file
Line 7 and line 19= You can change to another port instead of 12345

2) in the app.py:
Line 6 = You must go through the verification phase
Line 26 = You can change to another port instead of 12345
3) in the confing.json:
Do not make any manual changes to the file


Credit and sources:

https://meapi.readthedocs.io/en/latest/index.html

https://github.com/david-lev

https://flask.palletsprojects.com/en/2.2.x/

https://www.docker.com/
