from pathlib import Path


VERSION_FILE = Path("data/kb_version.txt")


def get_kb_version():

    if not VERSION_FILE.exists():

        VERSION_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        VERSION_FILE.write_text("0")

    return int(
        VERSION_FILE.read_text().strip()
    )


def increment_kb_version():

    current_version = get_kb_version()

    new_version = current_version + 1

    VERSION_FILE.write_text(
        str(new_version)
    )

    return new_version