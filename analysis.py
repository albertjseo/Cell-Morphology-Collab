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

    def set_image_path(self, image_path):
        """
        Sets a new image path. Paths are expected to be valid. Will set
        results_are_updated to false if a new image path is supplied

        :param image_path: Path to image
        """
        if image_path == self.image_path:
            return

        self.image_path = image_path

        self.results_are_updated = False

    def run_analysis(self):
        """
        TODO: Put the main analysis logic here
        :return:
        """
        if self.results_are_updated:
            return

        # TODO: Run analysis instead of supplying sample data
        self.cell_measurements = TableModel.getSampleData()

        self.results_are_updated = True

    def get_cell_measurements(self):
        """
        Returns a Pandas DataFrame of cell measurement information

        :return: Pandas DataFrame
        """
        if self.results_are_updated:
            return self.cell_measurements
