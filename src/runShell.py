import subprocess
import sys

def run_shell_command(command, output=False):
    """Execute a shell command."""
    try:
        if output:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return result.stdout.decode("utf-8")
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing command: {e}")
        sys.exit(1)
