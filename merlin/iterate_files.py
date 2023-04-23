import logging
import os
from merlin.call_ai_function import call_ai_function
from typing import List, Any


def iterate_files(filenames: List[str], function: str, args: List[Any],
                  description: str, is_test: bool = False, dry_run: bool = False) -> int:
    """
    Iterates through a list of files, applying a specified function to each file.

    Args:
        filenames (List[str]): A list of filenames to process.
        function (str): The name of the function to apply to each file.
        args (List[Any]): A list of arguments to pass to the function.
        description (str): A description of the function being applied.
        is_test (bool, optional): If True, appends "_tests" to the output filename. Defaults to False.
        dry_run (bool, optional): If True, does not write the modified code to the file. Defaults to False.

    Returns:
        int: Always returns 0.
    """
    for filename in filenames:
        try:
            print(f"Processing {filename}...")
            code = open(filename, 'rb').read().decode('utf-8')
            nargs = [code, args]

            modified = call_ai_function(function, nargs, description).encode('utf-8')

            # Conditionally append the filename with _tests.py if is_test is True
            name, extension = os.path.splitext(filename)
            output_filename = f"{name}_tests{extension}" if is_test else filename

            if not dry_run:
                with open(output_filename, 'wb') as f:
                    f.write(modified)
            else:
                logging.info(modified)

        except (FileNotFoundError, IsADirectoryError) as e:
            logging.error(f"File not found: {filename}")

    return 0
