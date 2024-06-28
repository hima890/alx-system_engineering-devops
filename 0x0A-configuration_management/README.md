# Puppet Configuration Management

This repository contains Puppet manifests to perform various system configuration tasks. Below are the details of each task and the corresponding Puppet manifest.

## Task 1: Create a File in /tmp

**Objective:**
Create a file at `/tmp/school` with the following requirements:
- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

**Manifest:**
```puppet
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
```

**Usage:**
Save the above code in a file called `create_school_file.pp` and apply the manifest using the following command:
```sh
sudo puppet apply create_school_file.pp
```

## Task 2: Install Flask from pip3

**Objective:**
Install Flask version 2.1.0 using `pip3`.

**Manifest:**
```puppet
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}
```

**Usage:**
Save the above code in a file called `install_flask.pp` and apply the manifest using the following command:
```sh
sudo puppet apply install_flask.pp
```

## Task 3: Execute a Command to Kill a Process

**Objective:**
Create a manifest that kills a process named `killmenow` using the `exec` Puppet resource and `pkill`.

**Manifest:**
```puppet
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
```

**Usage:**
Save the above code in a file called `kill_process.pp` and apply the manifest using the following command:
```sh
sudo puppet apply kill_process.pp
```

**Example Demonstration:**

1. **Terminal #0 - Start the process:**
   ```sh
   # Create the killmenow script
   cat > killmenow <<'EOF'
   #!/bin/bash
   while [[ true ]]
   do
       sleep 2
   done
   EOF

   # Make the script executable
   chmod +x killmenow

   # Run the script
   ./killmenow &
   ```

2. **Terminal #1 - Apply the Puppet manifest:**
   ```sh
   sudo puppet apply kill_process.pp
   ```

3. **Verify the process is terminated:**
   ```sh
   pgrep -f killmenow
   ```
   If the process is successfully terminated, there should be no output from this command.

## Notes

- Ensure you have Puppet installed on your system before applying the manifests.
- Use `sudo` to apply the manifests to ensure the necessary permissions for file creation, package installation, and process management.

## License

This project is licensed under the MIT License.
