# Simple Keylogger


## Overview

This is a Python-based Keylogger application that runs in the terminal (Command Line Interface - CLI). The application captures keystrokes in real-time and logs them to a file. It was developed using Visual Studio Code (VS Code) as the Integrated Development Environment (IDE). **Important:** This tool is created for educational purposes only. The misuse of this software can lead to legal consequences, and the author does not promote illegal activities.

---

## Features

- Logs all keystrokes in real-time
- Simple and easy to use CLI interface


---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x**: The application is written in Python 3. Ensure you have Python 3.x installed. If not, you can download it from [here](https://www.python.org/downloads/).
- **Visual Studio Code**: We recommend using VS Code for development. You can download it [here](https://code.visualstudio.com/).

---


## Usage

The keylogger is a CLI-based tool. After running the application, it will start capturing keystrokes and log them into a file.

### Command-line Options

- **Start the keylogger**:
  
  ```bash
  python keylogger.py --logfile <path/to/logfile.txt>
  ```

  Replace `<path/to/logfile.txt>` with the file path where you want to save the logs.

- **Stop the keylogger**:

  Use `ESC` in the terminal to stop the keylogger.

---

## Development Environment

- **IDE**: Visual Studio Code
- **Programming Language**: Python 3.x
- **Required Packages**: 

  Install the following packages (included in `requirements.txt`):
  
  ```bash
  pip install pynput
  ```

  The `pynput` library is used to capture keyboard input.

---

## Legal Disclaimer

This software is intended for educational purposes only. The developer is not responsible for any misuse of the application. Make sure to have explicit permission from the owner of the system where this keylogger will be used. Unauthorized use of keyloggers is illegal.

---





















