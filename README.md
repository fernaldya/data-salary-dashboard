# data-salary-dashboard 

Using this [dataset](https://www.kaggle.com/datasets/chopper53/machine-learning-engineer-salary-in-2024?resource=download) I create a data pipeline where I simulate:

1. Preloading the dataset into the source container postgres database (All TEXT datatype)
2. Create a data pipeline to fetch and standardize the data before injecting into another container
3. Create a data dashboard where the user can freely explore the data
