//// call f n
//	// push return-addr
//	@return_after_%s
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push LCL
//	@LCL
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push ARG
//	@ARG
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push THIS
//	@THIS
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push THAT
//	@THAT
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// ARG = SP - n - 5
//	// push SP addr
//	@SP
//	D=M
//	A=M
//	M=D
//	@SP
//	M=M+1
//	//push constant n- arg1 constant- arg2 n- cmd type: C_PUSH
//	@%s
//	D=A
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//
//	//push constant 5- arg1 constant- arg2 5- cmd type: C_PUSH
//	@5
//	D=A
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//
//	//add- cmd type: C_ARITHMETIC
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@SP
//	M=M-1
//	A=M
//	M=M+D
//	@SP
//	M=M+1
//
//	//sub- cmd type: C_ARITHMETIC
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@SP
//	M=M-1
//	A=M
//	M=M-D
//	@SP
//	M=M+1
//
//	// LCL = SP
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@ARG
//	M=D
//	// goto f
//	@%s
//	0;JMP
//	// (return-addr after f)
//	(return_after_%s)

// return 

//	FRAME = LCL
@LCL
D=M
@FRAME
M=D

//	*ARG = pop()
//pop argument 0- arg1 argument- arg2 0- cmd type: C_POP
@ARG
D=M
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//	SP = ARG + 1
@ARG
D=M
@SP
M=D+1
//	THAT = *(FRAME - 1)
//	THIS = *(FRAME - 2)
//push addr(FRAME)- arg1 temp- arg2 0- cmd type: C_PUSH
@FRAME
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 1- arg1 constant- arg2 1- cmd type: C_PUSH
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
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

//pop pointer 1 -- THAT
@SP
M=M-1
A=M
D=M
@THAT
M=D

////push FRAME
@FRAME
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 2- arg1 constant- arg2 2- cmd type: C_PUSH
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
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

//pop pointer 0 THIS
@SP
M=M-1
A=M
D=M
@THIS
M=D
//	ARG = *(FRAME - 3)
////push FRAME
@FRAME
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 3
@3
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
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

//pop to ARG
@SP
M=M-1
A=M
D=M
@ARG
M=D
//	LCL = *(FRAME - 4)
////push FRAME
@FRAME
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
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

//pop LCL
@SP
M=M-1
A=M
D=M
@LCL
M=D

//	RET = *(FRAME - 5)
////push FRAME
@FRAME
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 5
@5
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
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

// pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
// goto RET
@5
M=M
0;JMP
