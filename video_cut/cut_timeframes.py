import os.path
import os
from .concat_subclips import concat_subclips
from .extract_subclip import cut
from .support import name_and_ext
from functools import reduce



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


def cut_timeframes(in_path, timeframes, out_dir='./', out_pattern='{name}_{i}{ext}', ):
    for (i, (start, end)) in enumerate(timeframes):
        try:
            name, ext = name_and_ext(in_path)
            out_path = os.path.join(out_dir, out_pattern.format(name=name, ext=ext, i=i))
            out_path = cut(in_path, out_path, start, end)
            # os.remove(out_path)
            yield out_path
        except Exception as e:
            print(f'got exception {e}')
            pass
