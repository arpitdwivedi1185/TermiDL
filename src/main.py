import os
import directDownload
import libtorrent
import aria2c
import videos

DESTINATION = input("Enter destination directory: ")
GLOBAL_PATH = os.getcwd()
DESTINATION = GLOBAL_PATH + ("/" if "/" in GLOBAL_PATH else "\\") + DESTINATION
if not os.path.exists(DESTINATION):
    os.makedirs(DESTINATION)
print(f"Files will be downloaded to: {DESTINATION}")


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
            libtorrent.download_torrent(torrent_path, DESTINATION)
        elif c == 2:
            aria2c.download_torrent_with_aria2(torrent_path)
    elif choice == "2":
        link = input("Enter direct download link: ")
        directDownload.download_direct_link(link, DESTINATION)
    elif choice == "3":
        txt_file = input("Enter path to text file with download links: ")
        if not os.path.exists(txt_file):
            print(f"Text file not found: {txt_file}")
        else:
            with open(txt_file, "r") as file:
                links = file.readlines()
                for link in links:
                    directDownload.download_direct_link(link)
    elif choice == "4":
        video_url = input("Enter YouTube video or playlist URL: ")
        videos.download_video(video_url, DESTINATION)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
