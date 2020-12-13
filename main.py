from moviepy.editor import *

clip = VideoFileClip('testOriginal.mp4')

trimmedClip = clip.subclip(60, 120)

trimmedClip.write_videofile('testNew.mp4')