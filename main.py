import os
import sys
import time
import subprocess

try:
    import libtorrent as lt
except:
    print(
        "Could not import the library libtorrents.\nPlease use aria2 method for downloading."
    )

DESTINATION = input("Enter destination directory: ")
GLOBAL_PATH = os.getcwd()
DESTINATION = GLOBAL_PATH + ("/" if "/" in GLOBAL_PATH else "\\") + DESTINATION
if not os.path.exists(DESTINATION):
    os.makedirs(DESTINATION)
print(f"Files will be downloaded to: {DESTINATION}")


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


def download_torrent_with_aria2(torrent_path):
    """Download torrent files using aria2c."""
    print(f"Downloading torrent: {torrent_path}")
    command = f'aria2c --dir="{DESTINATION}" --seed-time=0 "{torrent_path}"'
    run_shell_command(command)
    print("Torrent download completed!")


def download_torrent(torrent_path):
    """Download torrent files using libtorrent."""
    ses = lt.session()
    ses.listen_on(6881, 6891)

    if torrent_path.startswith("magnet:"):
        print(f"Adding magnet link: {torrent_path}")
        handle = lt.add_magnet_uri(ses, torrent_path, {"save_path": DESTINATION})
    elif os.path.exists(torrent_path):
        print(f"Adding torrent file: {torrent_path}")
        info = lt.torrent_info(torrent_path)
        handle = ses.add_torrent({"ti": info, "save_path": DESTINATION})
    else:
        print("Invalid torrent file or magnet link!")
        return

    print("Downloading metadata...")
    while not handle.has_metadata():
        time.sleep(1)
    print("Metadata retrieved!")

    while not handle.is_seed():
        status = handle.status()
        print(
            f"Progress: {status.progress * 100:.2f}% - Download Speed: {status.download_rate / 1000:.2f} kB/s"
        )
        time.sleep(1)

    print("Download completed!")


def download_direct_link(link):
    """Download files from a direct link using aria2c."""
    command = f"aria2c {link}"
    print(f"Downloading: {link}")
    run_shell_command(command)
    print("Download completed!")


def download_from_txt(file_path):
    """Download files from a text file containing multiple links."""
    if not os.path.exists(file_path):
        print(f"Text file not found: {file_path}")
        return

    with open(file_path, "r") as file:
        links = file.readlines()
        for link in links:
            download_direct_link(link)


def download_youtube_video(video_url):
    """Download YouTube videos or playlists using yt-dlp."""
    command = f'yt-dlp -o "{DESTINATION}/%(title)s.%(ext)s" {video_url}'
    print(f"Downloading YouTube video/playlist: {video_url}")
    run_shell_command(command)
    print("YouTube video/playlist download completed!")


def main():
    print("\nChoose download mode:")
    print("1. Download Torrent File/Magnet Link")
    print("2. Download from Direct Link")
    print("3. Download from a Text File containing Links")
    print("4. Download YouTube Video/Playlist")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        torrent_path = input("Enter torrent file path or magnet link: ")
        c = int(
            input(
                "1. Download with libtorrent (Linux)\n2. Download with aria2 (Windows)\n"
            )
        )
        if c == 1:
            download_torrent(torrent_path)
        elif c == 2:
            download_torrent_with_aria2(torrent_path)
    elif choice == "2":
        link = input("Enter direct download link: ")
        download_direct_link(link)
    elif choice == "3":
        txt_file = input("Enter path to text file with download links: ")
        download_from_txt(txt_file)
    elif choice == "4":
        video_url = input("Enter YouTube video or playlist URL: ")
        download_youtube_video(video_url)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
