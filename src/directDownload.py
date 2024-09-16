import runShell

def download_direct_link(link, DESTINATION):
    """Download files from a direct link using aria2c."""
    command = f'aria2c --dir="{DESTINATION}" {link}'
    print(f"Downloading: {link}")
    runShell.run_shell_command(command)
    print("Download completed!")
