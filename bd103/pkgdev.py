import os
import subprocess
import sys

import click


# Thank you: https://stackoverflow.com/a/27496113
def get_installed():
    reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
    installed_pkgs = []
    for r in reqs.split():
        installed_pkgs.append(r.decode().split("==")[0])
    return installed_pkgs


@click.group()
def cli():
    pass


@cli.command()
@click.option("--poetry/--pip", default=True, help="Use Poetry or just PIP")
@click.option("--no-black", "-nb", is_flag=True, help="Disables adding Black formatter")
@click.option("--no-pytest", "-nt", is_flag=True, help="Disables adding Pytest")
@click.option("--upgrade", "-U", is_flag=True, help="Upgrade packages if using PIP")
def add_deps(poetry, no_black, no_pytest, upgrade):
    "Adds common dependencies to project, either Poetry or PIP"
    pkgs = ["isort", "flake8"]
    if not no_black:
        pkgs.append("black")
    if not no_pytest:
        pkgs.append("pytest")
    if poetry:
        if os.path.isfile("pyproject.toml"):
            for i in pkgs:
                subprocess.run(["poetry", "add", "-D", i])
        else:
            raise FileNotFoundError("pyproject.toml does not exist", 1)
    else:
        if upgrade:
            pkgs.insert(0, "pip")
            for i in pkgs:
                subprocess.run(["pip", "install", "-U", "-q", i])
        else:
            for i in pkgs:
                subprocess.run(["pip", "install", "-q", i])


@cli.command()
def clean():
    "Cleans up the project with Isort and Black if installed"
    installed_pkgs = get_installed()
    if "black" in installed_pkgs:
        subprocess.run(["black", "."])
    if "isort" in installed_pkgs:
        subprocess.run(["isort", ".", "--profile", "black"])


@cli.command()
def test():
    "Tests a project with Pytest and Flake8"
    installed_pkgs = get_installed()
    if "pytest" in installed_pkgs:
        subprocess.run(["pytest"])
    if "flake8" in installed_pkgs:
        subprocess.run(["flake8"])


if __name__ == "__main__":
    cli()
