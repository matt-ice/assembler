from tables import *

def decrease_line_number():
    global line_number
    line_number-=1

def process_a(instr):
    if "=" in instr:
        after_eq = instr.partition("=")[2]
        comp = after_eq.partition(";")[0]
    try:
        if "M" in comp:
            send="M"
        else:
            send="A"
    except:
        send="A"
    return get_a(send)

def process_comp(instr):
    if "="in instr:
        after_eq = instr.partition("=")[2]
        send = after_eq.partition(";")[0]
    else:
        send = instr.partition(";")[0]
    return get_comp(send)

def process_dest(instr):
    if "=" in instr:
        send = instr.partition("=")[0]
    else:
        send="null"
    return get_dest(send)

def process_jmp(instr):
    if ";" in instr:
        send = instr.partition(";")[2]
    else:
        send = "null"
    return get_jmp(send)

def process_Ainstr(instr):
    return "0" + format(int(instr[1:]),"015b")

def rem_comment(line):
    rem = line.find("//")
    if rem >0:
        return line[0:rem]
    elif rem == 0:
        return "//"
    elif rem is None:
        return "//"
    else:
        return line

def process_instr(instr):
    if "@" in instr:
        return process_Ainstr(instr)
    a = process_a(instr)
    comp = process_comp(instr)
    dest = process_dest(instr)
    jmp = process_jmp(instr)
    return "111" + a + comp + dest + jmp


def run_through(line_number, run, line):
    if run == 1:
        return first_run(line_number, line)
    elif run == 2:
        return second_run(line_number, line)
    elif run == 3:
        return final_run(line)

def first_run(pc,instr):
    send=instr
    # check for labels
    if len(instr)==0:
        send= "//"
    elif instr[0]=="(":
        # check if previous line was a label
        # if get_predef_exist(pc):
        #     set_predef_value(pc)
        #     decrease_line_number()
        #     pc-=1
        update_predef(instr.strip("()"),pc)
        send = "L"
    elif "@" in instr:
        if get_predef(instr[1:]) != False:
            send = "@" + str(get_predef(instr[1:]))
    else:
        send = instr
    return send

def second_run(pc,instr):
    send=""
    if "@" in instr:
        if instr[1:].isnumeric():
            send=instr
        elif get_predef(instr[1:]) != False:
            send = "@" + get_predef(instr[1:])
        elif get_predef(instr[1:]) == False:
            inc_var_count()
            update_predef(instr[1:],16+var_count)
            send = "@" + get_predef(instr[1:])
    else:
        send = instr
    return send

def final_run(instr):
    return process_instr(instr)

def inc_var_count():
    global var_count
    if get_predef_exist(16):
        var_count+=1
    else:
        var_count=0