import os.path
from .support import subprocess_call
from .align_audio_video import align_audio_video
from .support import name_and_ext, temporary_write




def cut_video(in_path, out_path, start, end, ):
    name, ext = name_and_ext(out_path)
    with temporary_write('', path=f'_{name}{ext}') as temp_path:
        cmd = [
          "ffmpeg","-y",
          "-i", in_path,
          "-ss", "%0.3f" % start,
          # "-strict",
          # "-2",
          "-to", "%0.3f" % end, # "-vcodec", "copy", "-acodec", "copy"
          # "-vcodec", "copy", "-acodec", "copy",
          "-map","0",
          "-c", "copy",
          # "-c:a", "aac",
          # "-crf", "18",
          "-shortest",
          # "-copyts",
          "-avoid_negative_ts", "1",
          temp_path
        ]
        subprocess_call(cmd)
        out_path = align_audio_video(temp_path, out_path)
        return out_path
