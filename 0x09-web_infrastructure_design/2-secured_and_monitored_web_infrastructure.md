### Infrastructure Specifics:

- **Element Addition Justification**: Each additional element is introduced to bolster the infrastructure's robustness, scalability, and security. For instance, incorporating a firewall helps control and filter incoming and outgoing traffic, enhancing network security.
- **Firewalls Purpose**: Firewalls act as a barrier between a trusted internal network and untrusted external networks, regulating traffic based on predefined security rules to prevent unauthorized access and protect against malicious threats.
- **HTTPS Traffic**: Serving traffic over HTTPS encrypts data exchanged between the user's browser and the server, ensuring confidentiality, integrity, and authenticity, thereby safeguarding sensitive information from eavesdropping and tampering.
- **Monitoring Importance**: Monitoring serves to track and analyze system performance, availability, and health in real-time, enabling proactive identification and resolution of issues, optimizing resource utilization, and enhancing user experience.
- **Monitoring Data Collection**: The monitoring tool gathers data through various metrics and sensors deployed across the infrastructure, continuously collecting and aggregating information on system metrics, application performance, network traffic, and user interactions.
- **Web Server QPS Monitoring**: To monitor web server queries per second (QPS), one can utilize monitoring tools like Prometheus or New Relic, which offer specialized metrics and dashboards for tracking and analyzing web server performance. This involves configuring appropriate metrics and alerts to monitor QPS trends and identify potential bottlenecks or issues.

### Issues with the Infrastructure:

- **SSL Termination at Load Balancer Level**: Terminating SSL at the load balancer exposes decrypted data within the internal network, potentially compromising data confidentiality and integrity, especially if proper security measures are not implemented.
- **Single MySQL Server for Writes**: Relying on a single MySQL server for write operations poses a single point of failure (SPOF), as any downtime or failure of the server can lead to data unavailability and service disruption.
- **Uniform Component Deployment**: Deploying servers with identical components across the board increases the risk of systemic failures or vulnerabilities affecting all instances simultaneously, limiting fault tolerance and resilience. This lack of diversity in infrastructure components may hinder fault isolation and recovery efforts in case of issues.
