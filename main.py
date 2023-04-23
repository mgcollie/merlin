import argparse
import logging
import os
import sys
import functions.auto_docstrings
import functions.auto_tests
import functions.auto_typehints
import functions.auto_all
from typing import List


__doc__ = """
A program to run specific tasks on a set of python files. Supported tasks include generating
docstrings, generating unit tests, and adding type hints.
"""


def find_python_files(path: str ) -> List[str]:
    """Find all Python files recursively in a given directory."""
    python_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


def cli():
    """Command line interface."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--files', nargs='+', help='Files to process')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO')
    parser.add_argument('--dry-run', action='store_true', help='Print the output instead of writing to files')
    parser.add_argument('--task', choices=['docs', 'tests', 'typehints', 'all'], default='all', help='Task to execute')
    parser.add_argument('--style', choices=['google', 'numpy', 'sphinx', 'reStructuredText'], default='google',
                        help='Docstring style')

    return parser.parse_args()


def main():
    """Main entry point."""

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
        "all": functions.auto_all.main,
    }

    # Execute the appropriate task
    return task_mapping[args.task](args)


if __name__ == '__main__':
    sys.exit(main())