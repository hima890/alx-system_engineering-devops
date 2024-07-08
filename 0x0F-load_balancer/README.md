### Tasks Overview and Setup Guide

This repository contains solutions for configuring web servers and load balancers using Nginx, HAProxy, and Puppet. Below are detailed instructions and examples for each task.

---

### Task 0: Double the number of webservers

#### Requirements:
- Configure web-02 identical to web-01 using automation.
- Configure Nginx to include a custom HTTP header (`X-Served-By`) with the server's hostname.

#### Steps:
1. **Configure Web Servers**:
   - Use a Bash script to automate the configuration of `web-02` to match `web-01`.

2. **Custom HTTP Header**:
   - Modify Nginx configuration to include `X-Served-By` header with the server's hostname.

#### Example:
```bash
$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
```

### Files:
- **0-custom_http_response_header**: Bash script to configure Nginx on Ubuntu with the custom HTTP header.

---

### Task 1: Install your load balancer

#### Requirements:
- Install and configure HAProxy (`lb-01`) to distribute traffic between `web-01` and `web-02`.
- Use round-robin algorithm for load distribution.
- Ensure HAProxy can be managed via an init script.
- Ensure servers are configured with hostnames `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.

#### Steps:
1. **HAProxy Configuration**:
   - Configure HAProxy to forward traffic to both web servers using round-robin.

2. **Server Configuration**:
   - Ensure servers have correct hostnames for proper HAProxy configuration.

#### Example:
```bash
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
X-Served-By: 03-web-01
```

### Files:
- **1-install_load_balancer**: Bash script to install and configure HAProxy on Ubuntu.

---

### Task 2: Add a custom HTTP header with Puppet

#### Requirements:
- Automate the configuration of a custom HTTP header (`X-Served-By`) using Puppet.
- Ensure Puppet configures a new Ubuntu machine to include the server's hostname in the HTTP response header.

#### Steps:
1. **Puppet Manifest**:
   - Create `2-puppet_custom_http_response_header.pp` to configure Nginx with the custom header.

#### Example:
```bash
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
X-Served-By: 03-web-02
```

### Files:
- **2-puppet_custom_http_response_header.pp**: Puppet manifest to automate setting up the custom HTTP header on Ubuntu.

---

### Repository Information:

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- **Directory**: 0x0F-load_balancer
- **Files**:
  - `0-custom_http_response_header`
  - `1-install_load_balancer`
  - `2-puppet_custom_http_response_header.pp`
