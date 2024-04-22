import logging
import os
from collections import defaultdict
import time
from datetime import datetime
from tabulate import tabulate

# Path to the log file
log_path = 'C:\\course\\marketfeed\\trial.log'

# Store the last position in the log file that was read
last_pos = 0

# Store the total count of log entries
total_entries = 0

# Dictionary to store keyword counts
keyword_count = defaultdict(int)
log_level_count = defaultdict(int)

# Dictionary to store the count of new entries added since the last report
new_entries = defaultdict(int)

# Flag to indicate if it's the first iteration
first_iter = True

# Flag to indicate if keyword search mode is active
search_active = False

try:
    while True:
        # Get the size of the log file
        file_size = os.path.getsize(log_path)

        # Read new entries from the log file
        with open(log_path, 'r') as file:
            # Seek to the last position
            file.seek(last_pos)
            new_lines = file.readlines()

            # Update the last position to the current file size
            last_pos = file_size

            # Perform basic log analysis on new entries
            for line in new_lines:
                if 'error' in line.lower():
                    keyword_count['error'] += 1
                    new_entries['error'] += 1
                if 'warning' in line.lower():
                    keyword_count['warning'] += 1
                    new_entries['warning'] += 1
                if 'info' in line.lower():
                    log_level_count['INFO'] += 1
                    new_entries['INFO'] += 1
                elif 'debug' in line.lower():
                    log_level_count['DEBUG'] += 1
                    new_entries['DEBUG'] += 1

            # Calculate the total count of log entries
            total_entries += len(new_lines)

        # Get the current date and time for the summary report
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Print summary report
        summary_report = []
        for category in set(list(log_level_count.keys()) + list(keyword_count.keys())):
            summary_report.append([
                category,
                log_level_count[category] + keyword_count[category],
                new_entries[category]
            ])
        summary_report.append(['Total Log Entries', total_entries, sum(new_entries.values())])

        print('\n--- Summary Report ---')
        print(tabulate(summary_report, headers=['Category', 'Count', 'New Added'], tablefmt='grid'))
        print(f"\nReport generated at: {report_time}")

        # Print new entries if not the first iteration
        if not first_iter:
            if any(new_entries.values()):
                print('\n--- New Entries ---')
                sorted_new_lines = sorted(new_lines, key=lambda x: ('warning' in x.lower(), 'error' in x.lower(), 'debug' in x.lower(), 'info' in x.lower()), reverse=True)
                new_lines_table = []
                for entry in sorted_new_lines:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_lines_table.append([timestamp, entry.strip()])
                print(tabulate(new_lines_table, headers=['Date and Time', 'Log Entry'], tablefmt='grid'))
            else:
                print("\nNo new entries.")

        # Reset counts for the next interval
        new_entries.clear()
        first_iter = False

        # Wait for 10 seconds before updating the summary report again
        time.sleep(10)

except KeyboardInterrupt:
    # Check if keyword search mode is active
    while not search_active:
        try:
            search_active = True
            keyword = input("\nEnter a keyword to search in the log file (Ctrl+C again to exit): ")
            with open(log_path, 'r') as file:
                lines = file.readlines()
                matching_lines = [line.strip() for line in lines if keyword.lower() in line.lower()]
                if matching_lines:
                    print("\n--- Search Results ---")
                    for line in matching_lines:
                        print(line)
                else:
                    print("\nNo matching entries found.")
        except EOFError:
            break
        finally:
            search_active = False

    else:
        print("\nStopping log monitoring and exiting.")
