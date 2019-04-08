from video_cut import cut_timeframes, concat_videos

timeframes = [(0, 1), (2, 3), (1, 8)]

paths = cut_timeframes(
    'tests/video_.m2ts',
    timeframes,
    out_dir='./subclips',
    out_pattern='{name}_{i}{ext}',
)

result = concat_videos(paths, 'result.mov')
