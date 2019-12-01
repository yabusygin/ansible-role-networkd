"""/etc/systemd/network/iface.network template tests."""

import unittest
import pathlib

from .utils import (
    relative_to_path,
    render_role_template,
    resource_abs_path,
    resource_str,
)


_ROLE_PATH = relative_to_path(
    base_path=pathlib.Path(__file__),
    relative_path=pathlib.Path(".."),
)
_TEMPLATE_FILENAME = "iface.network.j2"


class DHCPConfigured(unittest.TestCase):
    """DHCP configured host."""

    def test(self):
        """Run test."""
        expect = resource_str(
            resource_path=pathlib.Path("dhcp", "eth0.network"),
            package=__name__,
        )
        context_manager = resource_abs_path(
            resource_path=pathlib.Path("dhcp", "vars.yml"),
            package=__name__,
        )
        with context_manager as variables_path:
            actual = render_role_template(
                role_path=_ROLE_PATH,
                template_filename=_TEMPLATE_FILENAME,
                variables_path=variables_path,
            )
        self.assertEqual(expect, actual)


class Router(unittest.TestCase):
    """Router interface."""

    def test(self):
        """Run test."""
        expect = resource_str(
            resource_path=pathlib.Path("router", "eth0.network"),
            package=__name__,
        )
        context_manager = resource_abs_path(
            resource_path=pathlib.Path("router", "vars.yml"),
            package=__name__,
        )
        with context_manager as variables_path:
            actual = render_role_template(
                role_path=_ROLE_PATH,
                template_filename=_TEMPLATE_FILENAME,
                variables_path=variables_path,
            )
        self.assertEqual(expect, actual)


class MultipleAddresses(unittest.TestCase):
    """Interface with multiple addresses."""

    def test(self):
        """Run test."""
        expect = resource_str(
            resource_path=pathlib.Path("multiple-addresses", "eth0.network"),
            package=__name__,
        )
        context_manager = resource_abs_path(
            resource_path=pathlib.Path("multiple-addresses", "vars.yml"),
            package=__name__,
        )
        with context_manager as variables_path:
            actual = render_role_template(
                role_path=_ROLE_PATH,
                template_filename=_TEMPLATE_FILENAME,
                variables_path=variables_path,
            )
        self.assertEqual(expect, actual)
