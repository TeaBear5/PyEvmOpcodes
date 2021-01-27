# Standard libs
import os


def trace_debug_bytecode(bytecode, sender=None):
    command_str = "evm --debug --statdump --code " + bytecode
    if sender:
        command_str += " --sender " + sender
    command_str += " run"
    print(command_str)
    os.system(command_str)
