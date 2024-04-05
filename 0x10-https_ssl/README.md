# SSL Overview

## Overview

HTTPS (Hypertext Transfer Protocol Secure) and SSL (Secure Sockets Layer) are fundamental components of modern web security, providing encryption and authentication mechanisms to ensure secure communication between clients and servers.


## Resources

### Read or watch:

- [What is HTTPS?](https://en.wikipedia.org/wiki/HTTPS)
- [What are the 2 main elements that SSL is providing](https://www.ssl.com/faqs/what-are-the-two-main-elements-that-ssl-is-providing/)
- [HAProxy SSL termination on Ubuntu16.04](https://serversforhackers.com/c/letsencrypt-with-haproxy)
- [SSL termination](https://www.nginx.com/resources/glossary/ssl-termination/)
- [Bash function](https://www.tutorialspoint.com/unix/unix-functions.htm)

### man or help:

- [awk](https://linux.die.net/man/1/awk)
- [dig](https://linux.die.net/man/1/dig)

## General

### What is HTTPS SSL's Two Main Roles?

HTTPS SSL primarily serves two main roles:

1. **Encryption**: SSL ensures that the data exchanged between the client (e.g., web browser) and the server is encrypted, making it extremely difficult for unauthorized parties to intercept and decipher the transmitted information.
   
2. **Authentication**: SSL provides a mechanism for verifying the identity of the server, assuring the client that they are communicating with the intended and legitimate server, not an imposter.

### What Is the Purpose of Encrypting Traffic?

Encrypting traffic serves the fundamental purpose of protecting sensitive information from unauthorized access and interception during transmission over the internet. This includes personal data, login credentials, financial information, and any other sensitive data exchanged between users and servers.

### What Does SSL Termination Mean?

SSL termination refers to the process of decrypting SSL-encrypted traffic at a load balancer or proxy server before forwarding it to the backend servers. This allows the load balancer or proxy server to inspect, route, or manipulate the unencrypted traffic based on certain criteria (e.g., HTTP headers, URL paths) before re-encrypting it for onward transmission to the client.

By terminating SSL at the load balancer or proxy server, backend servers are relieved from the resource-intensive task of SSL decryption, resulting in improved performance and scalability of the overall system.


