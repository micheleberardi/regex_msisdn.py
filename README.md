# LOOKING MSISDN INTO A LOGS UNDER CERTAIN CONDITIONS

# HOW USE THE COMMAND

```
michelone$ python regex_msisnd.py --help
usage: regex_msisnd.py [-h] -p PATH [PATH ...] [--version]

HOW TO USE THE COMMAND

optional arguments:
  -h, --help            show this help message and exit
  -p PATH [PATH ...], --path PATH [PATH ...]
                        ...
  --version             show program's version number and exit

```

# EXAMPLE

```
$ python regex_msisdn.py -p logs/proxy_202005* <<< path with wildcard file for example check all logs on May 2020

```
# EXAMPLE LOGS
```
Sun, 03 May 2020 07:01:54 INFO     FOUND THIS CASE2020-05-01 00:16:57 (18930) [INF] [MONIT][DURATION:0.052103042602539][MSISDN:3421637533][MAYA_API:rechargeUserNew][userKey:'PoBtVrFqYwMEXrvr0iwCWSrp1mXWIRmE'][storeNetworkId:600000][domainId:'10'][realmId:'11'][datasource:'12'][realsource:'18'][RES:'{"userKey":"PoBtVrFqYwMEXrvr0iwCWSrp1mXWIRmE","action":"rechargeUserNew","result":"-1","message":"Not authorized user"}']

```

# CONDICTION OF THIS SCRIPT BUT YOU CAN CHANGE
the script need to return all MSISDN where if a raw ave
```
if "Not authorized user" in line and "MSISDN:3" in line and "rechargeUserNew" in line:
```
need to execute this regex rule
```
msidsn = re.search(r'\[MSISDN:([0-9]+)\]', line).groups(1)
```
retrun will be an list of MSISDN
```
3421637533
3385417856
3687335094
3474969811
3505778713
3247997243
3357031637
3273383228
3348437292
3881018964

```
