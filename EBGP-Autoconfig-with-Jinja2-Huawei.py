#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
from contextlib import redirect_stdout


#This line uses the current directory
file_loader = FileSystemLoader('.')
# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('bgp_huawei_template.j2')
output = template.render(
                         local_asn=input('Enter the local ASN: '), #Local ASN
                         provider_name=input('Enter the name of the internet provider (COGENT-VERIZON): '), #Service Provider Name (COGENT-VERIZON-NTT)
                         ipv4_underline=input('Enter the ipv4 address of the neighbor with underlines (1_1_1_1): '), #This will create the traffic policies and route-filters in IPv4
                         ipv6_underline=input('Enter the ipv6 address of the neighbor with underlines (2800_1_F_1): '), #This will create the traffic policies and route-filters in IPv6
                         interface=input('Enter the interface (100GE2/0/2): '), #BGP-Interface
                         description=input('Enter the interface description: '), #Interface Description 
                         ipv4_add=input('Enter the source ipv4 address and his mask (1.1.1.2 255.255.255.252): '), #IPv4 Address of the Source Interface
                         ipv6_add=input('Enter the source ipv6 address and his mask (2800:1:F::2/127): '), #IPv6 Address of the Source Interface
                         bgp_neighbor=input('Enter the neighbor ipv4 address (1.1.1.1): '), #Neighbor IPv4 Address
                         bgp_neighbor_v6=input('Enter the neighbor ipv6 address (2800:1:F::1): '), #Neighbor IPv6 Address
                         remote_asn=input('Enter the remote ASN: '), #Remote ASN
                         description_v4=input('Enter the description for the BGPv4 peer: '), #Description of the BGPv4 peer
                         description_v6=input('Enter the description for the BGPv6 peer: '), #Description of the BGPv6 peer
                         )
#Print the output
print(output)

with open('BGP-PEER-CONFIG-XXX.txt', 'a') as f: #save the output in a txt file
        with redirect_stdout(f):
            print(output)