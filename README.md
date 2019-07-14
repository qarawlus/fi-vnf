# fi-vnf
Small VNF for Future Internet course, SS'19 UPB

The VNF is a spam filter. It collects traffic only on port 25 and ignores other ports. 

## Requirements for Scapy
Collect the requirements using apt (Ubuntu) or your favorite package manager.
```bash
apt install python3 python-dev python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip libnetfilter-queue-dev 
```

## Installing the SPAM-VNF module 

```bash
git clone https://github.com/qarawlus/fi-vnf.git
cd fi-vnf
python setup.py install
``` 

## Running the VNF

### Running in mininet with provided example (Using ryu-controller)
Inside the fi-vnf folder run commands according to the following
```bash
$ ryu-manager <PATH_TO_RYU_CONTROLLER>/ryu/app/simple_switch.py
$ sudo mn --custom res/fi.py --topo FI_TOPO --switch ovsk --controller
mininet> xterm sf
xterm> ./initiate.sh
xterm> spam-vnf -d res/dict.yaml
```
Here, `-d res/dict.yaml` defines the filter rules file that is being used for the spam filtering

---
You can test connectivity on ports other than 25 by simply running the following:

```bash
mininet> h1 ping h2
```

