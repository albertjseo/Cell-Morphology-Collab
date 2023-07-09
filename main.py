import tkinter as tk
from tkinter import filedialog as fd

from PIL import ImageTk, Image
from pandastable import Table, TableModel

from analysis import Analysis


class CellMorphology:
    root = None
    image_path = None
    image = None
    image_canvas = None
    Analysis = None

    def get_image_path(self):
        """
        Prompt for opening an image. Defaults to only allowing PNG and JPEG
        files. Saves path as class member variable
        """
        filetypes = (('Images', '*.png *.jpg *.jpeg'), ('All files', '*.*'))

        self.image_path = fd.askopenfilename(title="Open an image",
                                             filetypes=filetypes)

    def display_image(self):
        """
        Displays input image to the user
        """
        if self.image_path is None:
            return

        self.image = ImageTk.PhotoImage(Image.open(self.image_path))

        self.image_canvas = tk.Canvas(self.root, width=self.image.width(),
                                      height=self.image.height())

        self.image_canvas.place(relx=0.5, y=50, anchor=tk.N)
        self.image_canvas.create_image(self.image.width() / 2,
                                       self.image.height() / 2,
                                       anchor=tk.CENTER, image=self.image)

    def show_results(self):
        """
        Displays the cell measurements as an interactive table

        TODO: Does not scroll using trackpad in macOS
        """
        # if self.Analysis is None:
        #     return

        # results = self.Analysis.get_cell_measurements()

        # if results is None:
        #     return

        self.image_canvas = None
        self.image = None

        table_frame = tk.Frame(self.root)
        table_frame.place(relx=0.5, y=50, anchor=tk.N)

        # TODO: Replace with actual data instead of sample data
        results = TableModel.getSampleData()
        results_table = Table(table_frame, dataframe=results)
        results_table.show()

    def run_analysis(self):
        if self.Analysis is None:
            self.Analysis = Analysis(self.image_path)

        # TODO: Run analysis

    def run_gui(self):
        """
        Main GUI loop
        """
        self.root = tk.Tk()
        self.root.geometry('800x400')

        # Load image button
        button = tk.Button(self.root, text="Open image",
                           command=self.get_image_path)
        button.place(relx=0.25, y=20, anchor=tk.E)

        # Display image button
        button = tk.Button(self.root, text="Display image",
                           command=self.display_image)
        button.place(relx=0.25, y=20, anchor=tk.W)

        # Run analysis button
        button = tk.Button(self.root, text="Run analysis",
                           command=self.run_analysis)
        button.place(relx=0.75, y=20, anchor=tk.E)

        # Print results button
        button = tk.Button(self.root, text="Get results",
                           command=self.show_results)
        button.place(relx=0.75, y=20, anchor=tk.W)

        self.root.mainloop()


if __name__ == "__main__":
    app = CellMorphology()
    app.run_gui()
