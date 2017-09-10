docker
======
[![Build Status](https://travis-ci.org/joshbenner/docker-ansible.svg?branch=master)](https://travis-ci.org/joshbenner/docker-ansible)

Installs Docker Engine from repositories, allowing for specific versions.

Testing
-------

Uses [molecule](https://github.com/metacloud/molecule) for automated testing.

Testing requirements:
* [molecule](https://github.com/metacloud/molecule)
* docker
* docker-py


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
