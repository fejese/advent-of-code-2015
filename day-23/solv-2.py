#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

program = []
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        parts = line.strip().split(" ")
        command = [
            parts[0],
            int(parts[1])
            if parts[1].lstrip("-+").isnumeric()
            else parts[1].rstrip(","),
        ]
        if len(parts) > 2:
            command.append(int(parts[2]))

        program.append(command)

reg = {"a": 1, "b": 0}
pos = 0
while 0 <= pos < len(program):
    cmd = program[pos]
    print(f"pos: {pos:2d} reg: {str(reg):25s} cmd: {str(cmd):20s}", end="")
    if cmd[0] == "inc":
        reg[cmd[1]] += 1
        pos += 1
    elif cmd[0] == "tpl":
        reg[cmd[1]] *= 3
        pos += 1
    elif cmd[0] == "hlf":
        reg[cmd[1]] //= 2
        pos += 1
    elif cmd[0] == "jmp":
        pos += cmd[1]
    elif cmd[0] == "jie":
        if reg[cmd[1]] % 2 == 0:
            pos += cmd[2]
        else:
            pos += 1
    elif cmd[0] == "jio":
        if reg[cmd[1]] == 1:
            pos += cmd[2]
        else:
            pos += 1
    print(f" => pos: {pos:2d} reg: {str(reg):25s}")
