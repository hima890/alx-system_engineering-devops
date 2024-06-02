# 3. Scale up

### Overview
This README will explain the roles of application servers and web servers in a web infrastructure, along with the design of an infrastructure that includes:

- One additional server
- One load balancer (HAProxy) configured as a cluster with another load balancer
- Separate servers for each component: web server, application server, and database server
### Infrastructure Design
#### Components
1. **Load Balancers (HAProxy)**
2. **Web Server (Nginx)**
3. **Application Server (e.g., Node.js, Python, PHP)**
4. **Database Server (MySQL)**
#### Diagram
```
User
  |
  v
DNS (www.foobar.com -> Load Balancer Cluster IP)
  |
  v
Firewall
  |
  v
Load Balancer Cluster (HAProxy)
  |
  v
  -------------------
  |       |         |
  v       v         v
Firewall Firewall  Firewall
  |       |         |
  v       v         v
Web     App       Database
Server  Server    Server
(Nginx) (App)     (MySQL)
```
### Specific Components and Their Roles
1. **Load Balancers (HAProxy)**
    - **Purpose**: To distribute incoming traffic across multiple servers for load balancing and high availability.
    - **Cluster Configuration**: Ensures redundancy and failover, so if one load balancer fails, the other can continue to handle traffic.
2. **Web Server (Nginx)**
    - **Role**: 
        - Manages incoming HTTP requests.
        - Serves static content (HTML, CSS, JavaScript, images).
        - Forwards dynamic content requests to the application server.
    - **Why Add It**: Specializes in handling static content and proxies dynamic requests, improving performance and separation of concerns.
3. **Application Server**
    - **Role**: 
        - Runs the application code.
        - Processes dynamic content.
        - Handles business logic and communicates with the database.
    - **Why Add It**: Separates the processing of dynamic content from serving static files, optimizing resource usage and performance.
4. **Database Server (MySQL)**
    - **Role**: 
        - Manages data storage and retrieval.
        - Handles database queries and transactions.
    - **Why Add It**: Centralizes data management, ensuring efficient data handling and security.
### Specifics About the Infrastructure
- **Load Balancer Cluster (HAProxy)**: 
    - **Purpose**: To distribute traffic evenly across multiple servers, enhancing availability and reliability.
    - **Why Add It**: Provides fault tolerance and load distribution, ensuring high availability.
- **Splitting Components**: 
    - **Web Server**: Efficiently serves static files and handles HTTP requests.
    - **Application Server**: Dedicated to running the application code and handling dynamic content, improving performance and scalability.
    - **Database Server**: Centralizes data storage and processing, enhancing security and data management.
### Additional Elements and Their Importance
- **Firewalls**: Placed between each layer to restrict unauthorized access and provide an additional layer of security.
- **Monitoring Clients**: Collect metrics and logs from each server to ensure health and performance monitoring.
### Issues and Solutions
- **Single Points of Failure (SPOF)**:
    - **Solution**: Using a load balancer cluster and separating components across different servers mitigates the risk of a single point of failure.
- **Scalability**:
    - **Solution**: The architecture allows horizontal scaling by adding more web servers and application servers as needed.
- **Maintenance and Updates**:
    - **Solution**: Isolating components on different servers allows for maintenance and updates to be performed with minimal impact on the overall system.
### Conclusion
This infrastructure design ensures a robust, scalable, and secure setup for hosting `www.foobar.com`, with clear separation of roles and responsibilities for each component. By using load balancers, dedicated servers for each component, and clustering, the system is resilient, efficient, and prepared for high traffic and future growth.

