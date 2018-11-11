import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service(host):
    docker = host.service('docker')
    assert docker.is_enabled
    assert docker.is_running


def test_docker_config(host):
    file = host.file('/etc/docker/daemon.json')
    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o600
    assert file.contains('syslog')
