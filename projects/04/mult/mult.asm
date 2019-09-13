// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.	

//a = R0
//b = R1

//sum = 0

//LOOP:
//	if b > 0
//		sum = sum + a
//		b = b - 1
//		goto loop
//	else
//		goto end


@sum
M=0

(LOOP)
@R1
D=M
@LAST
D;JEQ
@R0
D=M
@sum
M=M+D
@R1
M=M-1
@LOOP
0;JMP

(LAST)
@sum
D=M
@R2
M=D
(END)
@END
0;JMP