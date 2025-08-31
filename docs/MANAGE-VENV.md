# Manage Our Local Project Virtual Environment

## One-time Only: Create it 

Use the built in venv utility to create a local project virtual environment in a folder named .venv. 

Windows: 
```shell
py -3.11 -m venv .venv
```

Mac/Linux:
```zsh
python3 -3.11 -m venv .venv
```
Be patient. will end and a new .venv folder will appear.
This folder will become very large - we don't do anything with it directly, 
but Python will use this local virtual environment folder to hold a lot of
free code that we will use in our project. 

## As Needed: Activate .venv and Install Packages

Run the following commands to activate our local project virtual environment 
and install necessary packages. 
Wait for each command to finish before running the next command. 

Windows: 

```shell
.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

Mac/Linux: 

```zsh
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt
```

When done, .venv may be large. Allow time.

## Activate Every Time We Open a New Terminal 

Remember to always activate the .venv when opening a new terminal. 

Windows: 

```shell
.venv\Scripts\activate
```

Mac/Linux:

```shell
source .venv/bin/activate
```
