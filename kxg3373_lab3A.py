#NAME --- Kavya Sri Garikipati--------
#UTA ID: 1001953373
#DATE: April 15th, 2023
#------MAC OS--------
###############################################################################################################################################################################################################
#importing random and math modules in this way---------------------
import random
import math as m


def tab(space):
    gap = ''
    while space > 0: #----checking if space is greater than zero-----
        gap += ' '
        space -= 1
    return gap #returns gap

#init program
def init_program():
    print(tab(28) + 'Amazing Program') #printing amazing program
    print(tab(15) + 'Creative Computing Morristown, New Jersey') #printing 'CREATIVE COMPUTING MORRISTOWN'
    print('\n') #printing new line



    width, length = fetch_user_input()
    while width <= 1 or length <= 1: #checking if width and length are less than or equal to 1
        print('Meaningless Dimensions. Please try again.') #when incorrect dimensions are provided, printing please try again
        width, length = fetch_user_input() #fetching input
    return width, length #returns width and length


def fetch_user_input(): #fetching user input
    user_input = input('WHAT ARE YOUR WIDTH AND LENGTH? (For Example, type 10,10 and then press enter)\n') #asking for input: width and length
    width, length = user_input.split(',') #split function is used
    width, length = int(width), int(length) #declaring width and length
    return width, length #returns width and length

#init arrays
def init_arrays(k, V2):
    a,y  = [], []
    a.append([None] * V2)
    y.append([None] * V2)
    g = 1
    while g <= k:
        a.append([])
        y.append([])
        h = 1
        a[g].append(None)
        y[g].append(None)
        while h <= V2:
            a[g].append(0)
            y[g].append(0)
            h += 1
        g += 1

    return a, y


def first_line(j, k):
    l = ''
    g = 1
    while g <= k:
        if g == j:
            l += '.  '
        else:
            l += '.--'
        g += 1
    l += '.'
    print(l) #printing l


def search_non_explored_cell(t, k, u, V2): #searching non explored cells
    if t < k:
        t += 1
    elif u < V2:
        t = 1
        u += 1
    else:
        t, u = 1, 1

    return t, u


def maze_logic(j, a, y, k, V2): #maze logic

    b, f = 0, 0
    d = 1
    a[j][1] = d
    d += 1
    t, u = j, 1
    entry = 0

    while True:
        if entry == 2:
            t, u = search_non_explored_cell(t, k, u, V2)
            while a[t][u] == 0:
                t, u = search_non_explored_cell(t, k, u, V2)

        if entry == 0 and t-1 > 0 and a[t-1][u] == 0:

            if u-1 > 0 and a[t][u-1] == 0:
                if t<k and a[t+1][u] == 0:
                    j = m.floor(random.random()*3+1)
                elif u < V2:
                    if a[t][u+1] == 0:
                        j = m.floor(random.random() * 3 + 1)
                        if j == 3:
                            j = 4
                    else:
                        j = m.floor(random.random() * 2 + 1)
                elif f == 1:
                    j = m.floor(random.random() * 2 + 1)
                else:
                    b = 1
                    j = m.floor(random.random() * 3 + 1)
                    if j == 3:
                        j = 4
            elif t < k and a[t+1][u] == 0:
                if u < V2:
                    if a[t][u + 1] == 0:
                        j = m.floor(random.random() * 3 + 1)
                    else:
                        j = m.floor(random.random() * 2 + 1)
                    if j >= 2:
                        j += 1
                elif f == 1:
                    j = m.floor(random.random() * 2 + 1)
                    if j >= 2:
                        j += 1
                else:
                    b = 1
                    j = m.floor(random.random() * 3 + 1)
                    if j >= 2:
                        j += 1
            elif u < V2:
                if a[t][u + 1] == 0:
                    j = m.floor(random.random() * 2 + 1)
                    if j == 2:
                        j = 4
                else:
                    j = 1
            elif f == 1:
                j = 1
            else:
                b = 1
                j = m.floor(random.random() * 2 + 1)
                if j == 2:
                    j = 4
        elif u-1 > 0 and a[t][u-1] == 0:
            if t < k and a[t + 1][u] == 0:
                if u < V2:
                    if a[t][u + 1] == 0:
                        j = m.floor(random.random() * 3 + 2)
                    else:
                        j = m.floor(random.random() * 2 + 2)
                elif f == 1:
                    j = m.floor(random.random() * 2 + 2)
                else:
                    b = 1
                    j = m.floor(random.random() * 3 + 2)
            elif u < V2:
                if a[t][u + 1] == 0:
                    j = m.floor(random.random() * 2 + 2)
                    if j == 3:
                        j = 4
                else:
                    j = 2
            elif f == 1:
                j = 2
            else:
                b = 1
                j = m.floor(random.random() * 2 + 2)
                if j == 3:
                    j = 4

        elif t < k and a[t+1][u] == 0:
            if u < V2:
                if a[t][u+1] == 0:
                    j = m.floor(random.random() * 2 + 3)
                else:
                    j = 3
            elif f == 1:
                j = 3
            else:
                b = 1
                j = m.floor(random.random() * 2 + 3)
        elif u < V2:
            if a[t][u + 1] == 0:
                j = 4
            else:
                entry = 2
                continue
        elif f == 1:
            entry = 2 # here it is blocked
            continue
        else:
            b = 1
            j = 4

        if j == 1:
            a[t-1][u] = d
            d += 1
            y[t-1][u] = 2
            t -= 1
            if d == k * V2 + 1:
                break
            b = 0
            entry = 0
        elif j == 2:
            a[t][u-1] = d
            d += 1
            y[t][u-1] = 1
            u -= 1
            if d == k * V2 + 1:
                break
            b = 0
            entry = 0
        elif j == 3:
            a[t + 1][u] = d
            d += 1
            if y[t][u] == 0:
                y[t][u] = 2
            else:
                y[t][u] = 3
            t += 1
            if d == k * V2 + 1:
                break
            entry = 1
        elif j == 4:
            if b != 1:
                a[t][u + 1] = d
                d+=1
                if y[t][u] == 0:
                    y[t][u] = 1
                else:
                    y[t][u] = 3
                u+=1
                if d == k * V2 + 1:
                    break
                entry = 0
            else:
                f = 1
                if y[t][u] == 0:
                    y[t][u] = 1
                    b = 0
                    t = 1
                    u = 1
                    while a[t][u] == 0:
                        if t < k:
                            t += 1
                        elif u < V2:
                            t = 1
                            u += 1
                        else:
                            t = 1
                            u = 1
                    entry = 0
                else:
                    y[t][u] = 3
                    b = 0
                    entry = 2

    return y


def print_maze(y, k, V2):  #printing maze
    h = 1
    while h <= V2:
        ps = 'I'
        g = 1
        while g <= k:
            if y[g][h] < 2:
                ps += '  I'
            else:
                ps += '   '
            g += 1

        print(ps)

        ps = ''
        g = 1
        while g <= k:
            if y[g][h] == 0 or y[g][h] == 2:
                ps += ':--'
            else:
                ps += ':  '
            g += 1
        print(ps + '.')
        h += 1


def main(): #main function implementation-----------------------------
    k, V2 = init_program()
    a, y = init_arrays(k, V2)

    j = m.floor(random.random() * k + 1)
    first_line(j, k)

    y = maze_logic(j, a, y, k, V2)

    print_maze(y, k, V2) #prints maze


if __name__ == '__main__':
    main()