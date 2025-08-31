# Python Module and Package Imports

Using py -m (or python3 -m on Mac/Linux) runs a script as part of a package, 
ensuring Python uses the project’s root directory to resolve imports.

## Package Context

When using the -m flag, Python treats the directory containing the script 
as part of a package and uses the parent directory as the root package. 
This allows absolute imports like `from utils.utils_logger import logger` 
to work because Python knows to start looking from the root directory.

## Direct Execution Issue

Running a script directly (e.g., `py producers\basic_producer_case.py`) 
makes Python treat the producers folder as the starting point for resolving imports. 
In this case, Python cannot find utils because it does not automatically 
treat the parent directory as the root.

## When This Is Needed

Projects with subdirectories (producers, consumers, utils) often 
import from other local code files.
To resolve these local imports, Python must understand the package structure, 
which is activated when using the -m (module) flag to run. 
