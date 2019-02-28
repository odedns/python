
from urllib import request
import json
import stats
import bitcoinFile

# Retrieve content from a URL:
def get_data():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    http_response = request.urlopen(url)
    resp_str = http_response.read()
    bitcoin_data = json.loads(resp_str)
    print(bitcoin_data)
    list_data = bitcoin_data['bpi']
    bit_values = []
    [bit_values.append(list_data[v]) for v in list_data]
    print(bit_values)
    return bit_values

bit_values = get_data()
bit_stats = stats.calc_stats(bit_values)

print("stats:",bit_stats)

bitcoinFile.create_file(bit_stats)

