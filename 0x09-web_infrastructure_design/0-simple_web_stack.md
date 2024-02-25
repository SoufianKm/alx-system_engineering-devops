##This web infrastructure design is a foundational approach to web development, representing a crucial step in my journey as a software engineer. As part of a school assignment, we're constructing a streamlined infrastructure with a single server, emphasizing simplicity and core concepts.

### Here are the key elements of our design:
1. Server: Acts as the host for the website, identified by the IP address 8.8.8.8.
2. Domain Name: Provides a user-friendly address for the website (e.g., www.foobar.com).
3. DNS Record: Maps the "www" subdomain to the root domain.
4. Web Server (Nginx): Handles HTTP requests and serves static content efficiently.
5. Application Server: Executes dynamic code for the website's functionality.
6. Application Files: Houses the codebase for the website, facilitating development and maintenance.
7. Database (MySQL): Stores and manages the website's data securely.

### Here's a breakdown of the operational flow:
1. Users access the website via www.foobar.com.
2. Their computers resolve the domain name to the server's IP address.
3. Browsers send requests to the server.
4. Nginx manages incoming requests, serving static content directly or routing dynamic requests to the application server.
5. The application server processes requests, interacting with the database as necessary.
6. Upon completion, the application server generates responses.
7. Nginx delivers responses back to users' browsers.
8. Browsers render the received web pages for users.

### Despite its simplicity, our design does face some challenges:
- Single Point of Failure (SPOF): Any server downtime renders the website inaccessible.
- Downtime During Maintenance: Scheduled maintenance activities may disrupt website availability.
- Scalability Limitations: Scaling the infrastructure to accommodate increased traffic or growth presents challenges.
