# Load Balancer

## Overview

In this project, you will enhance the redundancy and scalability of our web stack by implementing a load balancer. This load balancer will distribute incoming traffic across multiple web servers, ensuring high availability and improved performance. Additionally, you will automate the configuration of new Ubuntu servers to match the project requirements using Bash scripts.

## Background Context

As part of this project, you have been provided with two additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

The goal is to enhance the web stack with redundancy for web servers, enabling us to handle more traffic by doubling the number of web servers and improving infrastructure reliability. With this setup, if one web server fails, the load balancer will automatically redirect traffic to the remaining active servers.

## Resources

Read or watch:

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)
- [HAProxy Documentation](https://www.haproxy.org/documentation/)

## Requirements

General requirements for the project include:

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- Mandatory README.md file at the root of the project folder
- All Bash script files must be executable
- Scripts must pass Shellcheck (version 0.3.7) without any error
- First line of all Bash scripts should be #!/usr/bin/env bash
- Second line should be a comment explaining the script's purpose
