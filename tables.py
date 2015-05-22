table_a = {"A":"0",
           "M":"1"}
table_dest = {  "null" : "000",
                "M" : "001",
                "D" : "010",
                "MD" : "011",
                "A" : "100",
                "AM" : "101",
                "AD" : "110",
                "AMD" : "111"}


table_comp = {  "null":"000000",
                "0" : "101010",
                "1" : "111111",
                "-1" : "111010",
                "D" : "001100",
                "A" : "110000",
                "M" : "110000",
                "!D" : "001101",
                "!A" : "110001",
                "!M" : "110001",
                "-D" : "001111",
                "-A" : "110011",
                "-M" : "110011",
                "D+1" : "011111",
                "1+D" : "011111",
                "1+A" : "110111",
                "A+1" : "110111",
                "1+M" : "110111",
                "M+1" : "110111",
                "1-D" : "001110",
                "D-1" : "001110",
                "1-A" : "110010",
                "A-1" : "110010",
                "1-M" : "110010",
                "M-1" : "110010",
                "D+A" : "000010",
                "A+D" : "000010",
                "D+M" : "000010",
                "M+D" : "000010",
                "A-D" : "000111",
                "D-A" : "010011",
                "M-D" : "000111",
                "D-M" : "010011",
                "D&A" : "000000",
                "A&D" : "000000",
                "D&M" : "000000",
                "M&D" : "000000",
                "D|A" : "010101",
                "A|D" : "010101",
                "D|M" : "010101",
                "M|D": "010101"}


table_jmp = {   "null":"000",
                "JGT": "001",
                "JEQ": "010",
                "JGE": "011",
                "JLT": "100",
                "JNE": "101",
                "JLE": "110",
                "JMP": "111"}


table_predef={
        "SP" : 0,
        "LCL" : 1,
        "ARG" : 2,
        "THIS" : 3,
        "THAT" : 4,
        "R0" : 0,
        "R1" : 1,
        "R2" : 2,
        "R3" : 3,
        "R4" : 4,
        "R5" : 5,
        "R6" : 6,
        "R7" : 7,
        "R8" : 8,
        "R9" : 9,
        "R10" : 10,
        "R11" : 11,
        "R12" : 12,
        "R13" : 13,
        "R14" : 14,
        "R15" : 15,
        "SCREEN" : 16384,
        "KBD" : 24576
    }

def get_a(a):
    return table_a[a]

def get_dest(dest):
    return table_dest[dest]

def get_comp(comp):
    return table_comp[comp]

def get_jmp(jmp):
    return table_jmp[jmp]

def get_predef(predef):
    if predef in table_predef:
        return str(table_predef[predef])
    else:
        return False
def get_predef_exist(value):
    if value in table_predef.values():
        return True
    else:
        return False

def update_predef(key,value):
    table_predef.update({key:value})
    print(table_predef[key])

def set_predef_value(old_value):
    for entry in table_predef.items():
        if table_predef[entry] == old_value:
            table_predef[entry] = old_value-1

