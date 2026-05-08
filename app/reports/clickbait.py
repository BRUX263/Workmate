from app.reports.base import BaseReport


class ClickbaitReport(BaseReport):

    def generate(self, videos):
        filtered_videos = [
            video
            for video in videos
            if video.ctr > 15 and video.retention_rate < 40
        ]

        return sorted(
            filtered_videos,
            key=lambda video: video.ctr,
            reverse=True,
        )