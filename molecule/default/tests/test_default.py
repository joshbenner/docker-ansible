import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    assert host.package('docker-engine').is_installed


def test_docker_service(host):
    docker = host.service('docker')
    assert docker.is_enabled
    assert docker.is_running
