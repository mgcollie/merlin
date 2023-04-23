from merlin.iterate_files import iterate_files


def main(args):
    """Main entry point."""

    signature = "def auto_typehints(code: str) -> str:"
    description = (
        "Returns the entire code with missing and or corrected typehints."
        "First it tests to see if there are any missing or incorrect typehints."
        "If this is true then it will only add or modify the incorrect, or "
        "missing typehints. If there are no missing or incorrect typehints."
        " The rest of the code will be returned as is."
    )

    return iterate_files(args.files, signature, ["None"], description, dry_run=args.dry_run)

