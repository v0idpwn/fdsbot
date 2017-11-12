import moviepy.editor as mp
import moviepy.video as mpv

def gifToClip(gifPath): 
    gifClip = mp.VideoFileClip(gifPath, target_resolution=[640,640])
    gifClip = mpv.fx.all.loop(gifClip, duration=60)
    gifClip = gifClip.set_audio(mp.AudioFileClip("sextaFeira.mp3").subclip(14, 74))
    videoPath = gifPath.replace("gif", "mp4")
    gifClip.write_videofile(videoPath)
    return videoPath    



