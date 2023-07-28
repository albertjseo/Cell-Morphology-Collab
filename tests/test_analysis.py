import pytest

from src.analysis import Analysis


@pytest.fixture
def image_path():
    return ["./test_images/mastcells_1.jpg", "./test_images/mastcells_2.jpeg"]


class TestGetCellMeasurements:
    def test_get_cell_measurements_returns_none_without_running_analysis(self,
                                                                         image_path):
        """
        get_cell_measurements() should return a None if you initialize the
        Analysis class and call this method before running the run_analysis()
        method
        """
        analysis = Analysis(image_path[0])

        ans = analysis.get_cell_measurements()

        assert ans is None

    def test_get_cell_measurements_returns_expected_columns(self, image_path):
        """
        get_cell_measurements() should return a DataFrame with the columns:
            - Area
            - Major Axis Length
            - Minor Axis Length
            - Perimeter
        """
        analysis = Analysis(image_path[0])
        analysis.run_analysis()

        ans = analysis.get_cell_measurements()

        assert ans.columns == ['Area', 'Major Axis Length', 'Minor Axis Length',
                               'Perimeter']

    def test_get_cell_measurements_provides_updated_results_on_new_image(self,
                                                                         image_path):
        """
        If you load one image and get results after running analysis, loading a
        new image and getting results after running analysis should yield you
        different results.
        """
        # Initialize and run analysis
        analysis = Analysis(image_path[0])
        analysis.run_analysis()

        # Get results
        old_results = analysis.get_cell_measurements()

        # Load new image
        analysis.load_image(image_path[1])

        # Get new results
        new_results = analysis.get_cell_measurements()

        # Verify new_results is not None
        assert new_results is not None

        # Verify old_results is not None
        assert old_results is not None

        # Verify they're not the same
        assert not old_results.equals(new_results)


class TestLoadImage:
    def test_load_image_returns_true_on_valid_image(self, image_path):
        """
        load_image() should return a True if the image path provided is valid
        """
        analysis = Analysis(image_path[0])

        ans = analysis.load_image(image_path[1])

        assert ans is True

    def test_load_image_returns_false_on_invalid_image(self, image_path):
        """
        load_image() should return a False if the image path provided is false
        """
        analysis = Analysis(image_path[0])

        ans = analysis.load_image('./invalid.jpeg')

        assert ans is False

    def test_load_image_deletes_old_results_on_new_image_load(self, image_path):
        """
        load_image() should prevent the user from getting the previous image's
        cell measurements if they load a new image and immediately call
        get_cell_measurements() without running run_analysis().
        get_cell_measurements() should return a None instead of old results
        """
        # Initialize and run analysis
        analysis = Analysis(image_path[0])
        analysis.run_analysis()

        # Get results
        old_results = analysis.get_cell_measurements()

        # Load new image
        analysis.load_image(image_path[1])

        # Get new results
        new_results = analysis.get_cell_measurements()

        # Verify old results is not None
        assert old_results is not None

        # Verify they're not the same
        assert not old_results.equals(new_results)

        # Verify new_results is a None
        assert new_results is None
