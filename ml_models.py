import os
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


class RandomForestModel():
    def __init__(self, data_url):
        self.data_url = data_url

    def _load_data(self, url: str) -> DataFrame:
        data = pd.read_csv(url)
        return data.copy()

    def _categorical_feature_encoding(self, data) -> DataFrame:
        data_c = data.copy()
        categorical_columns = ['source', 'browser', 'sex']
        onehot_encoder = OneHotEncoder(drop='first', sparse_output=False)
        data_encoded = pd.DataFrame(onehot_encoder.fit_transform(data_c[categorical_columns]))
        data_c = pd.concat([data_c, data_encoded], axis=1)
        data_c.drop(categorical_columns, axis=1, inplace=True)
        dependent_variable = 'class'
        data_c = data_c[[col for col in data_c.columns if col != dependent_variable] + [dependent_variable]]
        return data_c

    def _preprocess_data(self, data: DataFrame):
        # data split
        X = data.drop(['class'], axis=1)
        y = data['class']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=7)

        # fix the int column name error
        X_train.columns = X_train.columns.astype(str)
        X_test.columns = X_test.columns.astype(str)

        # SMOTE
        smote = SMOTE(random_state=7)
        X_train_resampl, y_train_resampl = smote.fit_resample(X_train, y_train)

        # feature scaling
        sc = StandardScaler()
        X_train_resampl = sc.fit_transform(X_train_resampl)
        X_test = sc.transform(X_test)
        return X_train_resampl, X_test, y_train_resampl, y_test

    def _train_model(self, X_train, y_train):
        classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=7)
        classifier.fit(X_train, y_train)
        return classifier

    def _prediction(self, classifier, X_test):
        y_pred = classifier.predict(X_test)
        return y_pred

    def _evaluate_model(self, y_test, y_pred):
        confmatrix = confusion_matrix(y_test, y_pred)
        accuracy_sc = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        rec_score = recall_score(y_test, y_pred)
        f_score = f1_score(y_test, y_pred)
        print(confmatrix)
        print('Accuracy Score', accuracy_sc)
        print('Precision:', precision)
        print('Recall:', rec_score)
        print('f1 Score:', f_score)

    def create_model(self):
        data = self._load_data(self.data_url)
        encoded_data = self._categorical_feature_encoding(data)
        X_train_resampl, X_test, y_train_resampl, y_test = self._preprocess_data(encoded_data)
        classifier = self._train_model(X_train_resampl, y_train_resampl)
        y_pred = self._prediction(classifier, X_test)
        self._evaluate_model(y_test, y_pred)


if __name__ == '__main__':
    url = os.path.join(os.getcwd(), "EFraud_data.csv")
    data = RandomForestModel(url)
    data.create_model()
