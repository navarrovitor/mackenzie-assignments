### EXERCICIO 1 ###

# if ( x == y) go to L2

# a[1] = b - c;

# b = a[2] + c

# c = b + c[3];

# L2: a[4] = a[6] + a[5]

# a = $s0
# b = $s1
# c = $s2
# x = $s3
# y = $s4

# .data
# a:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# b:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# c:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# .text
# la $s0, a
# la $s1, b
# la $s2, c
# la $s3, 0
# la $s4, 1

# beq $s3, $s4, L2
#   lw $t0, 0 ($s1) # b 0 * 4
#   lw $t1, 0 ($s2) # c 0 * 4
#   sub $t2, $t0, $t1
#   sw $t2, 4 ($s0) # a[1] 1 * 4

#   lw $t0, 8 ($s0) # a[2] 2 * 4
#   lw $t1, 0 ($s2) # c 0 * 4
#   add $t2, $t0, $t1
#   sw $t2, 0 ($s1) # b 0 * 4

#   lw $t0, 0 ($s1) # b 0 * 4
#   lw $t1, 12 ($s2) # c[3] 3 * 4
#   add $t2, $t0, $t1
#   sw $t2, 0 ($s2) # c 0 * 4
  
#   j done

# L2:
#   lw $t0, 20 ($s0) # a[5] 5 * 4
#   lw $t1, 24 ($s0) # a[6] 6 * 4
#   add $t2, $t0, $t1
#   sw $t2, 16 ($s0) # a[4] 4 * 4

# done:

### EXERCICIO 2 - A ###

# .data
# a:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# b:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# c:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# .text
# la $s0, a
# la $s1, b
# la $s2, c
# la $s3, 0
# la $s4, 1

# # if (x == y): else: GO to else
# beq $s3, $s4, else
#   # b[1] = a[8] - c[3]
#   lw $t0, 32 ($s0) # a[8] 8 * 4
#   lw $t1, 12 ($s2) # c[3] 3 * 4
#   # t2 = a[8] - c[3]
#   sub $t2, $t0, $t1
#   sw $t2, 4 ($s1) # b[1] 1 * 4

#   j done

# else:
#   # c[2] = b[5] + a[3]
#   lw $t0, 20 ($s1) # b[5] 5 * 4
#   lw $t1, 12 ($s0) # a[3] 3 * 4
#   add $t2, $t0, $t1
#   sw $t2, 8 ($s2) # c[2] 2 * 4

# done:

### EXERCICIO 2 - B###

# .data
# a:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
# b:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# .text
# la $s0, a
# la $s1, b
# lw $s2, 0 ($s0) # a[0]
# lw $t0, 60 ($s0) # b[15]

# # while(a[0] != b[15]):
# while:
#   beq $s2, $t0, done
#   addi $s2, $s2, 1
#   j while
# done:

### EXERCICIO 2 - C ###

# .data
# a:  .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

# .text
# la $s0, a
# lw $s1, 0 ($s0) # a[0]
# addi $t0, $0, 16
# addi $s2, $0, 1

# # for(i=1, i < 17, i++)
# #   a[0] += i
# for:
#   beq $s2, $t0, done
#   add $s1, $s1, $s2
#   addi $s2, $s2, 1
#   j for

# done:

### EXERCICIO 3 ###

# .data
# a: .word 10,20,30,40,50,60,70,80,90,100
# saida: .word 0

# .text

# la $s0, 0
# la $s1 , 0 
# la $s2 , 0
# la $s3, a
# la $s4, saida

# li $t0, 10

# for:
#   beq $s0, $t0, done
#   sll $t1, $s0, 2
#   add $t2, $s3, $t1
#   lw $t3, 0($t2)
#   add $s1, $s1, $t3
#   addi $s0, $s0, 1
#   j for

# done: 
#   div $s2, $s1, $t0

# sw $s2, 0 ($s4)
