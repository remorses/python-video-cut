import os.path
import os
from .cut_video import cut_video
from .support import name_and_ext



# def merge_overlap(acc, timeframe):
#     # print('timeframe',timeframe)
#     # print('acc',acc)
#     accuracy = 4 # seconds
#     start2, end2 = timeframe
#     start1, end1 = acc[-1] if acc else timeframe
#     if start2 - end1 <= accuracy:
#         return  [*acc[:-1], (start1, end2),  ]
#     else:
#         return [*acc, timeframe, ]


def cut_timeframes(
        in_path,
        timeframes,
        out_dir='./',
        out_pattern='{name}_{i}{ext}',
        on_exception= lambda e, t: print(f'exception while cutting {t}: {e}'),
        encode=False, 
        acodec=None, 
        vcodec=None,
    ):
    os.makedirs(out_dir, exist_ok=True)
    for (i, (start, end)) in enumerate(timeframes):
        try:
            name, ext = name_and_ext(in_path)
            out_path = os.path.join(out_dir, out_pattern.format(name=name, ext=ext, i=i))
            out_path = cut_video(in_path, out_path, start, end, encode=encode, acodec=acodec, vcodec=vcodec)
            # os.remove(out_path)
            yield out_path
        except Exception as e:
            on_exception(e, (start, end))
            pass
