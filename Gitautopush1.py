### This will Update all files and folder at One git status.
import subprocess
import time
import re
from datetime import datetime, timedelta

# Define the Git commands
commands = {
    'status': 'git status --porcelain',
    'add': 'git add "{filename}"',  # Adding quotes to handle spaces
    'commit': 'git commit -m "New concept"',
    'push': 'git push origin main'
}

def run_command(command, filename=None):
    if filename:
        command = command.format(filename=filename)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

def parse_git_status(status_output):
    # Use regex to match file paths, including directories and files with spaces
    pattern = r'^[ MADRCU?]{1,2} (.+)$'
    return re.findall(pattern, status_output, re.MULTILINE)

def main():
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Check the status of the Git repository
        result = run_command(commands['status'])
        status_output = result.stdout.strip()
        
        if status_output:
            # Parse the status output to get the list of files or folders
            items = parse_git_status(status_output)
            if items:
                # Print the list of items
                print(f'[{current_time}] Items detected for status update: {items}')
                
                # Loop through each item to handle them one by one
                for item in items:
                    # Add the item (file or folder)
                    run_command(commands['add'], item)
                
                # Commit the changes
                run_command(commands['commit'])
                
                # Push the changes
                push_result = run_command(commands['push'])
                if push_result.returncode == 0:
                    print(f'Successfully pushed the changes at {current_time}')
                else:
                    print(f'Failed to push the changes.')
                    print(push_result.stderr)
        
            # Set the waiting time (e.g., 15 minutes = 900 seconds)
            waiting_time = 1800  # 30 minutes in seconds
            
            next_check_time = (datetime.now() + timedelta(seconds=waiting_time)).strftime("%Y-%m-%d %H:%M:%S")
            print(f'Next Git status will be checked after {int(waiting_time / 60)} minutes at {next_check_time}')
            
            # Sleep for the specified time
            time.sleep(waiting_time)
        else:
            # If no files are untracked or modified, rest for a set amount of time
            rest_time = 900  # 15 minutes in seconds
            print(f'[{current_time}] No Untracked or Modified Files Found. Resting for {int(rest_time / 60)} minutes.')
            
            next_check_time = (datetime.now() + timedelta(seconds=rest_time)).strftime("%Y-%m-%d %H:%M:%S")
            print(f'Next Git status will be checked at {next_check_time}')
            
            # Sleep for the rest time
            time.sleep(rest_time)

if __name__ == "__main__":
    main()
