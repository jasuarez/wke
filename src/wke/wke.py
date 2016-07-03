import sys
import importlib
from docker import Client
from config import Config
import commands
from commands import *

class Wke(object):
    def __init__(self):
        self.client = Client()
        self.config = Config()
        self.available_commands = [comm for comm in dir(commands)
                                   if not comm.startswith('__')];

    def _get_command(self, cmd, initialize = True):
        command = importlib.import_module('wke.commands.' + cmd)
        if initialize:
            return command.Command(self.client, self.config)
        return command

    def print_usage(self):
        print("Usage: wke <command> <params> ...")
        print("")
        print("Available commands:")
        for c in self.available_commands:
            cmd = self._get_command(c, False)
            print("\t" + c + "\t" + cmd.SUMMARY)
        sys.exit(1)

    def invalid_command(self, command):
        print("Unknown command '" + command + "'")
        sys.exit(1)

    def run(self):
        argc = len(sys.argv)
        if argc == 1:
            self.print_usage()

        if sys.argv[1] not in self.available_commands:
            self.invalid_command(sys.argv[1])

        cmd = self._get_command(sys.argv[1])
        if cmd.expected_params() != argc - 2:
            print("wke " + sys.argv[1] + " " + cmd.usage())
            sys.exit(1)

        cmd.run(*sys.argv[2:])
