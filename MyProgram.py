import pdb
import sys
from datetime import datetime


def Fair_billing(dict):
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    start_time = lines[0].split("\n")[0].split(" ")[0]

    for line in lines:
        time, name, status = line.split("\n")[0].split(" ")

        if name in dict:
            if status == "End":
                if dict[name][0].get("Start time"):
                    tdelta = (datetime.strptime(time, '%H:%M:%S') - datetime.strptime(dict[name][0]["Start time"][0], '%H:%M:%S')).seconds
                    del dict[name][0]["Start time"][0]
                else:
                    tdelta = (datetime.strptime(time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')).seconds
                    dict[name][0]["sessions"] = dict[name][0]["sessions"] + 1
                dict[name][0]["total time"] = dict[name][0]["total time"] + tdelta

            elif status == "Start":
                if dict[name][0].get("Start time"):
                    dict[name][0]["Start time"].append(time)
                    dict[name][0]["sessions"] = dict[name][0]["sessions"] + 1
                else:
                    dict[name][0]["Start time"] = [time]
                    dict[name][0]["sessions"] = dict[name][0]["sessions"] + 1

        else:
            if status == "Start":
                dict[name] = [{"sessions": 1, "total time":0, "Start time": [time]}]
            elif status == "End":
                tdelta = (datetime.strptime(time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')).seconds
                dict[name] = [{"sessions": 1, "total time": tdelta}]

    for key, values in dict.items():
        print(key, values[0]["sessions"], values[0]["total time"])

    return "Completed Script!"


if __name__ == '__main__':
    Fair_billing({})
