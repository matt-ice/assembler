//
//
//
//
//
//
//
//
@0
D=M
@INFINITE_LOOP
D;JLE
@counter
M=D
@16384
D=A
@address
M=D
L
@address
A=M
M=-1
@address
D=M
@32
D=D+A
@address
M=D
@counter
MD=M-1
@10
D;JGT
L
@23
0;JMP