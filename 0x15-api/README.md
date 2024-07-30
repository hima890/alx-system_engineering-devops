# Task Management JSON Generator

This project generates a JSON file containing tasks for all employees. The JSON file includes task details organized by user ID, including usernames, task titles, and completion statuses.

## Overview

The script fetches tasks and user data from a public API and generates a JSON file where each user's tasks are organized by their `USER_ID`. This file provides a structured way to view all tasks assigned to users, including their completion status.

## Features

- Fetches task data from an API.
- Fetches user data from an API.
- Organizes tasks by user ID.
- Includes usernames, task titles, and completion statuses.
- Saves the data to a JSON file.

## Installation

To run this script, you need Python installed on your machine. You also need to install the `requests` library.

### Install Python

Download and install Python from the [official Python website](https://www.python.org/).

### Install Requests Library

You can install the `requests` library using pip. Open your terminal or command prompt and run:

```bash
pip install requests
```

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Run the script:

    ```bash
    python script.py
    ```

   This will generate a file named `todo_all_employees.json` in the project directory.

## JSON File Structure

The generated JSON file (`todo_all_employees.json`) will have the following structure:

```json
{
    "1": [
        {
            "username": "Bret",
            "task": "task title 1",
            "completed": false
        },
        {
            "username": "Bret",
            "task": "task title 2",
            "completed": true
        }
    ],
    "2": [
        {
            "username": "Antonette",
            "task": "task title 1",
            "completed": true
        }
    ]
}
```

- Each key is a `USER_ID`.
- Each value is a list of tasks associated with that user.
- Each task includes the `username`, `task` title, and `completed` status.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For any issues or suggestions, open an issue in the repository.
