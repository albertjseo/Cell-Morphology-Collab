class Analysis:
    """
    # TODO: Write description of what this analysis does
    """

    # Member variables
    image_path = None
    cell_measurements = None

    def __init__(self, image_path=None):
        """
        Constructor for the class

        :param image_path: Path to image to analyze
        """
        self.image_path = image_path

    def set_image_path(self, image_path):
        """
        Sets a new image path. Paths are expected to be valid

        :param image_path: Path to image
        """
        self.image_path = image_path

    def get_cell_measurements(self):
        """
        Returns a Pandas DataFrame of cell measurement information

        :return: Pandas DataFrame
        """
        return self.cell_measurements
