# Gas prices groups
G_ZERO = 0
G_BASE = 2
G_VERY_LOW = 3
G_LOW = 5
G_MID = 8
G_HIGH = 10


class OPCODE:
    value = "0x00"


class STOP(OPCODE):
    """
    Halts execution.
    """
    value = "0x00"
    gas = G_ZERO


class ADD(OPCODE):
    """
    Addition operation.
    """
    value = "0x01"
    gas = G_VERY_LOW


class MUL(OPCODE):
    """
    Multiplication operation.
    """
    value = "0x02"
    gas = G_LOW


class SUB(OPCODE):
    """
    Subtraction operation.
    """
    value = "0x03"
    gas = G_VERY_LOW


class DIV(OPCODE):
    """
    Integer division operation.
    """
    value = "0x04"
    gas = G_LOW


class SDIV(OPCODE):
    """
    Signed integer division operation (truncated).  Where all values are treated as two’s complement signed 256-bit
    integers.
    """
    value = "0x05"
    gas = G_LOW


class MOD(OPCODE):
    """
    Modulo remainder operation.
    """
    value = "0x06"
    gas = G_LOW


class SMOD(OPCODE):
    """
    Signed modulo remainder operation.  Where all values are treated as two’s complement signed 256-bit
    integers.
    """
    value = "0x07"
    gas = G_LOW


class ADDMOD(OPCODE):
    """
    Modulo addition operation.
    """
    value = "0x08"
    gas = G_MID


class MULMOD(OPCODE):
    """
    Modulo multiplication operation.
    """
    value = "0x09"
    gas = G_MID


class EXP(OPCODE):
    """
    Exponential operation.
    """
    value = "0x0a"
    gas = G_HIGH


class SIGNEXTEND(OPCODE):
    """
    Modulo addition operation.
    """
    value = "0x0b"
    gas = G_HIGH


class LT(OPCODE):
    """
    Less-than comparison.
    """
    value = "0x10"
    gas = G_VERY_LOW


class GT(OPCODE):
    """
    Greater-than comparison.
    """
    value = "0x11"
    gas = G_VERY_LOW


class SLT(OPCODE):
    """
    Signed less-than comparison.
    """
    value = "0x12"
    gas = G_VERY_LOW


class SGT(OPCODE):
    """
    signed greater-than comparison.
    """
    value = "0x13"
    gas = G_VERY_LOW


class EQ(OPCODE):
    """
    Equality comparison.
    """
    value = "0x14"
    gas = G_VERY_LOW


class ISZERO(OPCODE):
    """
    Simple not operator.
    """
    value = "0x15"
    gas = G_VERY_LOW


class AND(OPCODE):
    """
    Bitwise AND operation.
    """
    value = "0x16"
    gas = G_VERY_LOW


class OR(OPCODE):
    """
    Bitwise OR operation.
    """
    value = "0x17"
    gas = G_VERY_LOW


class XOR(OPCODE):
    """
    Bitwise XOR operation.
    """
    value = "0x18"
    gas = G_VERY_LOW


class NOT(OPCODE):
    """
    Bitwise NOT operation.
    """
    value = "0x19"
    gas = G_VERY_LOW


class BYTE(OPCODE):
    """
    Retrieve single byte from word.
    """
    value = "0x1a"
    gas = G_VERY_LOW


class SHL(OPCODE):
    """
    Left shift operation.
    """
    value = "0x1b"
    gas = G_VERY_LOW


class SHR(OPCODE):
    """
    Right shift operation.
    """
    value = "0x1c"
    gas = G_VERY_LOW


class SAR(OPCODE):
    """
    Bitwise NOT operation.
    """
    value = "0x1d"
    gas = G_VERY_LOW


class SHA3(OPCODE):
    """
    Compute Keccak-256 hash.
    """
    value = "0x20"
    gas = 30


class ADDRESS(OPCODE):
    """
    Get address of currently executing account. 
    """
    value = "0x30"
    gas = G_BASE


class BALANCE(OPCODE):
    """
    Get balance of the given account.
    """
    value = "0x31"
    gas = 700


class ORIGIN(OPCODE):
    """
    Get execution origination address.
    """
    value = "0x32"
    gas = G_BASE


class CALLER(OPCODE):
    """
    Get caller address.
    """
    value = "0x33"
    gas = G_BASE


class CALLVALUE(OPCODE):
    """
    Get deposited value by the instruction/transaction responsible for this execution.
    """
    value = "0x34"
    gas = G_BASE


class CALLDATALOAD(OPCODE):
    """
    Get input data of current environment.
    """
    value = "0x35"
    gas = G_VERY_LOW


class CALLDATASIZE(OPCODE):
    """
    Get size of input data in current environment.
    """
    value = "0x36"
    gas = G_BASE


