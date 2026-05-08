import csv
from pathlib import Path

from app.models import VideoMetric


class CsvReaderError(Exception):
    pass


def load_csv_files(files: list[str]) -> list[VideoMetric]:
    videos = []

    for file_name in files:
        path = Path(file_name)

        if not path.exists():
            raise CsvReaderError(f"File does not exist: {file_name}")

        with path.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                videos.append(
                    VideoMetric(
                        title=row["title"],
                        ctr=float(row["ctr"]),
                        retention_rate=float(row["retention_rate"]),
                    )
                )

    return videos