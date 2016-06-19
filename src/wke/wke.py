import sys
import importlib
from docker import Client
from config import Config

class Wke(object):
    def __init__(self):
        self.client = Client()
        self.config = Config()

    def print_usage(self):
        print("Usage: wke <command> <params> ...")
        sys.exit(1)

    def invalid_command(self, command):
        print("Unknown command '" + command + "'")
        self.print_usage()

    def run(self):
        argc = len(sys.argv)
        if argc == 1:
            self.print_usage()
            
        try:
            command = command = importlib.import_module('wke.commands.' + sys.argv[1])
        except ImportError:
            self.invalid_command(sys.argv[1])

        cmd = command.Command(self.client, self.config)
        
        if cmd.expected_params() != argc - 2:
            print("wke " + sys.argv[1] + " " + cmd.usage())
            sys.exit(1)

        cmd.run(*sys.argv[2:])
