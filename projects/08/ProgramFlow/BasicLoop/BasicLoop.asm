@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@0
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
(LOOP_START)
@ARG
D=M
@0
D=D+A
@addr
M=D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@0
D=D+A
@addr
M=D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
@LCL
D=M
@0
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
@ARG
D=M
@0
D=D+A
@addr
M=D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
@ARG
D=M
@0
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
@ARG
D=M
@0
D=D+A
@addr
M=D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JGT
@LCL
D=M
@0
D=D+A
@addr
M=D
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
(END)
@END
0;JMP