import pandas as p
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Binarizer

data_set = p.read_csv("C:\\dhara\\python\\mark.csv")
mark1 = data_set.head()
mark2 = np.array(data_set['m2'])

#x= mark1.reshape(-1,1)
y = mark2.reshape(-1,1)

Binarizer1 = Binarizer(threshold=70)
print(Binarizer1.fit_transform(mark1[['m1']]))
print(Binarizer1.fit_transform(y))


# import pandas as p
# from sklearn.preprocessing import Binarizer

# # Load the dataset
# data_set = p.read_csv("C:\\dhara\\python\\mark.csv")

# # Apply Binarizer directly to the columns of the dataframe
# Binarizer1 = Binarizer(threshold=70)

# # Applying the transformation to the columns directly without reshaping into arrays
# print(Binarizer1.fit_transform(data_set[['m1']]))
# print(Binarizer1.fit_transform(data_set[['m2']]))

# import pandas as p
# from sklearn.preprocessing import Binarizer

# # Load the dataset
# data_set = p.read_csv("C:\\dhara\\python\\mark.csv")

# # Select the first 5 rows using head() for both columns
# head_data = data_set.head()

# # Apply Binarizer directly to the columns of the DataFrame for the first 5 rows
# Binarizer1 = Binarizer(threshold=70)

# # Binarizing the first 5 rows of 'm1' and 'm2'
# print(Binarizer1.fit_transform(head_data[['m1']]))
# print(Binarizer1.fit_transform(head_data[['m2']]))
