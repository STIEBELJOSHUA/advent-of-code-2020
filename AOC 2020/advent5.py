#--question 1--
with open ('input','r') as file:
    passes = file.read().strip().split('\n')

def find_row(rows, board_pass):
    if len(rows)==1:
        return rows[0]
    elif board_pass[0] in ('B','R'):
        #crate image of pixels with rows lit up (use master image as base,but dont edit original) and save it 
        return find_row(rows[len(rows)//2:], board_pass[1:])
    elif board_pass[0] in ('F','L'):
        #create image of pixels with rows lit up (use master image as base, but dont edit original) and save it
        return find_row(rows[:len(rows)//2], board_pass[1:])

#create master image
def get_ticket_ids(tickets):
    board_pass_ids = []
    for board_pass in passes:
        rows = [i for i in range(0,128)]
        column = [i for i in range(0,8)]
        row = find_row(rows, board_pass[:7])
        column = find_row(column, board_pass[-3:])
        board_pass_ids.append(row*8+column)
        #add green pixel to master image and save it
    board_pass_ids.sort()
    return board_pass_ids

#--question 2--
def find_missing_ticket(tickets):
    for i in range(1,len(tickets)):
        if tickets[i]-1 != tickets[i-1]:
            return tickets[i]-1

#answer to part 1
board_pass_ids = get_ticket_ids(passes)
print(max(board_pass_ids))
#answer to part 2
print(find_missing_ticket(board_pass_ids))

#wow I did this stupidly
#fuck I'm dumbo. This shit was just a binary number from the fucking brrbrflf code thing to 1010101001
