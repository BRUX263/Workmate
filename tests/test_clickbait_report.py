from app.models import VideoMetric
from app.reports.clickbait import ClickbaitReport


def test_clickbait_report_filters_and_sorts_videos():
    videos = [
        VideoMetric(
            title="Video 1",
            ctr=18.0,
            retention_rate=35.0,
        ),
        VideoMetric(
            title="Video 2",
            ctr=25.0,
            retention_rate=20.0,
        ),
        VideoMetric(
            title="Video 3",
            ctr=10.0,
            retention_rate=90.0,
        ),
    ]

    report = ClickbaitReport()

    result = report.generate(videos)

    assert len(result) == 2

    assert result[0].title == "Video 2"
    assert result[1].title == "Video 1"