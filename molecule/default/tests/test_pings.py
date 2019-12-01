"""Test role."""

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_ping_hosts(host):
    """Ping hosts."""
    host.run_expect(expected=[0], command="ping -c 3 192.168.0.10")
    host.run_expect(expected=[0], command="ping -c 3 192.168.0.1")
    host.run_expect(expected=[0], command="ping -c 3 10.0.0.1")
    host.run_expect(expected=[0], command="ping -c 3 10.0.0.10")
    host.run_expect(expected=[0], command="ping -c 3 10.0.0.20")
