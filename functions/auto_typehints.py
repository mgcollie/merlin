from merlin.iterate_files import iterate_files


def main(args):
    """Main entry point."""

    signature = "def auto_typehints(code: str) -> str:"
    description = (
        "Returns the entire code with missing and or typehints "
        "added, including required import statements."
    )

    return iterate_files(args.files, signature, ["None"], description, dry_run=args.dry_run)
