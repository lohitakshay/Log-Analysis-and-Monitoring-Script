# Log-Analysis-and-Monitoring-Script

## Overview
This Python script provides real-time analysis of log files, generating summary reports at regular intervals and displaying new entries. It also includes a keyword search feature.

## Prerequisites
1. Basic knowledge of Python and log files
2. Python 3.x
3. Tabulate library 

## Installation
Clone the repository or download the log_analysis.py file.
Ensure Python is updated.
Install the Tabulate library using pip install tabulate.

## Execution
Modify the log_path variable in the script to point to your log file.
Run the script using python log_analysis.py.

## Usage
1. Run the `logging_example.py` script to generate example log messages. This script will create a log file named `example.log`.
2. Use the `example.log` file as a test case for your main log analysis and monitoring script (`log_analysis.py`).
3. Modify the `log_path` variable in the `log_analysis.py` script to point to the `example.log` file.
4. Run the `log_analysis.py` script to analyze and monitor the `example.log` file in real-time.


## Features
Real-time log analysis and monitoring.
Summary reports include counts of specific keywords or patterns, such as error messages.
Keyword search functionality allows users to search for specific terms within the log file.
Errors and exceptions are logged and displayed to the user.

## Note
The script does not print the existing log data in the log file

