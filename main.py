import argparse
import logging
import os
import sys
from typing import List
import functions.auto_docstrings
import functions.auto_tests
import functions.auto_typehints


__doc__ = """
A program to run specific tasks on a set of python files. Supported tasks include generating
docstrings, generating unit tests, and adding type hints.
"""


def find_python_files(path: str) -> List[str]:
    """
    Find all Python files recursively in a given directory, ignoring virtual environments.

    Args:
        path (str): The path to search for Python files.

    Returns:
        List[str]: A list of Python file paths.
    """
    python_files = []
    venv_directories = ['venv', '.venv']

    for root, dirs, files in os.walk(path):
        # Ignore virtual environment directories
        dirs[:] = [d for d in dirs if d not in venv_directories and not d.startswith('env')]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


def cli() -> argparse.Namespace:
    """
    Command line interface.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--files', nargs='+', help='Files to process')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO')
    parser.add_argument('--dry-run', action='store_true', help='Print the output instead of writing to files')
    parser.add_argument('--task', choices=['docs', 'tests', 'typehints', 'all'], default='all', help='Task to execute')
    parser.add_argument('--style', choices=['google', 'numpy', 'sphinx', 'reStructuredText'], default='google',
                        help='Docstring style')

    return parser.parse_args()


def main() -> int:
    """
    Main entry point.

    Returns:
        int: Exit code (0 for success, 1 for failure).
    """

    args = cli()

    logging.basicConfig(level=args.log_level)

    # If no files are provided, search the current directory
    if not args.files:
        args.files = find_python_files(os.getcwd())

    # Define a mapping of command-line arguments to functions
    task_mapping = {
        "docs": functions.auto_docstrings.main,
        "tests": functions.auto_tests.main,
        "typehints": functions.auto_typehints.main,
    }

    # Execute the appropriate task
    try:
        # Execute the appropriate task
        if args.task == "all":
            for task_function in task_mapping.values():
                try:
                    task_function(args)
                except Exception as e:
                    raise e
        elif args.task:
            return task_mapping[args.task](args)

        return 0
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
