# TermiDL

**TermiDL** is a terminal-based download manager that supports downloading content from various sources such as torrents, direct links, YouTube and other site's videos, and playlists. It simplifies the process of managing downloads directly from your terminal and leverages tools like `aria2` and `yt-dlp` for efficient file fetching.

## Features

- **Torrent Downloads**: Supports `.torrent` files and magnet links using `aria2` and `libtorrent`.
- **Direct Link Downloads**: Download files from HTTP/HTTPS URLs.
- **Text File Batch Downloads**: Download multiple links listed in a text file.
- **Videos & Playlists**: Download videos and entire playlists from YouTube and other supported sites via `yt-dlp`.
- **Cross-Platform**: Works on both Linux and Windows.

## Requirements

Make sure you have the following installed:

- **aria2**: For downloading torrents and direct links.
  - [Download aria2](https://aria2.github.io/)
- **yt-dlp**: For downloading YouTube videos and playlists.
  - [yt-dlp Installation Guide](https://github.com/yt-dlp/yt-dlp)
- **FFmpeg**: For proper functioning of yt-dlp, we need the FFmpeg depencency.
  - [FFmpeg Installation](https://www.ffmpeg.org/download.html)
- **Python 3.x**

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arpitdwivedi1185/TermiDL.git
   cd TermiDL
   ```
2. Install dependencies:
   - `aria2` must be installed and available in your system's PATH.
   - `yt-dlp` and `FFmpeg` should be installed for video support and should be in PATH as well.

## Usage
When you run TermiDL, you will be prompted to select a download mode from the following options:
1. **Download Torrent File/Magnet Link:** Enter the path to a .torrent file or a magnet link.
2. **Download from Direct Link:** Enter any HTTP/HTTPS URL for direct file download.
3. **Download from a Text File:** Provide the path to a text file containing multiple download links (one per line).
4. **Download Video/Playlist:** Enter a YouTube video or playlist URL to download the content.

### Example Usage
- **Downloading a torrent:**
    ```bash
    python3 main.py
    ```
    Give the desired download location, then select option 1 and provide a `.torrent` file location or magnet link.

- **Downloading a direct link:**
    ```bash
    python3 main.py
    ```
    Give the desired download location, then select option 2 and provide a direct link.
    
- **Downloading multiple files from direct link using txt file:**
    ```bash
    python3 main.py
    ```
    Give the desired download location, then select option 3 and provide the location to `.txt` file that contains direct download links, each on a new line.
    
- **Downloading Videos/Playlist:**
    ```bash
    python3 main.py
    ```
    Give the desired download location, then select option 4 and provide the link to video/playlist. A list of supported sites can be found [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).
    
## License
This project is licensed under the MIT License.
