# readme-check

This test ensures that every directory in the `scripts` folder has a corresponding entry in `scripts/README.md` and vice versa. This is to help contributors who forget to update the readme quickly realize their mistake and fix it.

## Usage

1. Make the script executable - `$ chmod +x path/to/script/main.py`
2. Execute the script - `$ path/to/script/main.py path/to/readme path/to/scripts`

The script exits with a non-zero exit code if there is an inconsistency in the directories in the `scripts` folder and the scripts listed in `scripts/README.md`.

In the use case of [pythonista](https://github.com/pyista/pythonista) (and in almost every use case) the `README.md` file resides in the same folder as all the scripts, so we invoke it as follows (from the project root):<br />
`$ ./test/readme-check/main.py ./scripts ./scripts`.

## Running Tests

Since this is a minimal utility script, a couple of test cases have been written in the `run_tests` method in the script. These correspond to use cases that are shown in the `tests/test1` and `tests/test2` folders. You can run the tests by running:<br />
`$ ./test/readme-check/main.py test`.

## Author

This script was authored by [Mohammed Ajmal Siddiqui](https://github.com/ajmalsiddiqui) for the [pythonista](https://github.com/pyista/pythonista) project.
