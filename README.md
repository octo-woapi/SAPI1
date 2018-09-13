# SAPI1
Basic API for SAPI1 live coding

# Getting started

## Python 3.5 and dependencies installation

> On UNIX/Linux environments

  - Install python 3
    ```$ sudo apt-get install python3```
  - Install pip3
    ```$ sudo apt install python3-pip```
  - Install virtualenv
    ```$ pip3 install virtualenv```

> On MAC environments

  - Install python 3
    ```$ brew install python3```
  - Install pip3
    ```$ brew install python3-pip```
  - Install virtualenv
    ```$ pip3 install virtualenv```


> On Windows environments

  - Install [python3.5.4 from the website](https://www.python.org/downloads/release/python-354/)
    Download and install the Windows x86 64 executable installer
  - Install virtualenv
    see the [official documentation](https://virtualenv.pypa.io/en/stable/userguide/) for installation and usage on windows

## Clone the project

  - Create a folder in your workspace that will be dedicated to the project. Every command will be made from this folder
    ```$ git clone git@github.com:octo-woapi/SAPI1.git```


## Makefile

A makefile is a special file, containing shell commands with shortcuts. The command ```make``` is used to execute commands from the Makefile. It is native on Unix and MACOSX OS.
If you have troubles installing or using **make** in a Windows environment, you can open the Makefile file and copy the commands you want to execute directly into your terminal


## Virtual environment

The API project is accessible via a python virtual environment. For more informationlis about virtualenvs, check the [official documentation](https://virtualenv.pypa.io/en/stable/)

Create a virtual environment inside the api_cost_estimator folder

    virtualenv venv

> Check the existence of a sub-folder named **venv**

Every command or action should now be made inside the virtual environment. To activate the virtual environment :

On Linux / MAC : ```source venv/bin/activate```

On Windows : ```venv/Scripts/activate.bat```

> Check that your prompt starts with **(venv)**

## Install dependencies

  This command should be made inside the virtual environment only.

    make install_requirements_dev

## Start the API

  This command should be made inside the virtual environment only.

    make start

  The API runs on the address **127.0.0.1** (localhost) on the port **5000**
  
  Visit http://localhost:5000/sapi/hello