class CALLDATACOPY(OPCODE):
    """
    Copy input data in current environment to memory.
    """
    value = "0x37"
    gas = G_VERY_LOW


class CODESIZE(OPCODE):
    """
    Get size of code running in current environment.
    """
    value = "0x38"
    gas = G_BASE


class CODECOPY(OPCODE):
    """
    Copy code running in current environment to memory
    """
    value = "0x39"
    gas = G_VERY_LOW


class GASPRICE(OPCODE):
    """
    Get price of gas in current environment.
    """
    value = "0x3a"
    gas = G_BASE


class EXTCODESIZE(OPCODE):
    """
    Get size of an account’s code.
    """
    value = "0x3b"
    gas = 700


class EXTCODECOPY(OPCODE):
    """
    Copy an account’s code to memory.
    """
    value = "0x3c"
    gas = 700


class RETURNDATASIZE(OPCODE):
    """
     Get size of output data from the previous call from the current environment.
    """
    value = "0x3d"
    gas = G_BASE


class RETURNDATACOPY(OPCODE):
    """
    Copy output data from the previous call to memory.
    """
    value = "0x3e"
    gas = G_VERY_LOW


class EXTCODEHASH(OPCODE):
    """
    Get hash of an account’s code.
    """
    value = "0x3f"
    gas = 700


class BLOCKHASH(OPCODE):
    """
    Get the hash of one of the 256 most recent complete blocks
    """
    value = "0x40"
    gas = 20


class COINBASE(OPCODE):
    """
    Get the block's beneficiary address
    """
    value = "0x41"
    gas = G_BASE


class TIMESTAMP(OPCODE):
    """
    Get the block's timestamp
    """
    value = "0x42"
    gas = G_BASE


class NUBMER(OPCODE):
    """
    Get the block's number
    """
    value = "0x43"
    gas = G_BASE


class DIFFICULTY(OPCODE):
    """
    Get the block's difficulty
    """
    value = "0x44"
    gas = G_BASE


class GASLIMIT(OPCODE):
    """
    Get the block's gas limit
    """
    value = "0x45"
    gas = G_BASE


class CHAINID(OPCODE):
    """
    Returns the current chain’s EIP-155 unique identifier
    """
    value = "0x46"
    gas = G_BASE


class POP(OPCODE):
    """
    Remove word from stack
    """
    value = "0x50"
    gas = G_BASE


class MLOAD(OPCODE):
    """
    Load word from memory
    """
    value = "0x51"
    gas = G_VERY_LOW


class MSTORE(OPCODE):
    """
    Save word to memory	
    """
    value = "0x52"
    gas = G_VERY_LOW


class MSTORE8(OPCODE):
    """
    Save byte to memory	
    """
    value = "0x53"
    gas = G_VERY_LOW


class SLOAD(OPCODE):
    """
    Load word from storage
    """
    value = "0x54"
    gas = 800


class SSTORE(OPCODE):
    """
    Save word to storage	
    """
    value = "0x55"
    gas = 20000


class JUMP(OPCODE):
    """
    Alter the program counter
    """
    value = "0x56"
    gas = G_MID


class JUMPI(OPCODE):
    """
    Conditionally alter the program counter
    """
    value = "0x57"
    gas = G_HIGH


class PC(OPCODE):
    """
    Get the value of the program counter prior to the increment corresponding to this instruction.
    """
    value = "0x58"
    gas = G_BASE


class MSIZE(OPCODE):
    """
    Get the size of active memory in bytes
    """
    value = "0x59"
    gas = G_BASE


class GAS(OPCODE):
    """
     Get the amount of available gas, including the corresponding reduction for the cost of this instruction.
    """
    value = "0x5a"
    gas = G_BASE


class JUMPDEST(OPCODE):
    """
    Mark a valid destination for jumps. This operation has no effect on machine state during execution.
    """
    value = "0x5b"
    gas = 1


class PUSH1(OPCODE):
    """
    Place 1 byte item on stack.
    """
    value = "0x60"
    gas = 3


class PUSH2(OPCODE):
    """
    Place 2 byte item on stack.
    """
    value = "0x61"
    gas = 3


class PUSH3(OPCODE):
    """
    Place 3 byte item on stack.
    """
    value = "0x62"
    gas = 3


class PUSH4(OPCODE):
    """
    Place 4 byte item on stack.
    """
    value = "0x63"
    gas = 3


class PUSH5(OPCODE):
    """
    Place 5 byte item on stack.
    """
    value = "0x64"
    gas = 3


class PUSH6(OPCODE):
    """
    Place 6 byte item on stack.
    """
    value = "0x65"
    gas = 3


class PUSH7(OPCODE):
    """
    Place 7 byte item on stack.
    """
    value = "0x66"
    gas = 3


class PUSH8(OPCODE):
    """
    Place 8 byte item on stack.
    """
    value = "0x67"
    gas = 3


