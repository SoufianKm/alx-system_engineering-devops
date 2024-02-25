### Infrastructure Specifics:

- **Element Addition Justification**: Each additional element is added to enhance the infrastructure's reliability, performance, and security. For example, adding a load balancer improves scalability by distributing traffic across multiple servers.
- **Load Balancer Algorithm**: The load balancer is configured with a Round Robin distribution algorithm, which evenly distributes incoming requests among available servers.
- **Active-Active vs. Active-Passive Setup**: The load balancer enables an Active-Active setup, where all servers actively handle requests simultaneously. In contrast, Active-Passive setup involves one set of servers actively serving traffic while the other set remains on standby for failover.
- **Database Primary-Replica Cluster**: In a Primary-Replica (Master-Slave) cluster, the Primary node handles write operations, while the Replica nodes replicate data from the Primary and serve read requests.
- **Primary vs. Replica Node**: The Primary node is responsible for processing write operations and maintaining the authoritative dataset. Replica nodes replicate data from the Primary node and handle read requests, providing fault tolerance and scalability.

### Issues with the Infrastructure:

- **Single Points of Failure (SPOF)**: Potential SPOFs include the absence of redundancy in critical components such as the load balancer and database servers.
- **Security Issues**: Lack of firewall protection and HTTPS encryption exposes the infrastructure to security vulnerabilities, increasing the risk of unauthorized access and data breaches.
- **Monitoring Absence**: Without proper monitoring tools and processes in place, detecting and addressing performance issues or system failures becomes challenging, leading to potential downtime and degraded user experience.
