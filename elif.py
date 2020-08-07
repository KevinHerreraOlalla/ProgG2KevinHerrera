# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:21:45 2020

@author: User
"""


aclnum=int(input("cual es el NUMERO IPv4 ACL?"))
if aclnum>=1 and aclnum<=99:
    print("Este es un sntandar ipv4 acl")
elif aclnum>=100 and aclnum<=199:
    print("Es una valor extenso ipv4 acl")
else:
    print("no es un valor standar o extenso ipv4 acl0")