# Web Stack Debugging - README

This README file provides details on two tasks focused on improving the performance and stability of web server setups, particularly those using Nginx. The tasks involve debugging and fixing configuration issues to enhance server response times and handle user limits more effectively.

## Task 0: Sky is the Limit, Let's Bring That Limit Higher

### Objective
In this task, we aimed to improve the performance of a web server setup running Nginx. The server was experiencing a significant number of failed requests under load, and our goal was to reduce the number of failed requests to zero.

### Problem Description
During benchmarking with ApacheBench, the server was tested with 2000 requests, 100 at a time. Initially, 943 out of 2000 requests failed, and the server returned many non-2xx responses. This indicated a problem with the server's configuration, which needed to be optimized to handle the load effectively.

### Solution
We applied a Puppet configuration file (`0-the_sky_is_the_limit_not.pp`) that adjusted the Nginx server settings to better handle high traffic. After applying the configuration, we reran the ApacheBench test and achieved the following results:
- All 2000 requests were completed successfully.
- No failed requests.
- Improved response time and throughput.

### How to Use
1. Apply the Puppet configuration:
   ```bash
   puppet apply 0-the_sky_is_the_limit_not.pp
   ```
2. Benchmark the server using ApacheBench:
   ```bash
   ab -c 100 -n 2000 localhost/
   ```
3. Verify that the number of failed requests is zero and check the server's performance metrics.

## Task 1: User Limit

### Objective
This task aimed to fix an issue related to the operating system's user limits, which was preventing the `holberton` user from logging in and executing basic commands due to too many open files.

### Problem Description
When attempting to log in as the `holberton` user, the system returned errors like "Too many open files," preventing the user from executing commands or logging out properly. This issue was caused by an incorrect configuration of the OS file descriptor limits.

### Solution
We applied a Puppet configuration file (`1-user_limit.pp`) that modified the OS settings to allow the `holberton` user to log in and execute commands without encountering the "Too many open files" error.

### How to Use
1. Apply the Puppet configuration:
   ```bash
   puppet apply 1-user_limit.pp
   ```
2. Log in as the `holberton` user:
   ```bash
   su - holberton
   ```
3. Verify that the user can now log in and execute commands without errors.

### Files in this Repository
- `0-the_sky_is_the_limit_not.pp`: Puppet configuration for optimizing Nginx performance.
- `1-user_limit.pp`: Puppet configuration for adjusting OS file descriptor limits.

## Conclusion
By following the steps outlined in this README, you can improve the performance and stability of your Nginx server under load and ensure that user limits do not hinder basic operations.

