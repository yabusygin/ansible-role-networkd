"""Test role."""

import os
import textwrap

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("gateway")


def test_network_files(host):
    """Test /etc/systemd/network/ files content."""
    actual = host.file("/etc/systemd/network/eth0.network").content_string
    expect = textwrap.dedent(
        """\
        [Match]
        Name=eth0

        [Network]
        DHCP=ipv4
        IPForward=ipv4
        """,
    )
    assert actual == expect

    actual = host.file("/etc/systemd/network/eth1.network").content_string
    expect = textwrap.dedent(
        """\
        [Match]
        Name=eth1

        [Address]
        Address=192.168.0.1/24

        [Network]
        IPForward=ipv4
        """,
    )
    assert actual == expect

    actual = host.file("/etc/systemd/network/eth2.network").content_string
    expect = textwrap.dedent(
        """\
        [Match]
        Name=eth2

        [Address]
        Address=10.0.0.1/24

        [Network]
        IPForward=ipv4
        """,
    )
    assert actual == expect
