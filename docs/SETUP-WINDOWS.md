# Windows Installation Instructions

Follow the steps carefully. Spacing, capitalization, spelling matter.

-----

## Enable File Explorer View Settings

1. Open File Explorer.
2. Click the View tab on the ribbon.
3. In the Show/Hide group, check:
   - File name extensions.
   - Hidden items.

-----

## Install Essential Tools with WinGet Package Manager

Open a PowerShell terminal (as Administrator) and run the following commands one at a time. 
Copy or type just the one line command and hit ENTER to run it. 

```shell
winget install --id Git.Git -e --source winget

winget install --id Python.Python.3.11 -e --source winget 

winget install --id Microsoft.VisualStudioCode -e --source winget
```

## Verify Installations

Close that terminal. Open a new PowerShell terminal. 
Run the following commands one at a time to verify. 

```shell
git --version
py --version 
python --version 
code --version
```

Note:
- The Windows Python launcher (py) will show the highest version number installed, e.g. 3.11 or 3.13). 
- The python command will show the most recent installation, e.g. 3.11.

-----

## Configure Git

Configure your git user.name and user.email. 
Use YOUR name and email in the commands below. 
Use the same email you used for GitHub. 
School emails may be temporary - you may wish to use a more permanent email. 

```shell
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
git config --list
```
-----

## VS Code: Turn on File / Autosave

Open VS Code. From the VS Code menu, use File / Autosave. 
If you don't choose to use this feature, remember to save all changes manually. 

## VS Code: Extensions

Once we start using .py files, VS Code will ask to install the recommended Python extension. 
Accept the suggestion to install it. 
Otherwise, go to the Extensions icon down the left side and search for and install:

- Python by Microsoft
- PowerShell by Microsoft
- Markdown All in One by Yu Zhang
