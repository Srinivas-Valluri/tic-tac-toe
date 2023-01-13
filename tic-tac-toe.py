#first player starts with X
grid = [['-','-','-'],['-','-','-'],['-','-','-']]

def display():
    for i in grid:
        print(i)

def choose():
    choice_list = ['X','O','X','O','X','O','X','O','X']
    choice_cnt=0
    valid_input=[0,1,2]
    while choice_cnt<9:
        #row=int(input('Enter the row: '))
        #col=int(input('Enter the col: '))
        row, col = list(map(int, input("Enter row and col: ").split()))
        if row in valid_input and col in valid_input:
            grid[row][col]=choice_list[choice_cnt]
            choice_cnt+=1
        display()



display()
choose()