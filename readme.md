# Caesar cipher API
### 1.Summary
This API let You encrypt and decrypt messages using caesar cipher.\
Go to Site address/encrypt?msg=XXX&key=Y, XXX is your message and Y is key You want to use for encryption(1-25)\
Go to Site address/decrypt?msg=XXX&key=Y, XXX is your message and Y is key You want to use for encryption(1-25)\
Works only with english alphabet.
Created with FastAPI and Uvicorn.
## 2.Instalation
#### Requierments:
-Python version 3.9.13 or higher\
-FastAPI\
-Uvicorn
#### Manual instalation:

1. Create directory for the application
2. Copy all files from the repository to directory You created
#### Instalation with Git:
In command line execute :
>git clone https://gitlab.portal.futurecollars.com/michal_lorenc/Caesar-cipher-API.git

It will create a directory named Caesar-cipher-API in your active directory(default: C/Users/username)

## 3.Start-up

1. Creating virtual environment
In command line execute
>  python -m venv env
2. Activating virtual environment
>  env/Scripts/activate
3. Instalation of packets and libraries used by app
> pip install -r requirements.txt
4. Booting server for app. By default, server runs on local host adress: http://127.0.0.1:8000
>  uvicorn main:app
