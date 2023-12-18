import os
import joblib
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import ADASYN
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import category_encoders as ce

class RandomForestModel():
    def __init__(self, data_url):
        self.data_url = data_url

    def _load_data(self, url: str) -> DataFrame:
        data = pd.read_csv(url)
        return data.copy()

    def _preprocess_data(self, data: DataFrame):
        # data split
        X = data.drop(['class'], axis=1)
        y = data['class']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=7)

        # Perform categorical encoding after splitting the data
        categorical_columns = ['source', 'browser', 'sex', 'country', 'device_id']
        binary_encoder = ce.BinaryEncoder(cols=categorical_columns)
        X_train_encoded = binary_encoder.fit_transform(X_train)
        X_test_encoded = binary_encoder.transform(X_test)

        # SMOTE
        adasyn = ADASYN(random_state=7)
        X_train_resampl, y_train_resampl = adasyn.fit_resample(X_train_encoded, y_train)

        # feature scaling
        sc = StandardScaler()
        X_train_resampl = sc.fit_transform(X_train_resampl)
        X_test = sc.transform(X_test_encoded)
        return X_train_resampl, X_test, y_train_resampl, y_test, binary_encoder

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
        X_train_resampl, X_test, y_train_resampl, y_test, binary_encoder = self._preprocess_data(data)
        classifier = self._train_model(X_train_resampl, y_train_resampl)
        y_pred = self._prediction(classifier, X_test)
        self._evaluate_model(y_test, y_pred)
        # save the model
        joblib.dump(classifier, 'RFC_model.joblib')
        joblib.dump(binary_encoder, 'binary_encoder.joblib')
if __name__ == '__main__':
    data_pwd = os.path.join(os.getcwd(), "EFraud_data.csv")
    data = RandomForestModel(data_pwd)
    data.create_model()

