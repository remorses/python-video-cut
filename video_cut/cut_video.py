import os.path
from .support import subprocess_call
from .align_audio_video import align_audio_video





def cut_video(in_path, out_path, start, end, ):
    temp_path = f'_{in_path}'
    """ makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    cmd = [
      "ffmpeg","-y",
      "-i", in_path,
      "-ss", "%0.3f" % start,
      # "-strict",
      # "-2",
      "-to", "%0.3f" % end, # "-vcodec", "copy", "-acodec", "copy"
      # "-vcodec", "copy", "-acodec", "copy",
      "-map","0",
      "-c:v", "copy",
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
