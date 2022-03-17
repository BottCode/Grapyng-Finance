from abc import (
  ABC,
  abstractmethod,
)

import configparser

class Data_Reader_Class(ABC):

    def __init__(self):
        self._config_parser = configparser.ConfigParser()
        self._config_parser.read("Configuration/Fimo_Config.ini")
        self._PATH_TO_DB = self._config_parser["Path to data"]["Path"]
        self._expenditure_types = []
        # self._expenditure_by_category = {}
        self._overall_expenditure_by_category = {}
        self._data_dict = {}
    
    @abstractmethod
    def read_data(self):
        ...

import csv
class CSV_Reader_Class(Data_Reader_Class):

    def __init__(self):
        super(CSV_Reader_Class, self).__init__()

        self._file = open(self._PATH_TO_DB, encoding='utf-8-sig')
        self._csv_reader = csv.reader(self._file)
        self._header = next(self._csv_reader)
        
        self._column_name_to_index = {column:0 for column in self._header}
        index = 0
        for column in self._header:
            self._column_name_to_index[column] = index
            index += 1
        
        for row in self._csv_reader:
            if len(row) < len(self._column_name_to_index):
                # end of file
                break

            curr_expenditure_type = row[self._column_name_to_index["AL CONTO / ALLA CATEGORIA"]]
            if curr_expenditure_type not in self._expenditure_types:
                self._expenditure_types.append(curr_expenditure_type)
                # self._expenditure_by_category[curr_expenditure_type] = []
                self._overall_expenditure_by_category[curr_expenditure_type] = 0
            
            curr_expenditure = row[self._column_name_to_index["IMPORTO"]]
            # self._expenditure_by_category[curr_expenditure_type].append(float(curr_expenditure))
            self._overall_expenditure_by_category[curr_expenditure_type] += float(curr_expenditure)


    def read_data(self):
        pass
    
    def get_overall_expenditure_by_category(self):
        return self._overall_expenditure_by_category

    def get_column_index(self, column_name):
        return self._column_name_to_index[column_name]

        