# Logistic Regression with Iris DataSet

from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import pandas as pd


def test_iris_dataset_logistic_regression():

    # load the iris datasets
    dataset = datasets.load_iris()

    # Print keys and feature names
    print ("Keys: " + ", ".join(dataset.keys()))
    print ("Feature names: " + ", ".join(dataset.feature_names))

    # Convert to pandas dataframe and show top 5
    pdDataFrame = pd.DataFrame(dataset.data)
    pdDataFrame.columns = dataset.feature_names
    print pdDataFrame.head(6)

    # fit a logistic regression model to the data
    model = LogisticRegression(verbose=0)
    model.fit(dataset.data, dataset.target)
    print(model)

    # make predictions
    expected = dataset.target
    predicted = model.predict(dataset.data)

    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

if __name__ == '__main__':
    test_iris_dataset_logistic_regression()