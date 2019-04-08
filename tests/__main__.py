from video_cut import cut_timeframes

timeframes = [(0, 4), (2, 5)]

paths = cut_timeframes(
    'tests/video.m2ts',
    timeframes,
    out_dir='./',
    out_pattern='{name}_{i}{ext}',
)

print(list(paths))
