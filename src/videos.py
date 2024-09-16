import runShell

def download_video(video_url, DESTINATION):
    """Download YouTube videos or playlists using yt-dlp."""
    command = f'yt-dlp -o "{DESTINATION}/%(title)s.%(ext)s" {video_url}'
    print(f"Downloading YouTube video/playlist: {video_url}")
    runShell.run_shell_command(command)
    print("YouTube video/playlist download completed!")