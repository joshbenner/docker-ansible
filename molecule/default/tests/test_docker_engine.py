import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('docker-engine')


def test_docker_engine_installed(host):
    assert host.package('docker-engine').is_installed


def test_docker_engine_version(host):
    assert host.package('docker-engine').version.startswith('1.12')
