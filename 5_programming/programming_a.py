# BBF Bali Programming Test A
# Python 3.9.12
# by Andrew Willis
# Do not share!

# declare parameter
width = 60
height = 30
half_w = int(width/2)
half_h = int(height/2)

# declare constant
row_lis = []

# start loop
for row in range(height):
    if row < half_h:
        # generate 1st half of the pattern width and height
        if row == 0:
            to_print = ('x' * half_w)
        if 1<= row <= 4 or 11<= row <= 14:
            to_print = (int(half_w-(2*row)) * 'x') + (2 * '-')
        elif row == 5:
            to_print = (int((2*row)) * 'x') + (12 * '-')
        elif 6<=row or 10<=row:
            to_print = (10 * 'x') + (2 * '-')
        
        # fill the internal part of the pattern 
        to_print = to_print + (half_w-len(to_print))*'x'

        # generate 2nd half of the pattern width
        to_print = to_print + to_print[::-1]

        # insert to list for reverse
        row_lis.insert(0, to_print)
    else:
        # generate 2nd half of the pattern height
        to_print = row_lis[(row - half_h)]
    
    # print the result 
    print (to_print)
        