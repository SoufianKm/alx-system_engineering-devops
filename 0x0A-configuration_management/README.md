# Configuration management

**Overview: Puppet Configuration Management**

This project focuses on using Puppet for configuration management. Puppet is a powerful tool for automating the provisioning and management of infrastructure, enabling administrators to define infrastructure as code.

**Resources**

Read or watch:

- [Intro to Configuration Management](#)
- [Puppet resource type: file](#) (check “Resource types” for all manifest types in the left menu)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet lint](#)
- [Puppet emacs mode](#)

**Requirements**

**General**

- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

**Note on Versioning**

- Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

**Installation**

- Install puppet:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

- Puppet 5 Docs: Puppet 5 Docs
- Install puppet-lint:
```
$ gem install puppet-lint
```
