
import os
import pandas as pd
from intervaltree import IntervalTree
from pandas import DataFrame


class Feature_Creation:

    def __init__(self, data_url, ip_url):
        self.data_url = data_url
        self.ip_url = ip_url

    def _preprocess_ip_to_int(self, ip: str) -> int:
        """
        Helper function to convert floating number IP address
        that represent the mean of different range of IP
        :param ip: raw data that is mean value of difference IP addresses
        :return: the number without floating point
        """
        return int(ip.split('.')[0])

    def load_data(self, url: str) -> DataFrame:
        """
        Load Fraud Data from .csv file and convert the time to datetime
        Take the integer value of IP address column suing helper function
        :param url:
        :return: return the data in DataFrame format
        """
        data = pd.read_csv(url, parse_dates=['signup_time', 'purchase_time'],
                           converters={'ip_address': lambda ip: self._preprocess_ip_to_int(ip)})
        # converters={'ip_address': lambda x: convert_to_int(x)})
        return data.copy()

    def load_ip(self, url: str) -> DataFrame:
        ip = pd.read_csv(url, converters={'lower_bound_ip_address': lambda x: int(float(x))})
        return ip.copy()

    def _replace_Ip_country(self, data_fraud: DataFrame, data_ip: DataFrame) -> DataFrame:
        """
        Create a new column 'country' from the IP address
        :param data_fraud: data fraud
        :param data_ip: data ip
        :return: renew data
        """
        search_tree = IntervalTree()
        for row in data_ip.itertuples(index=False):
            search_tree[row.lower_bound_ip_address:row.upper_bound_ip_address] = row.country

        def ip_lookup(ip):
            result = search_tree[ip]
            return result.pop().data if result else 'Others'

        data_fraud['country'] = data_fraud['ip_address'].apply(ip_lookup)
        return data_fraud

    def _time_differences(self, data_fraud: DataFrame) -> DataFrame:
        data_fraud['time_difference'] = (data_fraud['purchase_time'] - data_fraud['signup_time'])
        data_fraud['time_difference_sec'] = data_fraud['time_difference'].dt.total_seconds().astype(int)
        return data_fraud

    def _purchase_time(self, data_fraud: DataFrame) -> DataFrame:
        data_fraud['day_purchase'] = data_fraud['purchase_time'].dt.day
        data_fraud['hour_purchase'] = data_fraud['purchase_time'].dt.hour
        data_fraud['minute_purchase'] = data_fraud['purchase_time'].dt.minute
        data_fraud['second_purchase'] = data_fraud['purchase_time'].dt.second
        return data_fraud

    def _device_id_count(self, data_fraud: DataFrame) -> DataFrame:
        data_fraud['device_id_count'] = data_fraud.groupby('device_id')['device_id'].transform('count')
        return data_fraud

    def _country_count(self, data_fraud: DataFrame) -> DataFrame:
        data_fraud['country_count'] = data_fraud.groupby('country')['country'].transform('count')
        return data_fraud

    def _drop_clean_data(self, data_fraud: DataFrame) -> DataFrame:
        columns_drop = ['signup_time', 'purchase_time', 'device_id', 'time_difference', 'ip_address', 'country']
        data_fraud = data_fraud.drop(columns_drop, axis=1)
        dependent_variable = 'class'
        data_fraud = data_fraud[[col for col in data_fraud.columns if col != dependent_variable] + [dependent_variable]]
        return data_fraud

    def process_data(self) -> DataFrame:
        data_fraud = self.load_data(self.data_url)
        data_ip = self.load_ip(self.ip_url)

        data_country = self._replace_Ip_country(data_fraud, data_ip)
        data_time = self._time_differences(data_country)
        data_purchase = self._purchase_time(data_time)
        data_freq = self._device_id_count(data_purchase)

        data_country_count = self._country_count(data_freq)
        final_data = self._drop_clean_data(data_country_count)

        return final_data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data_path = os.path.join(os.getcwd(), "Fraud_Data.csv")
    ip_path = os.path.join(os.getcwd(), "IpAddress_to_Country.csv")
    final_url = os.path.join(os.getcwd(), "EFraud_data.csv")
    features = Feature_Creation(data_path, ip_path)
    final_data = features.process_data()
    print(final_url)
    final_data.to_csv(final_url, index=False)



