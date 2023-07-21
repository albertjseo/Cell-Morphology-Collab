import pytest

from analysis import Analysis


@pytest.fixture
def image_path():
    return "./test_images/mastcells_1.jpg"


def test_get_cell_measurements_returns_none_without_running_analysis(
        image_path):
    analysis = Analysis(image_path)

    ans = analysis.get_cell_measurements()

    assert ans is None


def test_get_cell_measurements_returns_expected_columns(image_path):
    analysis = Analysis(image_path)
    analysis.run_analysis()

    ans = analysis.get_cell_measurements()

    assert ans.columns == ['Area', 'Major Axis Length', 'Minor Axis Length',
                           'Perimeter']
