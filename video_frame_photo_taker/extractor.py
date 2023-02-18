import os
import moviepy.editor as mp

# Create a directory for storing the extracted frames
if not os.path.exists('archive'):
    os.mkdir('archive')

# Load the video file
video = mp.VideoFileClip('kama.mp4')

# Iterate through every second of the video and extract a frame in PNG format
for t in range(0, int(video.duration), 1):
    filename = f'archive/frame_{t:04d}.png'
    video.save_frame(filename, t)
