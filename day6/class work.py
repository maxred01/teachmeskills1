#1
def dict_data (data, data2, data3):
    print(data.items(), data3.keys(), data2.values())

    data_item = []
    data_item.extend(data.items())
    data_item.extend(data2.items())
    data_item.extend(data3.items())

    data_key = []
    data_key.extend(data.keys())
    data_key.extend(data2.keys())
    data_key.extend(data3.keys())

    data_value = []
    data_value.extend(data.values())
    data_value.extend(data2.values())
    data_value.extend(data3.values())

    data = {}
    for i in range(0, len(data_key)):
        data[data_key[i]] = data_value[i]
    return data

data = {'name': 'Sasha'}
data2 = {'Last_name': 'Viktorov'}
data3 = {'sur_name': 'Ivanova'}



dict_data(data, data2, data3)



