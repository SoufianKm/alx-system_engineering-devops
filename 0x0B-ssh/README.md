# SSH Overview

SSH, or Secure Shell, is a cryptographic network protocol used for secure communication between two networked devices. It provides a secure channel over an unsecured network by encrypting the data transmitted between the client and the server.

## Resources

### Read or watch:

- [What is a (physical) server - text](#)
- [What is a (physical) server - video](#)
- [SSH essentials](#)
- [SSH Config File](#)
- [Public Key Authentication for SSH](#)
- [How Secure Shell Works](#)
- [SSH Crash Course](#) (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

### For reference:

- [Understanding the SSH Encryption and Connection Process](#)
- [Secure Shell Wiki](#)
- [IETF RFC 4251](#) (Description of the SSH Protocol)
- [Internet Engineering Task Force](#)
- [Request for Comments](#)

### `man` or `help`:

- `ssh`
- `ssh-keygen`
- `env`

## General

- **What is a server:** A server is a computer program or device that provides functionality to other programs or devices, known as clients, over a network.
- **Where servers usually live:** Servers are typically hosted in data centers or server rooms with controlled environmental conditions and redundant power supplies.
- **What is SSH:** SSH is a cryptographic network protocol for operating network services securely over an unsecured network.
- **How to create an SSH RSA key pair:** Use `ssh-keygen` to generate an RSA key pair, which consists of a public key and a private key.
- **How to connect to a remote host using an SSH RSA key pair:** Use the `ssh` command along with the generated SSH key pair to authenticate and securely connect to a remote server.
- **The advantage of using #!/usr/bin/env bash instead of /bin/bash:** Using `#!/usr/bin/env bash` allows for better portability across different systems by using the `env` command to locate the Bash interpreter in the system's PATH.
