from merlin.iterate_files import iterate_files


def main(args):
    """Main entry point."""

    signature = "def auto_all(code: str, style: str) -> str:"
    description = (
        "Returns the entire code along with all missing/incorrect "
        "typehints, docstrings, and unit tests. Using the passed "
        "style argument for docstring convention. The goal is to"
        "maximize code coverage.  It is imperative that the code "
        "functions correctly and would pass even the most stringent"
        " of code reviews."
    )

    return iterate_files(args.files, signature, [args.style], description, dry_run=args.dry_run)

