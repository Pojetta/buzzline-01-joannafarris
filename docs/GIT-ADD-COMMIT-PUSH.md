## Git Add-Commit-Push

> Short guide to using Git to keep our machine work synchronized with the GitHub repo. 

## After Working Locally (On Our Machine) 

After making successful changes on our machine, we should run:

1. git **add** the files to source control.
2. git **commit** the files as a named set of changes.
3. git **push** the files to the GitHub repository.

Reading takes longer than the commands. 
The first times are more difficult, but we'll do these often and you'll soon be proficient.

Open a terminal (PowerShell if Windows, default for Mac/Linux) and run each command one at a time, waiting for it to finish before running the next. 

```shell
git add .
git commit -m "Initial change"
git push -u origin main
```

IMPORTANT: Always change the commit message to reflect what you did - e.g., "Add new producer", "Add new consumer", "Customize producer", "Update consumer alert", "Update README.md".
Professional communication skills make valuable team members.  

Later git pushes can be simplified - try just git push and see how it goes. 

```shell
git push
```

## Before Working Locally (On Our Machine) 

Before starting to make changes on our machine, we should run:

1. git **pull** to fetch any changes we made directly in GitHub.

```shell
git pull
```

## Terminal Help

- Use the UP ARROW to access a previously entered command. 
- Use the RIGHT ARROW to accept a terminal suggestion
