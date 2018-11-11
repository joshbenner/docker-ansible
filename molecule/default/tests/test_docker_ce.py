import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('docker-ce')


def test_docker_engine_installed(host):
    assert host.package('docker-ce').is_installed


def test_docker_engine_version(host):
    assert host.package('docker-ce').version.startswith('18.06')
