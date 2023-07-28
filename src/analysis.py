import pandas
from pandastable import TableModel


class Analysis:
    """
    # TODO: Write description of what this analysis does
    """

    def __init__(self, image_path=None):
        """
        Constructor for the class

        :param image_path: Path to image to analyze
        """
        self.image_path = image_path
        self.cell_measurements = None
        self.results_are_updated = False
        self.image = None

    def load_image(self, image_path) -> bool:
        """
        TODO: Finish
            It should:
                - Update the class's image_path with the new one after
                validating
                - Load the image using OpenCV and save it as the class's
                image var
                - Delete the old results and update class state
                - Return a True if successful or False if not successful
        :return:
        """

    def set_image_path(self, image_path) -> None:
        """
        Sets a new image path. Paths are expected to be valid. Will set
        results_are_updated to false if a new image path is supplied

        :param image_path: Path to image
        """
        if image_path == self.image_path:
            return

        self.image_path = image_path

        self.results_are_updated = False

    def run_analysis(self) -> None:
        """
        TODO: Put the main analysis logic here
        :return:
        """
        if self.results_are_updated:
            return

        # TODO: Run analysis instead of supplying sample data
        self.cell_measurements = TableModel.getSampleData()

        self.results_are_updated = True

    def get_cell_measurements(self) -> pandas.DataFrame or None:
        """
        Returns a Pandas DataFrame of cell measurement information

        :return: Pandas DataFrame
        """
        if self.results_are_updated:
            return self.cell_measurements
        else:
            return None
