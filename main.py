from document_tools import DataFile, ReportGenerator
def main():
    datafile = DataFile("../data/vgsales.csv", "VGSales Report")
    datafile.set_description("This is a summary of video game sales information.")
    datafile.load()
    datafile.set_process([6, 7, 8, 9, 10, 11])
    generator = ReportGenerator(datafile)
    generator.generate('../data/output.docx')
if __name__ == '__main__':
    main()
