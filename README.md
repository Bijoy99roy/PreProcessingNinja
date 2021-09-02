
# PreProcessing Ninja

A PreProcessing library for your basic PreProcessing needs

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org)

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)  
## Features of the package

 - impute_missing_value: Helps to impute missing values
 - scale_data: Scales the data
 - encode_categorical_data: Helps in encoding categorical variables
 - remove_outliers: Helps in removing outliers
## Use
```cmd
pip install PreProcessingNinja
```
## Github

- [Github](https://github.com/Bijoy99roy/PreProcessingNinja)

  
## Example

```python
from preprocessing_ninja import PreProcessingNinja
ninja = PreProcessingNinja()

#creating column dictionary
d = {
    'column1':'mean',
    'column2':'mean',
    'column3':'most_frequent'
}

#calling method
df = ninja.impute_missing_value(dataframe, d)
```

  
## Note

There might be bugs.

  
## Authors

- [@BijoyKumarRoy](https://www.linkedin.com/in/bijoy-kumar-roy-4b0975189/)

  