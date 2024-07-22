# Firewall Configuration and Network Tools Setup

## Overview

This repository contains the configuration steps and scripts for setting up firewall rules and network tools on an Ubuntu system. The tasks include configuring the UFW firewall, redirecting ports using iptables, and installing necessary network tools.

## Firewall Configuration

### UFW Setup

1. **Install UFW (if not already installed):**

    ```bash
    sudo apt-get update
    sudo apt-get install ufw
    ```

2. **Configure UFW Rules:**

    - Allow incoming traffic on ports 22 (SSH), 443 (HTTPS), and 80 (HTTP).
    - Block all other incoming traffic.

    ```bash
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow 22/tcp
    sudo ufw allow 443/tcp
    sudo ufw allow 80/tcp
    ```

3. **Enable UFW:**

    ```bash
    sudo ufw enable
    ```

### iptables Port Redirection

1. **Add a rule to redirect incoming traffic from port 8080 to port 80:**

    ```bash
    sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
    ```

2. **Save iptables Rules:**

    - To ensure the rules persist across reboots:

      ```bash
      sudo iptables-save > /etc/iptables/rules.v4
      ```

## Network Tools

### Install `netstat`

1. **Install the `net-tools` package:**

    ```bash
    sudo apt-get update
    sudo apt-get install net-tools
    ```

2. **Verify Installation:**

    ```bash
    netstat --version
    ```

### Check Active Ports

- **Using `netstat`:**

    ```bash
    netstat -tuln
    ```

- **Using `ss` (alternative to `netstat`):**

    ```bash
    ss -tuln
    ```

## Troubleshooting

- **If you encounter issues with `netstat` showing an empty or unresponsive log file, check for file permissions or verify the application's status.**

- **Ensure that the UFW firewall is properly enabled and the rules are correctly applied by running:**

    ```bash
    sudo ufw status verbose
    ```

- **Verify iptables rules by listing current rules:**

    ```bash
    sudo iptables -t nat -L -n -v
    ```

## Conclusion

This README provides the necessary steps to configure the firewall using UFW, redirect ports using iptables, and install network tools like `netstat` on an Ubuntu system. For further assistance, consult the official documentation or reach out for support.


