# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from feature_creation import Feature_Creation

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_url = "/home/icicala/Desktop/Data_Ecom_Fraud/Fraud_Data.csv"
    ip_url = "/home/icicala/Desktop/Data_Ecom_Fraud/IpAddress_to_Country.csv"
    features = Feature_Creation(data_url, ip_url)
    final_data = features.process_data()

    print(final_data)


