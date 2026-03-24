import re
import pandas as pd

apache_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<time>.*?)\] "(?P<method>\S+) (?P<url>\S+) .*" (?P<status>\d+)'
)

ssh_pattern = re.compile(
    r'Failed password.*from (?P<ip>\S+)'
)

def parse_apache(file):
    data = []
    with open(file) as f:
        for line in f:
            match = apache_pattern.search(line)
            if match:
                data.append(match.groupdict())

    df = pd.DataFrame(data)
    return df


def parse_ssh(file):
    data = []
    with open(file) as f:
        for line in f:
            match = ssh_pattern.search(line)
            if match:
                data.append(match.groupdict())

    df = pd.DataFrame(data)
    return df
