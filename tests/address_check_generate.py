# Local libs
from evmopcodes.opcodes import *

VALID_ADDRESS = "0x029f388ac4d5c8bff490550ce0853221030e822b"

program_commands = [
    CALLER,
    PUSH20,
    VALID_ADDRESS,
    EQ,
    PUSH1,
    "0x1B",
    JUMPI,
    STOP,
    JUMPDEST
]

bytecode = get_hex_program(program_commands)
print(bytecode)
print(len(bytecode)/2 - 2)
