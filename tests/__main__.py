from video_cut import cut_timeframes, concat_videos

timeframes = [(1, 7), (3, 4), (3 * 60 + 50, 3 * 30 + 90)]

paths = cut_timeframes(
    '/Users/morse/Documents/GitHub/twitch-to-youtube/data/videos/panetty_2019-04-07/video.m2ts',
    timeframes,
    out_dir='./subclips',
    out_pattern='{name}_{i}{ext}',
)

result = concat_videos(paths, 'result.mov')
