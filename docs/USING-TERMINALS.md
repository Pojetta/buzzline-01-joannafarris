# Using Terminals

Use the UP ARROW to show the prior command. 

Use the RIGHT ARROW to select a suggested command.

Type the `clear` command to clean up the terminal.

```shell
clear
```

## Close a Terminal / Kill a Process

Try CTRL c or CMD c to kill a running process and close a terminal window. 

Or use your mouse to click the X or trashcan icon (e.g. 🗑) in VS Code Terminals to close a terminal window. 


## One Open Terminal Per Running Process

If we're using a terminal to produce or consume streaming data, it must remain open. 
We cannot reuse that terminal unless the streaming process stops - either it times out, runs out of data, or we close the terminal window. 

## Multiple Terminals

When working with producers and consumers, we will typically have multiple terminals open - one per running process. 
Multiple terminals are common when working with streaming analytics. 
