# 2. Secured and monitored web infrastructure

### Secured and Monitored Web Infrastructure Design
### Infrastructure Components
1. **Load Balancer**: Handles incoming traffic and distributes it among the web servers.
2. **Two Web Servers**: Serve the website content and application logic.
3. **One Database Server**: Hosts the MySQL database.
### Security and Monitoring Additions
1. **Firewalls**: To protect each layer of the infrastructure.
2. **SSL Certificate**: For encrypted HTTPS traffic.
3. **Monitoring Clients**: Installed on each server to collect and send data to a monitoring service like Sumologic.
### Detailed Design
#### 1. User Request Flow
1. **User Request**: The user wants to access `www.foobar.com` .
2. **DNS Resolution**: The domain `www.foobar.com`  points to the public IP of the load balancer.
3. **Load Balancer**: The load balancer, configured with an SSL certificate, terminates the SSL connection and forwards the request to one of the web servers.
#### 2. Servers
1. **Load Balancer**: 
    - **Role**: Distributes incoming traffic to web servers and terminates SSL.
    - **Firewall**: Protects against unauthorized access, allowing only HTTP/HTTPS traffic.
    - **Monitoring Client**: Collects metrics and logs.
2. **Web Servers**:
    - **Role**: Handle application logic and serve content.
    - **Firewall**: Restricts access to necessary ports (e.g., port 80 for HTTP, port 443 for HTTPS, and internal ports for communication with the database).
    - **Monitoring Client**: Collects metrics, logs, and application performance data.
3. **Database Server**:
    - **Role**: Manages the MySQL database.
    - **Firewall**: Restricts access to the database port (3306), allowing only internal communication from web servers.
    - **Monitoring Client**: Monitors database performance, query execution, and health metrics.
### Infrastructure Diagram
```
User
  |
  v
DNS (www.foobar.com -> Load Balancer IP)
  |
  v
Firewall
  |
  v
Load Balancer (SSL Termination, Traffic Distribution)
  |
  v
  -----------------
  |               |
  v               v
Firewall        Firewall
  |               |
  v               v
Web Server 1     Web Server 2 (Application Logic, Static Content)
  |               |
  v               v
Firewall        Firewall
  |               |
  v               v
Database Server (MySQL)
```
### Specifics
1. **Firewalls**: Protect each layer (load balancer, web servers, database) by filtering traffic and preventing unauthorized access.
2. **SSL Certificate**: Ensures that all traffic between users and the website is encrypted, enhancing security and user trust.
3. **Monitoring Clients**: Collect performance metrics, logs, and other data for proactive monitoring and troubleshooting.
#### Roles
- **Firewalls**: Provide security by controlling incoming and outgoing traffic based on predetermined security rules.
- **HTTPS (SSL/TLS)**: Encrypts traffic between the user's browser and the server to protect data integrity and confidentiality.
- **Monitoring**: Allows tracking of server health, performance metrics, and alerts for issues.
    - **Data Collection**: Monitoring clients (e.g., agents) on each server collect and send data to a centralized monitoring service.
### Monitoring QPS (Queries Per Second)
1. **Web Server Monitoring**: Use monitoring tools (like Sumologic, Prometheus) to collect metrics on HTTP requests.
2. **Metrics Collection**: Configure the monitoring client to gather web server logs and extract QPS data.
3. **Visualization and Alerts**: Use the monitoring service's dashboard to visualize QPS and set up alerts for unusual traffic patterns.
### Issues with this Infrastructure
1. **SSL Termination at the Load Balancer**:
    - **Issue**: SSL termination at the load balancer means internal traffic between the load balancer and web servers is unencrypted, which can be a security concern.
    - **Solution**: Use end-to-end encryption by configuring SSL on both the load balancer and web servers.
2. **Single MySQL Server for Writes**:
    - **Issue**: A single MySQL server is a single point of failure and can become a bottleneck.
    - **Solution**: Implement database replication with a master-slave setup or use a distributed database system.
3. **Identical Servers for All Components**:
    - **Issue**: Combining all components (web server, application server, database) on each server can lead to resource contention and complex failure scenarios.
    - **Solution**: Separate concerns by dedicating servers for specific roles, enabling easier scaling and maintenance.
### Enhanced Security and Scalability
For better security and scalability, consider:

- **Using a Web Application Firewall (WAF)**: To protect against common web exploits.
- **Database Clustering**: To ensure high availability and redundancy.
- **Horizontal Scaling**: Adding more web servers and load balancers as traffic grows.
This design ensures a secure, scalable, and monitored web infrastructure for `www.foobar.com`.

