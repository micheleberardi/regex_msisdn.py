#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

__author__ = "Michele Berardi"
__copyright__ = "Copyright 2020"
__license__ = "GPL"
__version__ = "1.0.8"
__maintainer__ = "Michele Berardi"
__email__ = "michele@linux.com"
__status__ = "Production"

import os
import argparse
import re
#from datetime import datetime
import logging

if __name__ == '__main__':
    ENV = (os.path.dirname(os.path.realpath(__file__)))
    #datelog = datetime.now().strftime('%Y-%m-%d')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=ENV + "/ads-ingester-one.log", filemode='a')
    parser = argparse.ArgumentParser(description='HOW TO USE THE COMMAND')
    parser.add_argument('-p', '--path', type=str, help='...', nargs='+',required=True)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.7')
    args = parser.parse_args()
    path = args.path
    for f in path:
        logging.info("START TO PROCESS FILE " + str(f))
        with open(f, 'r') as myfile:
            for line in myfile:
                if "Not authorized user" in line and "MSISDN:3" in line and "rechargeUserNew" in line:
                    logging.info("FOUND THIS CASE "+str(line))
                    try:
                        msidsn = re.search(r'\[MSISDN:([0-9]+)\]', line).groups(1)
                        print(msidsn[0])
                        logging.info("FOUND MSISDN "+str(msidsn[0]))
                    except:
                        logging.error("ERROR "+str(line))

                else:
                    continue
        logging.info("FINISH TO PROCESS FILE " + str(f))
    logging.info("********")
    logging.info("ALL DONE")



'''
NOTE:
GREP COMMAND LINE TO VERIFY
grep -E 'rechargeUserNew' logs/proxy_202005010*.log |grep 'Not authorized user' |grep 'MSISDN:3' -c
SECOND METHOD
#msidsn = re.findall(r".(?<=MSISDN:)(.*)(?=\]\[MAYA)", line)
'''



