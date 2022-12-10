"""Project 3: Analyzing Data and Producing reports. This is a project that calls upon 3 classes in order to
read data about video games from a CSV file. Those 3 classes are used to find information like means, medians, and etc.
and then  a microsoft word document is produced displaying that information.

Programmer Names: James Brand, Alec Mirambeau.

Date of Submission: 12/09/2022.

James Brand, Alec Mirambeau
We certify that this work was done in accordance with the GV academic honesty policies.
Fall, 2022."""

from document_tools import DataFile, ReportGenerator
# end of imports

# define the main function of the program
def main():
    """
    :return: nothing
    """
    datafile = DataFile("../data/vgsales.csv", "VGSales Report")
    datafile.set_description("This is a summary of video game sales information.")
    datafile.load()
    datafile.set_process([6, 7, 8, 9, 10, 11])
    generator = ReportGenerator(datafile)
    generator.generate('../data/output.docx')

if __name__ == '__main__':
    # running the main function
    main()

