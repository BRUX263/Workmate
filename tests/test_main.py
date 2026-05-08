import pytest

from app.main import get_report


def test_get_report_returns_clickbait_report():
    report = get_report("clickbait")

    assert report is not None


def test_get_report_raises_error_for_unknown_report():
    with pytest.raises(ValueError):
        get_report("unknown")