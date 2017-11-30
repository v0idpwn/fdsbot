import moviepy.editor as mp
import moviepy.video as mpv

def gif_to_clip(gifPath): 
    gif_clip = mp.VideoFileClip(gifPath, target_resolution=[640,640])
    gif_clip = mpv.fx.all.loop(gifClip, duration=60)
    gif_clip = gifClip.set_audio(
                    mp.AudioFileClip("sextaFeira.mp3")
                    .subclip(14, 74)
                )
    video_path = gifPath.replace("gif", "mp4")
    gif_clip.write_videofile(video_path,audio_codec="aac", 
                             audio_bitrate="96k")
    return video_path
