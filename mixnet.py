from prometheus_client.parser import text_string_to_metric_families
import requests
from subprocess import check_output
from json import loads
from pprint import pprint

def prometheus_data():
    for ip in instance_list.values():
        metrics = requests.get("http://" + ip+":6543/metrics").content.decode()
        for family in text_string_to_metric_families(metrics):
            print(family)

def mixnet_document():
    return loads(check_output(["go", "run", "mixnet.go"]))

if __name__ == '__main__':
    pprint(mixnet_document())
