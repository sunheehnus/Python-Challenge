#!/usr/bin/python
import xmlrpclib
server=xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
#server.system.listMethods()
print server.phone("Bert")
