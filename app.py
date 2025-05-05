import subprocess

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    try:
        # Ensure the command is passed as a list and shell=False to avoid injection
        cmd_list = cmd.split()  # Split into a list of command and arguments
        result = subprocess.run(cmd_list, check=True, text=True, capture_output=True)
        print(result.stdout)  # Print the standard output of the command
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")  # Print the error if the command fails
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
    
    # Get the command input
    cmd = input("Enter a command to run: ")
    
    # Run the command safely
    run_command(cmd)
