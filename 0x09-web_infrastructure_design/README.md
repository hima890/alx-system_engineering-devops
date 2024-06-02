# README: Web Infrastructure Designs

This repository contains various web infrastructure designs for hosting the website www.foobar.com. Each design caters to different requirements and complexities, from a simple web stack to a secured, monitored, and scalable infrastructure.

## Table of Contents

1. [Simple Web Stack](#simple-web-stack)
2. [Distributed Web Infrastructure](#distributed-web-infrastructure)
3. [Secured and Monitored Web Infrastructure](#secured-and-monitored-web-infrastructure)
4. [Scale Up: Application Server vs. Web Server](#scale-up-application-server-vs-web-server)

---

## Simple Web Stack

**File:** [0-simple_web_stack](./0-simple_web_stack.md)

This design features a single server setup, commonly known as a LAMP stack, and is ideal for small-scale applications.

### Components:
- **1 Server**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Application Files (Code Base)**
- **1 Database (MySQL)**
- **1 Domain Name (foobar.com) configured with a `www` record pointing to IP 8.8.8.8**

### Topics Covered:
- What is a server
- Role of the domain name
- Type of DNS record for `www`
- Roles of the web server, application server, and database
- Server communication with the user's computer
- Issues: Single Point of Failure (SPOF), downtime during maintenance, and scalability limitations

---

## Distributed Web Infrastructure

**File:** [1-distributed_web_infrastructure](./1-distributed_web_infrastructure)

This design introduces a three-server setup to distribute the load and increase availability.

### Components:
- **2 Servers**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Load Balancer (HAProxy)**
- **1 Set of Application Files (Code Base)**
- **1 Database (MySQL)**

### Topics Covered:
- Purpose of each additional element
- Load balancer distribution algorithm (Round-Robin)
- Active-Active vs. Active-Passive load balancer setups
- Database Primary-Replica (Master-Slave) cluster functionality
- Differences between Primary and Replica nodes
- Issues: SPOF, security vulnerabilities, lack of monitoring

---

## Secured and Monitored Web Infrastructure

**File:** [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure)

This design builds upon the distributed infrastructure, adding security and monitoring features.

### Components:
- **3 Servers**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Load Balancer (HAProxy)**
- **3 Firewalls**
- **1 SSL Certificate for HTTPS**
- **3 Monitoring Clients (Sumologic or similar)**

### Topics Covered:
- Purpose of each additional element
- Role and importance of firewalls
- Benefits of serving traffic over HTTPS
- Monitoring tools and data collection methods
- Monitoring web server QPS (Queries Per Second)
- Issues: SSL termination at the load balancer, single MySQL server for writes, identical server components

---

## Scale Up: Application Server vs. Web Server

**File:** [3-scale_up](./3-scale_up)

This design focuses on scaling up the infrastructure by splitting the components into dedicated servers and configuring a load balancer cluster.

### Components:
- **1 Additional Server**
- **1 Load Balancer (HAProxy) configured as a cluster with another load balancer**
- **Separate servers for Web Server (Nginx), Application Server, and Database (MySQL)**

### Topics Covered:
- Purpose of each additional element
- Differences between web servers and application servers
- Load balancer clustering for high availability

---

### Repository Structure

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
- **Directory:** `0x09-web_infrastructure_design`

### How to Use

Each file in the directory contains a detailed explanation of the specific infrastructure design, including the components used, their roles, and potential issues. Navigate to the respective files for a comprehensive understanding of each setup.
