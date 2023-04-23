from merlin.iterate_files import iterate_files


def main(args):
    """Main entry point."""

    signature = "def auto_tests(code: str) -> str:"
    description = (
        "Analyzes the code and then generates and returns all "
        " unit tests that are required to achieve maximal coverage."
    )

    return iterate_files(args.files, signature, ["None"], description, is_test=True, dry_run=args.dry_run)