class PUSH9(OPCODE):
    """
    Place 9 byte item on stack.
    """
    value = "0x68"
    gas = 3


class PUSH10(OPCODE):
    """
    Place 10 byte item on stack.
    """
    value = "0x69"
    gas = 3


class PUSH11(OPCODE):
    """
    Place 11 byte item on stack.
    """
    value = "0x6a"
    gas = 3


class PUSH12(OPCODE):
    """
    Place 12 byte item on stack.
    """
    value = "0x6b"
    gas = 3


class PUSH13(OPCODE):
    """
    Place 13 byte item on stack.
    """
    value = "0x6c"
    gas = 3


class PUSH14(OPCODE):
    """
    Place 14 byte item on stack.
    """
    value = "0x6d"
    gas = 3


class PUSH15(OPCODE):
    """
    Place 15 byte item on stack.
    """
    value = "0x6e"
    gas = 3


class PUSH16(OPCODE):
    """
    Place 16 byte item on stack.
    """
    value = "0x6f"
    gas = 3


class PUSH17(OPCODE):
    """
    Place 17 byte item on stack.
    """
    value = "0x70"
    gas = 3


class PUSH18(OPCODE):
    """
    Place 18 byte item on stack.
    """
    value = "0x71"
    gas = 3


class PUSH19(OPCODE):
    """
    Place 19 byte item on stack.
    """
    value = "0x72"
    gas = 3


class PUSH20(OPCODE):
    """
    Place 20 byte item on stack.
    """
    value = "0x73"
    gas = 3


class PUSH21(OPCODE):
    """
    Place 21 byte item on stack.
    """
    value = "0x74"
    gas = 3


class PUSH22(OPCODE):
    """
    Place 22 byte item on stack.
    """
    value = "0x75"
    gas = 3


class PUSH23(OPCODE):
    """
    Place 23 byte item on stack.
    """
    value = "0x76"
    gas = 3


class PUSH24(OPCODE):
    """
    Place 24 byte item on stack.
    """
    value = "0x77"
    gas = 3


class PUSH25(OPCODE):
    """
    Place 25 byte item on stack.
    """
    value = "0x78"
    gas = 3


class PUSH26(OPCODE):
    """
    Place 26 byte item on stack.
    """
    value = "0x79"
    gas = 3


class PUSH27(OPCODE):
    """
    Place 27 byte item on stack.
    """
    value = "0x7a"
    gas = 3


class PUSH28(OPCODE):
    """
    Place 28 byte item on stack.
    """
    value = "0x7b"
    gas = 3


class PUSH29(OPCODE):
    """
    Place 29 byte item on stack.
    """
    value = "0x7c"
    gas = 3


class PUSH30(OPCODE):
    """
    Place 30 byte item on stack.
    """
    value = "0x7d"
    gas = 3


class PUSH31(OPCODE):
    """
    Place 31 byte item on stack.
    """
    value = "0x7e"
    gas = 3


class PUSH32(OPCODE):
    """
    Place 32 byte item on stack.
    """
    value = "0x7f"
    gas = 3


class DUP1(OPCODE):
    """
    Duplicate 1st stack item.
    """
    value = "0x80"
    gas = 3


class DUP2(OPCODE):
    """
    Duplicate 2ne stack item.
    """
    value = "0x81"
    gas = 3


class DUP3(OPCODE):
    """
    Duplicate 3rd stack item.
    """
    value = "0x82"
    gas = 3


class DUP4(OPCODE):
    """
    Duplicate 4th stack item.
    """
    value = "0x83"
    gas = 3


class DUP5(OPCODE):
    """
    Duplicate 5th stack item.
    """
    value = "0x84"
    gas = 3


class DUP6(OPCODE):
    """
    Duplicate 6th stack item.
    """
    value = "0x85"
    gas = 3


class DUP7(OPCODE):
    """
    Duplicate 7th stack item.
    """
    value = "0x86"
    gas = 3


class DUP8(OPCODE):
    """
    Duplicate 8th stack item.
    """
    value = "0x87"
    gas = 3


class DUP9(OPCODE):
    """
    Duplicate 9th stack item.
    """
    value = "0x88"
    gas = 3


class DUP10(OPCODE):
    """
    Duplicate 10th stack item.
    """
    value = "0x89"
    gas = 3


class DUP11(OPCODE):
    """
    Duplicate 11th stack item.
    """
    value = "0x8a"
    gas = 3


class DUP12(OPCODE):
    """
    Duplicate 12th stack item.
    """
    value = "0x8b"
    gas = 3


class DUP13(OPCODE):
    """
    Duplicate 13th stack item.
    """
    value = "0x8c"
    gas = 3


class DUP14(OPCODE):
    """
    Duplicate 14th stack item.
    """
    value = "0x8d"
    gas = 3


