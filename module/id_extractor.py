#!/usr/bin/env python2
import os.path as path
import json

class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Extract ID'
        self.server = None
        if options is not None:
            if 'server' in options.keys():
                self.server = options['server']

        # source will be set by the proxy thread later on
        self.source = None

    def execute(self, data):
        print data

        js = json.loads(data)

        print "ID: ", js["id"]
        print "PW: ", js["pw"]
        f = open("id_pw.txt", "w")
        f.write("%s, %s" % (js["id"], js["pw"]))
        f.close()

        return data

    def help(self):
        h = '\tserver: remote source, used in response Server header\n'
        return h


if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
