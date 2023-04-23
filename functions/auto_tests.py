from merlin.iterate_files import iterate_files


def main(args) -> None:
    """Main entry point.

    Args:
        args: Command line arguments.
    """

    signature = "def auto_tests(code: str) -> str:"
    description = (
        "Analyzes the code and then generates and returns all "
        " unit tests that are required to achieve maximal coverage. "
        "Includes all required imports as well."
    )

    return iterate_files(args.files, signature, ["None"], description, is_test=True, dry_run=args.dry_run)