import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_installed(host):
    docker = host.package('docker-engine')
    assert docker.is_installed


def test_docker_service(host):
    docker = host.service('docker')
    assert docker.is_enabled
    assert docker.is_running
