from Data_Reader_Class import CSV_Reader_Class
from Data_Plotter_Class import Data_Plotter_Class

if __name__ == "__main__":

    CSV_Reader = CSV_Reader_Class()
    
    Data_Plotter = Data_Plotter_Class()

    Data_Plotter.expenditure_hist(CSV_Reader.get_overall_expenditure_by_category())