import subprocess

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
    
    cmd = input("Enter a command to run: ")
    
    cmd_list = cmd.split() 
    
    run_command(cmd_list)
