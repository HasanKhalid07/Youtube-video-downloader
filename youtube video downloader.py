from pytube import YouTube

def download_video(url, path):
    """
    Downloads the highest resolution video from the given YouTube URL and saves it to the specified path.
    
    Parameters:
    url (str): The URL of the YouTube video.
    path (str): The directory path where the video will be saved.
    """
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)

        # Get the stream with the highest resolution
        stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        stream.download(output_path=path)

        # Print the title of the downloaded video
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the YouTube video URL
    video_url = input("Enter the URL of the YouTube video: ")

    # Prompt the user to enter the path where the video should be saved
    save_path = input("Enter the path where you want to save the video: ")

    # Call the download_video function with the provided URL and path
    download_video(video_url, save_path)
 