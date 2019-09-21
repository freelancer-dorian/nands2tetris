@510
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop temp 6- arg1 temp- arg2 6- cmd type: C_POP
@R5
D=M
@6
D=D+A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D