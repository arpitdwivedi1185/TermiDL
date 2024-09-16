import runShell

def download_torrent_with_aria2(torrent_path, DESTINATION):
    """Download torrent files using aria2c."""
    print(f"Downloading torrent: {torrent_path}")
    command = f'aria2c --dir="{DESTINATION}" --seed-time=0 "{torrent_path}"'
    runShell.run_shell_command(command)
    print("Torrent download completed!")
