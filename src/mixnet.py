from prometheus_client.parser import text_string_to_metric_families
import requests
from subprocess import check_output, run, PIPE, STDOUT
from json import loads
from pprint import pprint

def prometheus_data(ip):
    metrics = requests.get("http://" + ip+":6543/metrics").content.decode()
    for family in text_string_to_metric_families(metrics):
        print(family.keys())

def mixnet_document():
    try:
        return loads(check_output("./fmixnet"))
    except:
        return loads(check_output("fmixnet"))

if __name__ == '__main__':
    #pprint(mixnet_document())
    #topology = [item for sublist in mixnet_document()['Topology'] for item in sublist]
    #pprint(topology)
    #addresses = [n['Addresses']['tcp4'][0].split(":")[0] for n in topology]
    #[pprint(prometheus_data(a)) for a in addresses]
    #pprint(layers)
    pass
