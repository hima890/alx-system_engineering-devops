# 0x0E. Web Stack Debugging #1

This project involves debugging and configuring an Nginx installation on an Ubuntu container to ensure it listens on port 80. The tasks include writing Bash scripts to automate the fixes required.

## Table of Contents

- [Tasks](#tasks)
  - [0. Nginx likes port 80](#0-nginx-likes-port-80)
  - [1. Make it sweet and short](#1-make-it-sweet-and-short)
- [Repository](#repository)

## Tasks

### 0. Nginx likes port 80

**Objective:**  
Debug and fix the Nginx installation in an Ubuntu container so that it listens on port 80.

**Requirements:**

- Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs.
- Write a Bash script (`0-nginx_likes_port_80`) to automate the configuration.

**Steps to Debug:**

1. Check the status of Nginx.
2. Verify if Nginx is listening on port 80.
3. Modify the Nginx configuration if necessary.
4. Restart Nginx to apply the changes.

**Example Usage:**

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused

root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2>&1

root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<!-- HTML content truncated for brevity -->
</html>
```

### 1. Make it sweet and short

**Objective:**  
Refactor the solution from task #0 into a concise Bash script with a maximum of 5 lines.

**Requirements:**

- The Bash script (`1-debugging_made_short`) must be 5 lines or less.
- It must include a newline at the end.
- Adhere to usual Bash script requirements.
- Avoid using `;`, `&&`, or `wget`.
- Do not execute the previous script.
- Ensure the service command indicates that Nginx is not running after execution.

**Example Usage:**

```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused

root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5

root@966c5664b21f:/# ./1-debugging_made_short

root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<!-- HTML content truncated for brevity -->
</html>

root@966c5664b21f:/# service nginx status
 * nginx is not running
```

## Repository

- **GitHub repository:** [alx-system_engineering-devops](https://github.com/hima890/alx-system_engineering-devops)
- **Directory:** `0x0E-web_stack_debugging_1`
- **Files:**
  - `0-nginx_likes_port_80`
  - `1-debugging_made_short`
