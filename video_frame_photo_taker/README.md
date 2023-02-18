# Extract Frames from Video using Python


To download every second of a video and save it in PNG format using Python, you can use the moviepy library.

This code first creates a directory named "archive" to store the extracted frames. It then loads the video file using moviepy, and iterates through every second of the video using a for loop. For each second, it extracts a frame from the video and saves it as a PNG file in the "archive" directory, with a filename that includes the frame number. The t variable is the time in seconds, and int(video.duration) is the total duration of the video in seconds.

Note that this code assumes that you have the moviepy library installed. If you don't have it, you can install it using pip install moviepy.

Requirements
- Python 3.6 or higher
- moviepy library


How to download the MoviePy library from GitHub:

1. First, navigate to the official MoviePy GitHub repository, which can be found at https://github.com/Zulko/moviepy.

2. Once you're on the repository page, locate the green "Code" button, which is located just above the list of files and directories.

3. Click the "Code" button to reveal a dropdown menu, and then select "Download ZIP". This will download a ZIP archive of the entire repository to your local machine.

4. Extract the contents of the ZIP archive to a folder on your local machine. This folder will contain all of the necessary files for the MoviePy library.

5. Open your command prompt or terminal window and navigate to the folder where you extracted the ZIP archive. You can do this by using the cd command followed by the file path of the folder.

6. Once you're in the MoviePy folder, you can install the library by running the following command: pip install .

7. Wait for the installation to complete, and you're done! You should now be able to import the MoviePy library into your Python scripts and use it to create and edit videos.

ustomization
You can customize the script by modifying the following variables:

- video_file: The name of the video file to extract frames from.
- output_dir: The name of the output directory to save the frames in.
- fps: The number of frames per second to extract.

That's it! If you followed these steps correctly, you should now have the MoviePy library installed on your machine and ready to use. If you encounter any issues during the installation process, refer to the official MoviePy documentation or reach out to the community for help.
