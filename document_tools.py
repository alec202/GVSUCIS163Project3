import csv
from docx import Document
import analysis_tools as at


class DataFile:
    def __init__(self, filename, title):
        self.filename = filename
        self.title = title
        self.description = None
        self.process = []
        self.data = []
        self.header = None


    """defining the getters"""
    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_process(self):
        return self.process

    def get_data(self):
        return self.data

    def get_header(self):
        return self.header

    """defining the setters"""
    def set_filename(self, new_name):
        self.filename = new_name

    def set_title(self, new_title):
        self.title = new_title

    def set_description(self, new_description):
        self.description = new_description

    def set_process(self, new_list):
        self.process = new_list

    def set_data(self, new_data):
        self.data = new_data

    def set_header(self, new_header):
        self.header = new_header

    """end of setters"""

    # method to get the name of the column at the specificed index
    def get_col_name(self, index):
        return self.header[index]

    # Method which adds the data for the specified column in every row to a new list and returns this new list
    def get_col(self, col):
        newList = []
        for row in self.data:
            newList.append(row[col])
        return newList

    def load(self):
        data = []
        with open(self.filename) as csvfile:
           reader = csv.reader(csvfile)
           for row in reader:
              data.append(row)
           self.header = data[0]
           del(data[0])
           self.data = data


class ReportGenerator:
    def __init__(self, datafile):
        self.datafile = datafile

    def generate(self, output_name):
        document = Document()
        document.add_heading(self.datafile.get_title(),0)
        document.add_paragraph(self.datafile.get_description())
        for col in self.datafile.get_process():
            document.add_heading(self.datafile.get_col_name(col), 1)

            # table portion
            # Create Table
            table = document.add_table(rows=1, cols=2)

            # Get first row to display mean info.
            row_cells1 = table.add_row().cells
            row_cells1[0].text = "mean:"
            row_cells1[1].text = str(at.MyMath.mean(self.datafile.get_col(col)))

            # Create and Display
            row_cells2 =



"""docx isn't working, it keeps generating an error"""
# document = Document()
#
# document.add_heading("SomeText", 0)
#
# document.save("myfile.docx")
