joshbenner.docker
=================
[![Build Status](https://travis-ci.org/joshbenner/docker-ansible.svg?branch=master)](https://travis-ci.org/joshbenner/docker-ansible)

Installs Docker from repositories, allowing for specific versions.

**NOTE:** This will pin the docker package version on Debian and RedHat family systems.

Example Playbook
----------------

```yaml
- name: Docker
  hosts: docker-servers
  become: yes
  roles:
    - role: joshbenner.docker
      docker_log_driver: syslog
      docker_version: 1.12*
```

Install Docker CE using docker.com repository on Ubuntu:

```yaml
- name: Docker
  hosts: docker-servers
  become: yes
  roles:
    - role: joshbenner.docker
      docker_use_docker_ce: true
      docker_version: 18.06.1*
```

Testing
-------

Uses [molecule](https://github.com/metacloud/molecule) for automated testing.

Testing requirements:
* Python
* Docker
* Install Python requirements in molecule/requirements.txt


| Command             | Description                  |
|---------------------|------------------------------|
| `molecule test`     | Run all test steps           |
| `molecule create`   | Create vagrant VM            |
| `molecule converge` | Run role against vagrant VM  |
| `molecule verify`   | Run tests against vagrant VM |
| `molecule destroy`  | Destroy vagrant VM           |
| `molecule lint`     | Lint YAML files              |

See [molecule documentation](https://molecule.readthedocs.io/en/latest/) for more information about using molecule.

License
-------

BSD
