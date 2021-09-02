import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder


class PreProcessingNinja:
    def __init__(self):
        self.scaler = None
        self.encoder = None

    def impute_missing_value(self, dataframe, columns, missing_value=np.nan):
        """
        Helps in imputing missing values in dataframe
        :param dataframe: pandas dataframe
        :param columns: columns info to be passed in dictionary format
        {
        attribute: strategy
        }
        strategy-
        "mean": replaces null values with mean of all the values
        "median": replaces null values with median of all values
        "most_frequent": replaces null values with mode of all values
        :param missing_value: type of missing values default: nan
        :return: dataframe
        """
        try:
            for key, value in columns.items():
                imputer = SimpleImputer(missing_values=missing_value, strategy=value)
                dataframe[[key]] = imputer.fit_transform(dataframe[[key]])
            return dataframe
        except Exception as e:
            print(e)

    def scale_data(self, dataframe, columns, strategy='Standardarization'):
        """
        Helps in scaling data in dataframe
        :param dataframe: pandas dataframe
        :param columns: list of columns to scale
        :param strategy: strategy to scale data
        default: 'Standardarization',
        another one 'Normalization'
        :return: dataframe
        """
        try:
            if isinstance(self.scaler, (StandardScaler, MinMaxScaler)):
                dataframe[columns] = self.scaler.transform(dataframe[columns])
            else:
                if strategy == 'Standardarization':
                    self.scaler = StandardScaler()
                    dataframe[columns] = self.scaler.fit_transform(dataframe[columns])
                elif strategy == 'Normalization':
                    self.scaler = MinMaxScaler()
                    dataframe[columns] = self.scaler.fit_transform(dataframe[columns])
            return dataframe
        except Exception as e:
            print(e)

    def encode_categorical_data(self, dataframe, columns, drop_first=True):
        """
        encode categorical data
        :param dataframe: pandas dataframe
        :param columns: columns info to be passed in dictionary format
        {
        'attribute': 'strategy'
        }
        strategy-
        'binary': encodes data in binary format
        'ordinal': encodes data in ordinal format
        :param drop_first: it will drop first column, applicable only for binary
        :return: dataframe
        """
        try:
            if isinstance(self.encoder, OrdinalEncoder):
                dataframe[list(columns.keys())] = self.encoder.transform(dataframe[list(columns.keys())])
            else:
                for key, value in columns.items():
                    if value == 'binary':
                        dataframe = pd.get_dummies(dataframe, columns=[key], prefix=[key], drop_first=drop_first)
                    elif value == 'ordinal':
                        self.encoder = OrdinalEncoder()
                        dataframe[[key]] = self.encoder.fit_transform(dataframe[[key]])
            return dataframe
        except Exception as e:
            print(e)

    def remove_outliers(self, dataframe, columns, lower_thresh=0.25, upper_thresh=0.75):
        """
        removes outliers
        :param dataframe: pandas dataframe
        :param columns: list of columns to remove outlier
        :param lower_thresh: lower threshold for quantile
        default: 0.25
        :param upper_thresh: upper threshold for quantile
        default: 0.75
        :return: dataframe
        """
        try:
            for i in columns:
                iqr = dataframe[i].quantile(upper_thresh) - dataframe[i].quantile(lower_thresh)
                lower = dataframe[i].quantile(lower_thresh) - 1.5 * iqr
                upper = dataframe[i].quantile(upper_thresh) + 1.5 * iqr
                dataframe.loc[dataframe[i] < lower, i] = lower
                dataframe.loc[dataframe[i] > upper, i] = upper
            return dataframe
        except Exception as e:
            print(e)
