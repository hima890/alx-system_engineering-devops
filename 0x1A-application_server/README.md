Here’s a sample `README.md` file that you can use for the tasks related to serving the AirBnB Clone using Gunicorn and Nginx:

```markdown
# AirBnB Clone - Web Dynamic with Gunicorn and Nginx

This project involves deploying the dynamic version of the AirBnB clone using Gunicorn as a WSGI server and Nginx as a reverse proxy. The web application is built using Flask, and it serves both dynamic and static content.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [Cloning the Repository](#cloning-the-repository)
  - [Gunicorn Configuration](#gunicorn-configuration)
  - [Nginx Configuration](#nginx-configuration)
  - [Testing](#testing)
- [Files and Directories](#files-and-directories)
- [Authors](#authors)

## Project Overview

The goal of this project is to serve a dynamic version of the AirBnB clone using the following setup:

- Gunicorn serves the Flask application.
- Nginx acts as a reverse proxy, handling client requests and forwarding them to Gunicorn.
- Nginx also serves static files directly to the client.

### Tasks Implemented

1. **Serve AirBnB Clone - RESTful API**:  
   - **Gunicorn** serves content from `api/v1/app.py` on port `5002`.
   - **Nginx** is configured to route `/api/` to Gunicorn and serve the API both locally and publicly on port `80`.

2. **Serve AirBnB Clone - Web Dynamic**:  
   - **Gunicorn** serves content from `web_dynamic/2-hbnb.py` on port `5003`.
   - **Nginx** routes `/` to Gunicorn and serves the page on port `80`.
   - Static assets in `web_dynamic/static/` are served directly by Nginx.

## Requirements

- **Python 3.6+**
- **Flask**
- **Gunicorn**
- **Nginx**
- **Git**

## Setup Instructions

### Cloning the Repository

```bash
git clone https://github.com/yourusername/AirBnB_clone_v4.git
cd AirBnB_clone_v4
```

### Gunicorn Configuration

1. **Start Gunicorn for the API:**

    ```bash
    gunicorn --bind 0.0.0.0:5002 api.v1.app:app
    ```

2. **Start Gunicorn for the Web Dynamic:**

    ```bash
    gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app
    ```

### Nginx Configuration

1. **Create an Nginx configuration file:**

    ```bash
    sudo nano /etc/nginx/sites-available/airbnb_clone
    ```

2. **Add the following configuration:**

    ```nginx
    server {
        listen 80;
        server_name your_server_ip;

        location /api/ {
            proxy_pass http://127.0.0.1:5002;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location / {
            proxy_pass http://127.0.0.1:5003;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias /path/to/AirBnB_clone_v4/web_dynamic/static/;
        }
    }
    ```

3. **Enable the configuration and restart Nginx:**

    ```bash
    sudo ln -s /etc/nginx/sites-available/airbnb_clone /etc/nginx/sites-enabled/
    sudo service nginx restart
    ```

### Testing

1. **Local Testing:**

    Test the API and dynamic web content locally:

    ```bash
    curl 127.0.0.1:5002/api/v1/states
    curl 127.0.0.1:5003/
    ```

2. **Public Testing:**

    Test the API and dynamic web content from another machine:

    ```bash
    curl http://your_server_ip/api/v1/states
    curl http://your_server_ip/
    ```

## Files and Directories

- **`api/v1/app.py`**: Main entry point for the RESTful API.
- **`web_dynamic/2-hbnb.py`**: Main entry point for the dynamic web application.
- **`web_dynamic/static/`**: Directory containing static assets (CSS, JS, images).
- **`5-app_server-nginx_config`**: Nginx configuration file used in the project.

## Authors

- **Your Name** - [GitHub Profile](https://github.com/hima890)

```

Replace `"yourusername"` and `"your_server_ip"` with your actual GitHub username and server IP address.

This README provides a clear overview and instructions for anyone looking to replicate your setup.
