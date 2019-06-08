#!/usr/bin/python -tt

# vm-mgmt connects to a vCenter/ESX Server to execute tasks
# and generate reports
# Copyright: (c) 2014 Jonar M.
# License: BSD, see LICENSE for more details.

import sys
import os
import re
import inspect
import getpass
import time
import pysphere
from pysphere import VIServer, VIProperty, MORTypes


def get_user_info():
    """ Obtain accoount details through user input"""
    user = raw_input('Enter username: ')
    if len(user) == 0 or user.isspace():
        sys.exit('Error: Emtpy username')
    passwd = getpass.getpass('Password: ')
    vcenter = raw_input('Enter vCenter/ESX Server: ')
    if len(vcenter) == 0 or vcenter.isspace():
        sys.exit('Error: Emtpy vCenter/ESX Server')
    return (user,passwd,vcenter)


def get_serverlist():
    """Obtain hostname listed on serverlist file through user input"""
    serverlist = raw_input('Enter the serverlist file: ')
    try:
        f = open(serverlist)
    except IOError:
        sys.exit('IOError: No such file or directory. Check also the file permissions')
    servers = f.readlines()
    servercount = len(servers)
    for host in servers:
        return (host,servers,servercount)


def getserver_type_api():
    """Display's the server type(vCenter or ESX) and also the VMWare API version"""
    s = VIServer()
    print 'Server Type: ', s.get_server_type()
    print 'API Version: ', s.get_api_version()


def vm_migrate():
    """Migrate the VMs based on the list given"""
    user, passwd, vcenter = get_user_info()
    host, servers, servercount = get_serverlist()
    s = VIServer()
    s.connect(vcenter, user, passwd)
    getserver_type_api()

    esxhost_input = raw_input('Enter target ESX Host: ')
    esxhost = s.get_hosts().items()
    for k,v in esxhost:
        if v == esxhost_input:
            for host in servers:
                host = host.strip()
                vm = s.get_vm_by_name(host)
                vm.migrate(host=k)
                time.sleep(10)
    s.disconnect()


def menu(list, question):
    """Provides the list of options or tasks that the user may choose"""
    for entry in list:
        print '[', 1 + list.index(entry), '] ' + entry
    return input(question)
    #return raw_input(question)


def main():
    items = ['Vmotion servers based on given list', \
             'Exit'\
            ]
    choice = menu(items,"Select an option: ")
    while True:
        if choice == 1:
            vm_migrate()
        elif choice == 2:
            print sys.exit('Bye!')
        else:
            print 'Choose from the options only!'
            break


if __name__ == '__main__':
    main()
