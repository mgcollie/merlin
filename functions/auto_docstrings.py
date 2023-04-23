from merlin.iterate_files import iterate_files


def main(args):
    """Main entry point."""

    signature = "def auto_docstrings(code: str, style: str) -> str:"
    description = (
        "Returns the entire code with missing and or corrected docstrings based on the style provided."
        "First it tests to see if there are missing or incorrect dosctrings. "
        "If this is true then it generates the docstrings based on the style provided. "
        "If this is false then nothing happens."
    )
    return iterate_files(args.files, signature, [args.style], description, dry_run=args.dry_run)
