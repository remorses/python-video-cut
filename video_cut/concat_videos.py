import os.path
from .support import subprocess_call, temporary_write



def concat_videos(in_paths, out_path):
    in_paths = [os.path.abspath(path) for path in in_paths]
    file_list = '\n'.join(f'file {path}' for path in in_paths)
    with temporary_write(file_list) as list_path:
        subprocess_call([
            'ffmpeg',
            '-f',
            'concat',
            '-y',
            '-safe',
            '0',
            '-i',
            list_path,
            '-c',
            'copy',
            out_path
        ])
    return out_path
