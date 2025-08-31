# Make This Project Your Own

This guide walks you through the steps to:

- Start with an example project.
- Copy it into your own GitHub account.
- Rename it with your own unique name.
- Clone it to your local machine.
- Open and explore the project in VS Code for editing and learning.

## Copy This Repository

1. Login to GitHub.
2. Go to the existing example repository.
3. Click "Fork" or "Use This Template" to copy it into your GitHub account.

IMPORTANT: Rename the repo to include yourname (or something unique). 
Follow naming conventions - use all lowercase, no spaces, and use dashes between words. 
"Forking" keeps you tied to the original repo. 
"Use this template" removes the link.

## Clone YOUR Repository to Your Machine

In your browser, click on YOUR new repository.
Copy the URL into your clipboard (e.g. using CTRL a and CTRL c).

### Windows
On your machine, open a PowerShell terminal. 
Execute the commands one at a time to:
  1. Change directory to the root (C:\)
  2. Create a Projects folder (if you don't already have one) 
  3. Clone YOUR repo into your C:\Projects.
  4. Change directory into your new repository folder. 
  5. Open your new folder in VS Code.

```shell
cd \
mkdir Projects
cd Projects
git clone https://github.com/**youraccount**/**your-repo-name**
cd **your-repo-name**
code .
```

### Mac/Linux
On your machine, open a terminal. 
Execute the commands one at a time to:
  1. Change directory to the root (~)
  2. Create a Projects folder (if you don't already have one) 
  3. Clone YOUR repo into your ~\Projects.
  4. Change directory into your new repository folder. 
  5. Open your new folder in VS Code.

```zsh
cd \
mkdir Projects
cd Projects
git clone https://github.com/**youraccount**/**your-repo-name**
cd **your-repo-name**
code .
```

## Exploring the Project Folder in VS Code

The last command "code space dot" opens the current folder in VS Code. 
Trust the author when prompted by VS Code.
See the files down the left side Explorer. 
Close the welcome page after reviewing it. 

## Open a Terminal in VS Code
    
Open a terminal in VS Code by selecting Terminal > New Terminal from the menu.
(Click the three dots in the toolbar if the menu isn't fully visible.)

In Windows, we provide PowerShell commands (cmd is deprecated and not recommended).
