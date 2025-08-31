# Mac/Linux Installation Instructions

Follow the steps carefully. Spacing, capitalization, spelling matter.

-----

## Enable Finder View Settings

1. Open your file manager (e.g., Finder on Mac).
2. Enable viewing hidden files and folders:
   - Mac: Press Cmd+Shift+. in Finder to toggle hidden files.
   - Linux: Use your file manager settings to show hidden files.
3. Enable viewing file extensions:
   - Mac: In Finder, go to Preferences > Advanced and check "Show all filename extensions."
   - Linux: Use your file manager settings to show file extensions.

-----
## Install Homebrew Package Manager

Homebrew is a package manager for Mac/Linux. Install it with this command.


```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, add Homebrew to your shell profile:

```zsh
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```
-----

## Install Essential Tools with Homebrew Package Manager

```zsh
brew install git
brew install python@3.11 
brew install --cask visual-studio-code
```

## Verify Installations

Close that terminal. Open a new terminal. 
Run the following commands one at a time to verify. 

```zsh
git --version
python3.11 --version  
python3 --version  
code --version
```

On Mac/Linux, the python3 command typically uses the default Python
 version set in your system's PATH. 
 This is not necessarily the most recent or last-installed version 
 but depends on the order in which Python versions are listed in the PATH.

We will manage the project version by using .venv, our local project virtual environment. 

-----

## Configure Git with User Name and User Email

Configure your git user.name and user.email. 
Use YOUR name and email in the commands below. 
Use the same email you used for GitHub. 
School emails may be temporary - you may wish to use a more permanent email. 

```zsh
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
