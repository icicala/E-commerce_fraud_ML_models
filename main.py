# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import pandas as pd

from feature_creation import Feature_Creation

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), "Fraud_Data.csv")
    ip_path = os.path.join(os.getcwd(), "IpAddress_to_Country.csv")
    final_url = os.path.join(os.getcwd(), "EFraud_data.csv")
    features = Feature_Creation(data_path, ip_path)
    final_data = features.process_data()
    final_data.to_csv(final_url, index=False)


