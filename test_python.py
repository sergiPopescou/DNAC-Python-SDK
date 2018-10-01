#!/usr//bin/env python

'''

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

'''
import sys

__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"
from python_client.api.network_device_api import NetworkDeviceApi
from python_client.api.topology_api import TopologyApi
from python_client.api.discovery_api import DiscoveryApi
from python_client.api.dna_intent_api import DnaIntentApi
from python_client.api.misc_api import MiscApi
from python_client.api.interface_api import InterfaceApi
from python_client.configuration import Configuration
from python_client.api_client import ApiClient
from python_client.models.generate_token_request import GenerateTokenRequest
import json
import argparse
import socket
import getpass
import urllib3

# Quick check if the entered ip address is a valid one
def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def main():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['network'], type=str,
                        help='command = "network" for retrieving network count ' \
                             'and a list of network devices')
    parser.add_argument('-i', '--ipaddress', type=str, help='DNA Center cluster ip address')
    parser.add_argument('-u', '--uname', type=str, default='admin', help='DNA Center login username')
    args = parser.parse_args()
    #
    # if valid_ip(args.ipaddress) == False:
    #     print ('You need to provide a valid ipaddress')
    #     sys.exit('Invalid ipaddress')
    if args.uname == '':
        print ('You need to provide a valid DNAC login username')
        sys.exit('Invalid username')

    # Prompt for password
    dnacPwd = getpass.getpass(
        "\nPlease enter the DNA Center \'{}\' user password for the {} cluster : ".format(args.uname,
                                                                                              args.ipaddress))
    #Set up configuration
    config = Configuration()
    config.host = "https://" + args.ipaddress
    config.username = args.uname
    config.password = dnacPwd
    # Set the following to True if you want to enable SSL verification
    config.verify_ssl = False
    config.debug = False

    #Get Basic Auth of credentials
    config.api_key = config.get_basic_auth_token()
    #Create client by passing the config params
    apic = ApiClient(configuration=config, header_name = 'Authorization', header_value = config.api_key)
    #Get the auth token
    tokenRequest = GenerateTokenRequest()
    auth_instance = MiscApi(apic)
    auth_response = auth_instance.post_auth_token(request=tokenRequest,authorization=config.api_key)
    token = auth_response.token
    # Set X-AUTH-TOKEN
    apic.set_default_header("X-AUTH-TOKEN",token)

    # Call the APIs
    api_instance = NetworkDeviceApi(apic)
    iface_api = InterfaceApi(apic)
    api_instance_top = TopologyApi(apic)
    api_instance_disc = DiscoveryApi(apic)
    api_dna_intent = DnaIntentApi(apic)
    print("\nGetting device count\n")
    count_response = api_instance.get_network_device_count()
    print(count_response.response)
    print("\n")
    print("Getting devices\n")
    template = '{:<40} {:<15} {:<25} {:<6}'
    table_headers = ['Id', 'PlatformId', 'Hostname', 'Serial']
    table_ul = ['--------', '--------', '----------', '------']
    dev_response = api_instance.get_network_device()
    print(template.format(*table_headers))
    print(template.format(*table_ul))
    for dev in dev_response.response:
        dev_dict = dev.to_dict()
        print(template.format(dev_dict["id"],dev_dict["platform_id"],dev_dict["hostname"],dev_dict["serial_number"]))
        wireless_resp = api_instance.get_network_device_wireless_info_by_id(dev_dict["id"])
        print(wireless_resp.response.to_dict())
        iface_resp = iface_api.get_interface_network_device_by_device_id(dev_dict["id"])
        #uplinks = []
        # for ifc in iface_resp.response:
        #     print(ifc.to_dict()["status"])
        #     if ifc.status == 'UP':
        #         uplinks.append(ifc.to_dict())
        uplinks = [ifc.to_dict() for ifc in iface_resp.response if ifc.status == 'up']
        print(uplinks)
        timestamp = 3000
        clie_detail = api_dna_intent.get_dna_intent_clie_detail(timestamp, dev_dict["mac_address"])
        print(clie_detail)
    print("\n")

    print("Getting Topology\n")
    template = '{:<40} {:<40} {:<25} {:<15} {:<100}'
    table_headers = ['Id', 'ParentId', 'Global Name Hierarchy',  'Name', 'Address']
    table_ul = ['--------', '--------', '----------', '----------', '----------']
    print(template.format(*table_headers))
    print(template.format(*table_ul))
    dev_response = api_instance_top.get_topology_site_topology()
    for sit in dev_response.response.sites:
        sit_dict = sit.to_dict()
        print(template.format(sit_dict["id"],sit_dict["parent_id"],sit_dict["group_name_hierarchy"],sit_dict["name"],sit_dict["location_address"]))
        # disco = api_instance_disc.get_discovery_by_id(sit_dict["parent_id"])
        # print(disco)

if __name__ == '__main__':
    main()
