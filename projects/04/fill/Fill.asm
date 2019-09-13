// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


//LOOP:
//	addr = SCREEN
//	n = 8192
//	i = 0
//	read key
//	if key is empty
//		value = 0
//	else
//		value = 1
//
//
//		LOOP_HANDLE_SCREEN:
//			if i>n
//				back to loop
//			addr[i] = value
//			i++
//			goto LOOP_HANDLE_SCREEN



@flag
M=0

(LOOP)
@SCREEN
D=A
@addr
M=D

@8192
D=A
@n
M=D

@i
M=0

@KBD
D=M
@CLEAN
D;JEQ
@FILL
0;JMP


(CLEAN)
@flag
D=M
@LOOP
D;JEQ
@flag
M=0
(CLEAN_LOOP)
@i
D=M
@n
D=D-M
@LOOP
D;JGT
@addr
A=M
M=0
@addr
M=M+1
@i
M=M+1
@CLEAN_LOOP
0;JMP

(FILL)
@flag
D=M
@LOOP
D;JGT
@flag
M=1
(FILL_LOOP)
@i
D=M
@n
D=D-M
@LOOP
D;JGT
@addr
A=M
M=-1
@addr
M=M+1
@i
M=M+1
@FILL_LOOP
0;JMP