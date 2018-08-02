This directory contains all the scripts in the repo. 

## Contents
1. [Guidelines](#guidelines)
2. [Template](#template)
3. [Scripts](#script)

## Guidelines
-  Each script should be in it's own seperate directory.
-  The script name must be same as the directory name of the script.
-  All scripts should be invokable as `python main.py`. That is, the file that is to be called by the python interpreter should be named `main.py`.
- If your script has dependencies, it should contain a `requirements.txt`.
- Each script directory should contain a `README.md` file with installation and usage instructions, description, and any other information needed.
- You should also edit this README and add your script to it in accordance with the [template](#template).
- If the script you are contributing is under version control, make sure you add it as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
-  Any contributions that fail the status checks will not be accepted unless there is a very good reason to accept them.
- When adding scripts to the `scripts/README.md` file, keep the following points in mind to prevent the CI status check from failing:
    * The template is followed perfectly.
	* The name of the directory containing the script is the same as the name of the script in `scripts/README.md`.
	* The comments that delimit the scripts section are not altered.
	* You add your script **between** the `scriptsstart` and `scriptsstop` comments.

## Template
Your contribution should update this README with the following information, and in accordance with this template:

-	script-name<br />
	Description<br />
	[Author's Name](#)

## Scripts
<!-- scriptsstart -->
-	tictactoe<br />
	A cli-based tictactoe game to play with the computer.<br />
	[Rounak Vyas](http://www.github.com/itsron717)
<!-- scriptsstop -->
