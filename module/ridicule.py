#!/usr/bin/env python2
import os.path as path


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Prepend HTTP response header'
        self.server = None
        if options is not None:
            if 'server' in options.keys():
                self.server = options['server']

        # source will be set by the proxy thread later on
        self.source = None

    def execute(self, data):
        f = open("id_pw.txt", "r")
        line = f.readline()
        identifier = line.strip().split(",")[0].strip()
        password = line.strip().split(",")[1].strip()
        f.close()

        html = "<html><head><title>You Hacked!</title></head><body><h1>Your ID is %s and your password is %s, right? kkk...!</h1></body></html>" % (identifier, password)

        return html

    def help(self):
        h = '\tserver: remote source, used in response Server header\n'
        return h


if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
