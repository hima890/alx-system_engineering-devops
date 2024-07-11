# HAProxy Configuration for HTTPS and HTTP to HTTPS Redirection

This repository contains configurations and setup instructions for configuring HAProxy to handle HTTPS traffic, terminate SSL, and enforce HTTP to HTTPS redirection.

## HAProxy Configuration Files

### `haproxy.cfg`

The `haproxy.cfg` file located in `/etc/haproxy/haproxy.cfg` contains the main configuration for HAProxy. Below are the key configurations:

#### Global Settings

- Logging configuration (`log /dev/log local0`, `log /dev/log local1 notice`)
- User and group settings (`user haproxy`, `group haproxy`)
- Daemon mode (`daemon`)

#### Default Settings

- Timeout settings for various connections (`timeout connect`, `timeout client`, `timeout server`)
- Error file configurations (`errorfile` directives for various HTTP error codes)

#### Frontend Configuration for HTTP and HTTPS Traffic

```plaintext
frontend http_front
    bind *:80
    mode http
    option forwardfor
    redirect scheme https code 301 if !{ ssl_fc }
```

- Binds to port 80 and listens for HTTP traffic.
- Redirects HTTP requests to HTTPS using a 301 status code (`Moved Permanently`).

#### Frontend Configuration for HTTPS Traffic

```plaintext
frontend https_front
    bind *:443 ssl crt /etc/letsencrypt/live/www.ibrahimhanafideveloper.tech/fullchain.pem
    http-request add-header X-Forwarded-Proto https
    default_backend http_back
```

- Binds to port 443 and listens for HTTPS traffic.
- Performs SSL termination with certificates located at `/etc/letsencrypt/live/www.ibrahimhanafideveloper.tech/fullchain.pem`.
- Adds `X-Forwarded-Proto` header for backend servers to identify HTTPS traffic.
- Routes traffic to the `http_back` backend.

#### Backend Configuration

```plaintext
backend http_back
    balance roundrobin
    server web01 35.175.102.190:80 check
    server web02 3.89.146.68:80 check
```

- Defines backend servers (`web01` and `web02`) that handle HTTP requests.

#### Optional: Stats Configuration

```plaintext
listen stats
    bind *:8080
    mode http
    stats enable
    stats uri /stats
    stats hide-version
    stats auth admin:password
```

- Provides HAProxy statistics and monitoring on port 8080.

### `100-redirect_http_to_https`

This file represents the specific configuration file (`/etc/haproxy/haproxy.cfg`) focusing on redirecting HTTP traffic to HTTPS.

## SSL Certificate

The SSL certificate used for HTTPS configuration is obtained from Let's Encrypt. The certificate and private key files are located at:

- `/etc/letsencrypt/live/www.ibrahimhanafideveloper.tech/fullchain.pem`
- `/etc/letsencrypt/live/www.ibrahimhanafideveloper.tech/privkey.pem`

### Certificate Renewal

To renew the SSL certificate in the future, run the following command:

```bash
certbot renew
```

### Additional Notes

Ensure proper permissions and configuration adjustments are made based on your specific environment and requirements.
