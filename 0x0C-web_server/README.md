![Web Server Configuration](what-is-nginx-1024x512.png)

# Web Server Configuration Tasks

This repository contains several tasks aimed at configuring a web server using both Bash and Puppet scripts. Below are brief descriptions of each task, along with instructions on how to use the corresponding files.

## 0. Transfer a file to your server

### File
- `0-transfer_file`

### Description
A Bash script that transfers a file from the client to a server using SCP.

### Usage
```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```
Example:
```bash
./0-transfer_file some_page.html 8.8.8.8 user /path/to/private_key
```
This script will transfer `some_page.html` to the home directory of the user on the server with IP `8.8.8.8`.

## 1. Install nginx web server

### File
- `1-install_nginx_web_server`

### Description
A Bash script to install and configure Nginx on an Ubuntu server. It ensures Nginx listens on port 80 and serves a "Hello World!" page at the root URL.

### Usage
```bash
sudo ./1-install_nginx_web_server
```
Run this script on your Ubuntu server to install Nginx and set up the "Hello World!" page.

## 2. Setup a domain name

### File
- `2-setup_a_domain_name`

### Description
Contains the registered .tech domain name that points to your web server's IP address.

### Usage
The file should contain only the domain name. Example:
```
myschool.tech
```
Register a .tech domain and configure DNS records to point to your server's IP address. Verify the setup using `dig` or similar tools.

## 3. Redirection

### File
- `3-redirection`

### Description
A Bash script to configure Nginx to redirect requests from `/redirect_me` to another URL with a 301 status code.

### Usage
```bash
sudo ./3-redirection
```
Run this script on your Ubuntu server to configure the redirection. Verify by running:
```bash
curl -I http://your_server_ip/redirect_me
```
This should return a `301 Moved Permanently` status with the correct redirection URL.

## 4. Not found page 404

### File
- `4-not_found_page_404`

### Description
A Bash script to configure Nginx to serve a custom 404 page containing the string "Ceci n'est pas une page".

### Usage
```bash
sudo ./4-not_found_page_404
```
Run this script on your Ubuntu server to set up the custom 404 page. Verify by running:
```bash
curl http://your_server_ip/nonexistent_page
```
This should return a `404 Not Found` status with the custom message.

## 5. Install Nginx web server (w/ Puppet)

### File
- `7-puppet_install_nginx_web_server.pp`

### Description
A Puppet manifest to install and configure Nginx. It ensures Nginx listens on port 80, serves a "Hello World!" page at the root URL, and redirects requests from `/redirect_me` to another URL with a 301 status code.

### Usage
```bash
sudo puppet apply 7-puppet_install_nginx_web_server.pp
```
Run this command on your Ubuntu server to apply the Puppet manifest. Verify by running:
```bash
curl http://your_server_ip/
```
This should return the "Hello World!" page.

For the redirection, run:
```bash
curl -I http://your_server_ip/redirect_me
```
This should return a `301 Moved Permanently` status with the correct redirection URL.
