# buzzline-01-case

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project introduces streaming data. 
The Python language includes generators - we'll use this feature to generate some streaming buzzline messages. 
As the code runs, it will continuously update the log file. 
We'll use a consumer to monitor the log file and alert us when a special message is detected. 

## Task 1. Set Up Your Machine & Sign up for GitHub

We practice professional Python. In each course that uses Python, we use a standard set of popular professional tools. 
This course uses advanced tools such as Apache Kafka that requires **Python 3.11**. 
You are encouraged to install and practice with multiple versions. 
If space is an issue, we only need Python 3.11 for this course. 

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 1: Set Up Machine & Sign up for GitHub**.

**Setup is critical.** Follow all steps exactly and verify success before proceeding.  
Missing or incomplete setup steps can make the course impossible to complete.

## Task 2. Initialize a Project

Once your machine is ready, you'll copy this template repository into your own GitHub account  
and create your personal version of the project to run and explore. 
Name it **buzzline-01-yourname** (replace `yourname` with something unique to you).  

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 2: Initialize a Project**.
This will get your project stored safely in the cloud - and ready for work on your machine. 

## Task 3. Generate Streaming Data (Terminal 1)

Now we'll generate some streaming data. 
By the way - you've done 90% of the hard work before we even look at code. 
Congratulations!

In VS Code, open a terminal.
Use the commands below to activate .venv, and run the generator as a module. 
To learn more about why we run our Python file as a module, see [PYTHON-PKG-IMPORTS](docs/PYTHON-PKG-IMPORTS.md) 

Windows PowerShell:

```shell
.venv\Scripts\activate
py -m producers.basic_producer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.basic_producer_case
```

## Task 4. Monitor an Active Log File (Terminal 2)

A common streaming task is monitoring a log file as it is being written. 
This project has a consumer that reads and processes our own log file as log messages arrive. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and run the file as a module. 

Windows:
```shell
.venv\Scripts\activate
py -m consumers.basic_consumer_case
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_consumer_case
```

## How to Stop the Processes
Stop a continuous process (kill it) by selecting the terminal and hitting CTRL+c (press CTRL key and c key at the same time). 

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 
We will get a good amount of practice. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.
