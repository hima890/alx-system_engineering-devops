# Process Termination Scripts

## Introduction

This repository contains Bash scripts for terminating processes on a Unix-like system. The scripts demonstrate various methods for finding and terminating processes, such as using `kill`, `pgrep`, and sending signals.

## Files

1. `terminate_process.sh`: A Bash script that terminates a specified process using the `kill` command.

2. `terminate_process_without_kill.sh`: A Bash script that terminates a specified process without using the `kill` command.

## How to Use

### `terminate_process.sh`

This script terminates a specified process using the `kill` command.

Usage:

```bash
./terminate_process.sh process_name
```

Replace `process_name` with the name of the process you want to terminate.

### `terminate_process_without_kill.sh`

This script terminates a specified process without using the `kill` command.

Usage:

```bash
./terminate_process_without_kill.sh process_name
```

Replace `process_name` with the name of the process you want to terminate.

## Notes

- Make sure to run the scripts with appropriate permissions (`chmod +x script_name.sh`).
- The scripts may require superuser privileges to terminate certain processes.
- Use the scripts responsibly and ensure that you are terminating the correct processes.

```