class DUP15(OPCODE):
    """
    Duplicate 15th stack item.
    """
    value = "0x8e"
    gas = 3


class DUP16(OPCODE):
    """
    Duplicate 16th stack item.
    """
    value = "0x8f"
    gas = 3


class SWAP1(OPCODE):
    """
    2 Exchange 1st and 2nd stack item
    """
    value = "0x90"
    gas = 3


class SWAP2(OPCODE):
    """
    2 Exchange 1st and 3rd stack item
    """
    value = "0x91"
    gas = 3


class SWAP3(OPCODE):
    """
    2 Exchange 1st and 4th stack item
    """
    value = "0x92"
    gas = 3


class SWAP4(OPCODE):
    """
    2 Exchange 1st and 5th stack item
    """
    value = "0x93"
    gas = 3


class SWAP5(OPCODE):
    """
    2 Exchange 1st and 6th stack item
    """
    value = "0x94"
    gas = 3


class SWAP6(OPCODE):
    """
    2 Exchange 1st and 7th stack item
    """
    value = "0x95"
    gas = 3


class SWAP7(OPCODE):
    """
    2 Exchange 1st and 8th stack item
    """
    value = "0x96"
    gas = 3


class SWAP8(OPCODE):
    """
    2 Exchange 1st and 9th stack item
    """
    value = "0x97"
    gas = 3


class SWAP9(OPCODE):
    """
    2 Exchange 1st and 10th stack item
    """
    value = "0x98"
    gas = 3


class SWAP10(OPCODE):
    """
    2 Exchange 1st and 11th stack item
    """
    value = "0x99"
    gas = 3


class SWAP11(OPCODE):
    """
    2 Exchange 1st and 12th stack item
    """
    value = "0x9a"
    gas = 3


class SWAP12(OPCODE):
    """
    2 Exchange 1st and 13th stack item
    """
    value = "0x9b"
    gas = 3


class SWAP13(OPCODE):
    """
    2 Exchange 1st and 14th stack item
    """
    value = "0x9c"
    gas = 3


class SWAP14(OPCODE):
    """
    2 Exchange 1st and 15th stack item
    """
    value = "0x9d"
    gas = 3


class SWAP15(OPCODE):
    """
    2 Exchange 1st and 16th stack item
    """
    value = "0x9e"
    gas = 3


class SWAP16(OPCODE):
    """
    2 Exchange 1st and 17th stack item
    """
    value = "0x9f"
    gas = 3


class LOG0(OPCODE):
    """
    Append log record with no topics
    """
    value = "0xa0"
    gas = 375


class LOG1(OPCODE):
    """
    Append log record with 1 topic
    """
    value = "0xa1"
    gas = 750


class LOG2(OPCODE):
    """
    Append log record with 2 topics
    """
    value = "0xa2"
    gas = 1125


class LOG3(OPCODE):
    """
    Append log record with 3 topics
    """
    value = "0xa3"
    gas = 1500


class LOG4(OPCODE):
    """
    Append log record with 4 topics
    """
    value = "0xa4"
    gas = 1875


class CREATE(OPCODE):
    """
    Create a new account with associated code
    """
    value = "0xf0"
    gas = 32000


class CALL(OPCODE):
    """
    Message-call into an account
    """
    value = "0xf1"
    gas = 700


class CALLCODE(OPCODE):
    """
    Message-call into this account with alternative account's code
    """
    value = "0xf2"
    gas = 700


class RETURN(OPCODE):
    """
    Halt execution returning output data
    """
    value = "0xf3"
    gas = G_ZERO


class DELEGATECALL(OPCODE):
    """
    Message-call into this account with an alternative account's code, but persisting into this account with an
    alternative account's code
    """
    value = "0xf4"
    gas = 700


class CREATE2(OPCODE):
    """
    Create a new account with associated code.
    """
    value = "0xf5"
    gas = 32000


class STATICCALL(OPCODE):
    """
    Static message-call into an account.
    """
    value = "0xfa"
    gas = 40


class REVERT(OPCODE):
    """
    Halt execution reverting state changes but returning data and remaining gas.
    """
    value = "0xfd"
    gas = G_ZERO


class INVALID(OPCODE):
    """
    Designated invalid instruction.
    """
    value = "0xfe"
    gas = G_ZERO


class SELFDESTRUCT(OPCODE):
    """
    Halt execution and register account for later deletion.
    """
    value = "0xff"
    gas = 5000


def get_hex_value(item):
    if isinstance(item, str):
        return item
    elif isinstance(item, type):
        return item.value


test_program = [
    "0x00",
    "0x01",
    "0x30",
    "0x1234212",
    SELFDESTRUCT,
    INVALID,
    ADD
]


def get_hex_program(item_list):
    program = "0x"
    for item in item_list:
        program += get_hex_value(item)[2:]

    return program
