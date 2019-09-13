// Target

// for (i = 0; i < n; i++) {
//	arr[i] = -1;
//}
// let's say arr = 100, and n = 10
// set arr as 100, so memeory[100] + 10 will be initialized
@100
D=A
@arr
M=D

// set n as 10
@10
D=A
@n
M=D

// initialize i as 0
@i
M=0

(LOOP)
	// if i == n
	@i
	D=M
	@n
	D=D-M
		// end loop
		@END
		D;JEQ

	// else
	// arr[i] = -1
	@arr
	D=M
	@i
	A=D+M  // key point here, modifying the address
	M=-1

	// i++
	@i
	M=M+1
		// back to loop
	@LOOP
	0;JMP

(END)
@END
0;JMP