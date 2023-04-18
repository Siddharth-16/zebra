from zebras.datainput import DataInput
from zebras.standardization import Standardization
from zebras.normalization import Normalization
from zebras.impute import Impute
from zebras.categorical import Categorical
import pandas as pd

class Preprocessor:

    data = 0

    def __init__(self, filepath):
        self.data = DataInput().inputFunction(filepath)
        self.imp = Impute(self.data)
        self.standardization = Standardization(self.data)
        self.normalization = Normalization(self.data)
        self.categorical = Categorical(self.data)

    def printData(self):
        print(self.data)

    def save(self, saveData):
        toBeDownloaded = {}
        for column in saveData.columns.values:
            toBeDownloaded[column] = saveData[column]

        newFileName = "processed.csv"
        pd.DataFrame(saveData).to_csv(newFileName, index=False)