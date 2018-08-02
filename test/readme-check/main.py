#!/usr/bin/env python3

from pathlib import Path
import os
import re
import sys

# TODO: Add docstring specifying that path_to_readme is an instance of PosixPath


def read_readme(path_to_readme):
    path_to_readme = path_to_readme / "README.md"
    readme = open(path_to_readme, "r").read()

    return readme

# TODO: path_to_scripts is a Path object. Make docstring


def get_scripts_list(path_to_scripts):
    # path_to_scripts = Path(path_to_scripts)
    dir_list = [dirname for dirname in os.listdir(
        path_to_scripts) if os.path.isdir(os.path.join(path_to_scripts, dirname))]

    return dir_list


def get_titles_from_readme(readme):
    # Note: All of this can be done in fewer steps
    # This is just for readibility
    scripts = readme.split("<!-- scriptsstart -->")[1]
    scripts = scripts.split("<!-- scriptsstop -->")[0]
    scripts = scripts.split("-\t")[1:]
    scripts = [re.split(r"\n|<br>|<br\s?/>", script)[0] for script in scripts]
    scripts = [re.sub(r'[\n|\t]*', "", script) for script in scripts]

    return scripts


def test_scripts(path_to_readme, path_to_scripts):
    titles = get_titles_from_readme(read_readme(path_to_readme))
    scripts = get_scripts_list(path_to_scripts)
    return set(titles) == set(scripts)

# TODO add docstring


def run_tests():
    print("[readme-check] Running tests...")
    test1_dir = Path(os.path.dirname(__file__) + "/tests/test1")
    test2_dir = Path(os.path.dirname(__file__) + "/tests/test2")

    test1 = test_scripts(test1_dir, test1_dir)
    test2 = test_scripts(test2_dir, test2_dir)

    print("[readme-check] Test 1 complete.\nExpected output: {}\nActual output: {}\n".format(True, test1))
    print("[readme-check] Test 2 complete.\nExpected output: {}\nActual output: {}\n".format(False, test2))

    if test1 and not test2:
        print("[readme-check] All test cases passed!")
        return True

    print("[readme-check] Some test cases failed.")
    return False


if __name__ == "__main__":
    try:
        if sys.argv[1] == "test":
            if not run_tests():
                sys.exit(1)
            else:
                sys.exit(0)
        README_PATH = Path(sys.argv[1])
        SCRIPTS_PATH = Path(sys.argv[2])
        if test_scripts(README_PATH, SCRIPTS_PATH):
            print("[readme-check] README check passed. Everything looks fine!")
            sys.exit(0)
        else:
            print("[readme-check] README check failed. Ensure that you've updated the README.md file in the scripts folder and that the name of the script matches the name of the directory.")
            sys.exit(1)
    except Exception:
        print("[readme-check] Error: Something went wrong. Did you forget to give the path to README.md or the path to scripts?")
        sys.exit(2)
