import click

data = (
    """
\033[96mBD103 Python Package

\033[34mList of Modules:\033[94m
- scripts (Module)
  + Collection of helpful functions
  + Use:
    > import bd103.scripts
    > from bd103 import scripts
- pkgdev (CLI)
  + Manage and setup Python packages
  + Use:
    > bd103-pkgdev --help
    > python -m bd103.pkgdev
"""
    + "\033[0m"
)


@click.command()
def bd103():
    "Shows information on the BD103 Package"
    print(data.strip())


if __name__ == "__main__":
    bd103()
