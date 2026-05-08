import argparse
import sys

from tabulate import tabulate

from app.csv_reader import CsvReaderError, load_csv_files
from app.reports.clickbait import ClickbaitReport


REPORTS = {
    "clickbait": ClickbaitReport,
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate YouTube reports from CSV files",
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV files with video metrics",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name",
    )

    return parser.parse_args()


def get_report(report_name: str):
    report_class = REPORTS.get(report_name)

    if report_class is None:
        available_reports = ", ".join(REPORTS.keys())

        raise ValueError(
            f"Unknown report: {report_name}. "
            f"Available reports: {available_reports}"
        )

    return report_class()


def print_report(videos):
    table = [
        [video.title, video.ctr, video.retention_rate]
        for video in videos
    ]

    print(
        tabulate(
            table,
            headers=["title", "ctr", "retention_rate"],
            tablefmt="grid",
        )
    )


def main():
    args = parse_args()

    try:
        videos = load_csv_files(args.files)
        report = get_report(args.report)

        report_result = report.generate(videos)

        print_report(report_result)

    except CsvReaderError as error:
        print(error)
        sys.exit(1)

    except ValueError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()