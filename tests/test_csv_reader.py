import pytest

from app.csv_reader import CsvReaderError, load_csv_files


CSV_CONTENT = """title,ctr,retention_rate,views
Video A,18.5,35,100
Video B,22.0,25,200
"""


def test_load_csv_files_reads_videos(tmp_path):
    csv_file = tmp_path / "stats.csv"
    csv_file.write_text(CSV_CONTENT, encoding="utf-8")

    result = load_csv_files([str(csv_file)])

    assert len(result) == 2

    assert result[0].title == "Video A"
    assert result[0].ctr == 18.5
    assert result[0].retention_rate == 35.0


def test_load_csv_files_raises_error_for_missing_file():
    with pytest.raises(CsvReaderError):
        load_csv_files(["missing.csv"])