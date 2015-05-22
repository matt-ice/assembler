import os
from processing import *

# reset label and variable counter
var_count = 0
ignore_count = 0
line_number = 0

def decrease_line_number():
    global line_number
    line_number-=1
print(os.getcwd())

# file to be processed
open_string = "Rect"


hack_out = open(open_string +".hack", "w+")
asm_in = open(open_string +".asm")
asm_out = open(open_string +"-out.hack", "w+")
asm_out2 = open(open_string+"-out2.hack", "w+")
line = "x"

# get line count
for i, l in enumerate(asm_in):
    pass

asm_len = i + 1
print(asm_len)

# set focus at the beginning of file
asm_in.seek(0, 0)

for run in range(1, 4):
    global ignore_count, line_number
    # ignore_count used to determine instruction number
    ignore_count = 0
    line_number = 0
    asm_out.seek(0,0)
    asm_out2.seek(0,0)
    # cycle through lines in file
    for i in range(0, asm_len):
        if run == 1:
            rline = asm_in.readline()
        elif run == 2:
            rline = asm_out.readline()
        elif run == 3:
            rline = asm_out2.readline()
        line = ''.join(rline.split())
        if run == 3 and line in ("","L","//"):
            continue

        # print(line)
        if rem_comment(line) != "//":
            line = rem_comment(line)
            pc = i - (ignore_count)
            send = run_through(line_number, run, line)
            if send == "L" or send == "" or send == "//" or send is None:
                ignore_count += 1
            else:
                line_number += 1
        else:
            send = "//"
            ignore_count += 1

        send = send + "\n"
        #print(send)
        # print only binary code to machine language file
        if send is not None and len(send) > 1 and run == 3:
            hack_out.write(send)
            hack_out.flush()
            os.fsync(hack_out)
        # print all lines to temp files
        if run == 1:
            asm_out.write(send)
            asm_out.flush()
            os.fsync(asm_out)
        elif run == 2:
            asm_out2.write(send)
            asm_out2.flush()
            os.fsync(asm_out2)

os.fsync(hack_out)
hack_out.close()
asm_in.close()
asm_out.close()
asm_out2.close()
print("Done")
