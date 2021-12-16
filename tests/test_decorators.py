import platform

import pytest

from bd103.decorators import requires_module, requires_os


class TestRequiresOs(object):
    impossible_os = ["Linux", "Windows", "Darwin"]

    try:
        impossible_os.remove(platform.system())
    except ValueError:
        print(f"{platform.system()} not in impossible_os")

    @requires_os(platform.system())
    def only_current():
        return True

    @requires_os([platform.system()])
    def only_current_list():
        return True

    @requires_os(impossible_os[0])
    def impossible_str():
        pass

    @requires_os(impossible_os)
    def impossible_list():
        pass

    @requires_os(impossible_os, silent=True)
    def silent_error():
        return True

    def test_current(self):
        assert TestRequiresOs.only_current()
        assert TestRequiresOs.only_current_list()

    def test_not_current(self):
        with pytest.raises(OSError):
            TestRequiresOs.impossible_str()

        with pytest.raises(OSError):
            TestRequiresOs.impossible_list()

    def test_silent(self):
        assert TestRequiresOs.silent_error() is None


class TestRequiresModule(object):
    @requires_module("json")
    def reqs_builtin():
        return True

    @requires_module("pytest")
    def reqs_installed():
        return True

    @requires_module("missing-pkg-name")
    def reqs_missing():
        return True

    def test_main(self):
        assert TestRequiresModule.reqs_builtin()
        assert TestRequiresModule.reqs_installed()

    def test_errors(self):
        with pytest.raises(ModuleNotFoundError):
            TestRequiresModule.reqs_missing()
