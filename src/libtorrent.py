import os
import time

try:
    import libtorrent as lt
except:
    print(
        "Could not import the library libtorrents.\nPlease use aria2 method for downloading."
    )
    

def download_torrent(torrent_path, DESTINATION):
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