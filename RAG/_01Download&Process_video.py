import os 
import subprocess  #this module is used to perform terminal command in python 


# downloading the playlist from the youtube using the subprocess in python(we are using yt-dlp to download video or mp3)
# subprocess.run(["yt-dlp","-P", "/Users/amarjeet/Desktop/RAG/video" , "https://www.youtube.com/watch?v=wLEH8thqQZ8&list=PLGendcE67AFA"])

# yt-dlp -P "folder_path" "playlist/url_link"  it helps to download a video in the existing folder


files = os.listdir("video")
for file in files:
    # this terminal command is used for converting the video into mp3 using ffmpeg
    # subprocess.run(["ffmpeg", "-i", f"video/{file}", f"audio/{file}.mp3"])
    print(f"{file} converted")


