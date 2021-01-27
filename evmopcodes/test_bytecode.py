# Standard libs
import os


def trace_debug_bytecode(bytecode, sender=None, gas=None, price=None, data=None):
    command_str = "evm --debug --statdump --code " + bytecode
    if sender:
        command_str += " --sender " + sender
    if gas:
        command_str += " --gas " + gas
    if price:
        command_str += " --price " + price
    if data:
        command_str += " --input " + data
    command_str += " run"
    print(command_str)
    os.system(command_str)
