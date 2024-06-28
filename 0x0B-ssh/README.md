# SSH Configuration Setup with Manual and Puppet Methods

This repository provides instructions and Puppet manifests to configure SSH client settings on a Linux system. Specifically, it demonstrates how to set up SSH to use a specific private key and disable password authentication.

## Prerequisites

- Linux environment (tested on Ubuntu)
- Access to the server where SSH configuration changes are intended
- Basic understanding of SSH and Puppet

## Tasks

### Manual SSH Configuration

1. **Copy SSH Public Key**

   - Copy your SSH public key to the server's `authorized_keys` file for passwordless authentication.

2. **Edit SSH Configuration**

   - Edit the SSH client configuration file (`~/.ssh/config`) to specify the private key and disable password authentication.

   ```bash
   Host your_server_ip_or_hostname
       IdentityFile ~/.ssh/school
       PasswordAuthentication no
   ```

   - Save the file and ensure correct permissions (`chmod 600 ~/.ssh/config`).

3. **Verify and Test**

   - SSH into your server to ensure passwordless authentication works as expected:

     ```bash
     ssh your_server_ip_or_hostname
     ```

### Puppet SSH Configuration

1. **Create Puppet Manifest**

   - Create a Puppet manifest file (`100-puppet_ssh_config.pp`) with the following content:

     ```puppet
     # Puppet manifest to configure SSH client

     file_line { 'Turn off passwd auth':
       path   => '/etc/ssh/ssh_config',
       line   => 'PasswordAuthentication no',
       ensure => present,
     }

     file_line { 'Declare identity file':
       path   => '/etc/ssh/ssh_config',
       line   => 'IdentityFile ~/.ssh/school',
       ensure => present,
     }
     ```

2. **Apply Puppet Manifest**

   - Apply the Puppet manifest using:

     ```bash
     sudo puppet apply 100-puppet_ssh_config.pp
     ```

   - Puppet will update the SSH configuration (`/etc/ssh/ssh_config`) to disable password authentication and declare the private key for authentication.

3. **Verify and Test**

   - Verify the changes in `/etc/ssh/ssh_config` to ensure the lines `PasswordAuthentication no` and `IdentityFile ~/.ssh/school` are correctly added.

   - Test SSH connection to the server to confirm passwordless authentication:

     ```bash
     ssh your_server_ip_or_hostname
     ```

## Additional Notes

- Ensure proper permissions for SSH configuration files (`chmod 600 ~/.ssh/*`).
- Always test SSH connections after making configuration changes to verify functionality.
- Adjust paths and filenames as necessary based on your system setup.
