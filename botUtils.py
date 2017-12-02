import moviepy.editor as mp
import moviepy.video as mpv

def gif_to_clip(gif_path): 
    gif_clip = mp.VideoFileClip(gif_path, target_resolution=[640,640])
    gif_clip = mpv.fx.all.loop(gif_clip, duration=60)
    gif_clip = gif_clip.set_audio(
                    mp.AudioFileClip("sextaFeira.mp3")
                    .subclip(14, 74))
    video_path = gif_path.replace("gif", "mp4")
    gif_clip.write_videofile(video_path,audio_codec="aac", 
                             audio_bitrate="96k")
    return video_path
