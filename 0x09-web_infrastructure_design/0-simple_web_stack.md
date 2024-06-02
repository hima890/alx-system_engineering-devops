# 0-simple_web_stack

### Basic Web Infrastructure Design

1. **User Request**: A user wants to access the website `www.foobar.com` .
2. **Domain Name**: The domain name `foobar.com`  is configured with a `www`  record (a CNAME or A record) that points to the server's IP address `8.8.8.8` .
3. **Server**: This is a single server that hosts all components needed for the website. For our purposes, we'll assume it has sufficient resources (CPU, RAM, storage) to run everything smoothly.
### Components on the Server
1. **Web Server (Nginx)**: 
    - **Role**: The web server is responsible for handling HTTP requests from users' browsers, serving static files (like HTML, CSS, JavaScript, images), and passing dynamic requests to the application server.
    - **Configuration**: Nginx listens on port 80 (HTTP) and optionally port 443 (HTTPS).
2. **Application Server**:
    - **Role**: The application server runs the code base (e.g., a PHP, Python, Node.js, or Java application) and processes dynamic content. It communicates with the web server via FastCGI, WSGI, or similar protocols.
    - **Configuration**: Typically, it listens on an internal port (e.g., 8000) and is not directly exposed to the internet.
3. **Code Base**:
    - **Role**: This is your application code (e.g., a PHP application) that handles business logic, interacts with the database, and generates dynamic content.
4. **Database (MySQL)**:
    - **Role**: The database stores and retrieves data for the application. It handles queries, updates, and ensures data integrity.
    - **Configuration**: MySQL listens on port 3306, but access is restricted to the local server or specific IPs for security.
### Network Flow
1. **DNS Resolution**:
    - The user types `www.foobar.com`  in their browser.
    - The browser queries DNS to resolve `www.foobar.com`  to `8.8.8.8` .
2. **HTTP Request**:
    - The browser sends an HTTP request to `8.8.8.8` .
    - Nginx receives the request and checks if it's for a static file. If not, it forwards the request to the application server.
3. **Application Processing**:
    - The application server processes the request, interacts with the MySQL database if necessary, and generates a response.
4. **Response Delivery**:
    - The application server sends the response back to Nginx.
    - Nginx forwards the response to the user's browser.
### Specifics
- **Server**: A physical or virtual machine with an OS (e.g., Ubuntu) that hosts all components.
- **Domain Name**: `foobar.com`  is a human-readable address that maps to the server's IP.
- **DNS Record**: `www`  is a CNAME or A record pointing to `8.8.8.8` .
- **Web Server (Nginx)**: Manages HTTP requests, serves static files, and proxies requests to the application server.
- **Application Server**: Runs the business logic and processes dynamic requests.
- **Database (MySQL)**: Manages data storage and retrieval.
- **Communication Protocol**: HTTP/HTTPS is used between the user's browser and Nginx. Internal communication between Nginx and the application server can be through FastCGI, WSGI, etc.
### Issues with this Infrastructure
1. **Single Point of Failure (SPOF)**: If the server fails, the website becomes unavailable.
2. **Downtime for Maintenance**: Restarting Nginx or deploying new code requires taking the server offline, leading to downtime.
3. **Scalability**: A single server can't handle high traffic volumes. As traffic increases, performance degrades.
### Diagram
I can't draw on a whiteboard here, but imagine this flow visually:

```
User -> DNS (www.foobar.com -> 8.8.8.8) -> Nginx (Web Server)
-> Application Server (Processes Request)
-> MySQL (Database) <- Application Server
```


