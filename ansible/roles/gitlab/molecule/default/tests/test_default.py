import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_epel_repo(host):
    f = host.file('/etc/yum.repos.d/epel.repo')
    assert f.exists


def test_requirement_packages_is_installed(host):
    device_mapper = host.package("device-mapper-persistent-data")
    lvm2 = host.package("lvm2")
    pip = host.package("python-pip")
    assert device_mapper.is_installed
    assert lvm2.is_installed
    assert pip.is_installed


def test_docker_is_installed(host):
    docker = host.package('docker-ce')
    docker_cli = host.package('docker-ce-cli')
    containerd = host.package('containerd.io')
    assert docker.is_installed
    assert docker_cli.is_installed
    assert containerd.is_installed


def test_docker_service_is_enabled_and_running(host):
    docker = host.service("docker")
    assert docker.is_enabled
    assert docker.is_running


def test_docker_compose_packege_is_installed(host):
    pip_packages = [package.lower() for package in dict(host.pip_package.get_packages()).keys()]
    assert 'docker-compose' in pip_packages
    assert 'docker' in pip_packages
    assert 'pyyaml' in pip_packages


def test_gitlab_dirs_is_exists(host):
    gitlab_config = host.file('/srv/gitlab/config')
    gitlab_data = host.file('/srv/gitlab/data')
    gitlab_logs = host.file('/srv/gitlab/logs')
    assert gitlab_config.exists
    assert gitlab_data.exists
    assert gitlab_logs.exists
    assert gitlab_config.is_directory
    assert gitlab_data.is_directory
    assert gitlab_logs.is_directory


def test_gitlab_docker_compose_is_exists(host):
    gitlab_docker_compose = host.file('/srv/gitlab/docker-compose.yaml')
    assert gitlab_docker_compose.exists


def test_gitlab_container_is_running(host):
    gitlab_container = host.docker('gitlab_web_1')
    assert gitlab_container.is_running


def test_gitlab_ports_is_listening(host):
    gitlab_http_port = host.socket('tcp://0.0.0.0:80')
    gitlab_https_port = host.socket('tcp://0.0.0.0:443')
    assert gitlab_http_port.is_listening
    assert gitlab_https_port.is_listening
