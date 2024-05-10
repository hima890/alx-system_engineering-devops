## Networking Basics 2

This repository contains Bash scripts aimed at configuring and managing network settings on Ubuntu servers. Below are the tasks covered along with their descriptions and usage examples:

### Task 0: Change Your Home IP

**Description:**
Write a Bash script that configures an Ubuntu server to meet the following requirements:
- Configure localhost to resolve to 127.0.0.2
- Configure facebook.com to resolve to 8.8.8.8

**Usage Example:**
```
sylvain@ubuntu$ sudo ./0-change_your_home_IP
```

### Task 1: Show Attached IPs

**Description:**
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

**Usage Example:**
```
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
```

### Task 2: Port Listening on localhost

**Description:**
Write a Bash script that listens on port 98 on localhost.

**Usage Example:**
```
Terminal 0:

Starting my script.
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost

Terminal 1:

Connecting to localhost on port 98 using telnet and typing some text.
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test

Terminal 0:

Receiving the text on the other side.
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test

For the sake of the exercise, this connection is made entirely within localhost. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
```

**Note:** Ensure to revert localhost to 127.0.0.1 after running Task 0 script to avoid issues with local services. 

**Repository:**
- GitHub Repository: [alx-system_engineering-devops](https://github.com/hima890/alx-system_engineering-devops)
- Directory: 0x08-networking_basics_2
