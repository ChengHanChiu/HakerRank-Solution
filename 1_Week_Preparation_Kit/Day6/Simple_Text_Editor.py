

if __name__ == '__main__':
    
    q = int(input())

    s = ''
    edit_history = []

    for i in range(q):
        
        operation = input().rstrip().split()
        
        match int(operation[0]):               
            case 1:                             # append(W) - Append string W to the end of S.
                edit_history.append(s)
                s += operation[1]               
            case 2:                             # delete(k) - Delete the last k characters of S.
                edit_history.append(s)          
                s = s[:-int(operation[1])]
            case 3:                             # print(k) - Print the kth character of S.
                print(s[int(operation[1])-1])
            case 4:                             # undo() - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.
                s = edit_history.pop()