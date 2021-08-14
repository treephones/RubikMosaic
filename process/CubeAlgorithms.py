#colours as numbers (temporary)
white = 1
yellow = 6
red = 2
orange = 5
green = 3
blue = 4


list_of_cubefaces = [
  [[red, red, red],
  [red, red, red],
  [red, red, red]],

  [[red, orange, red],
  [red, red, red],
  [green, red, yellow]],
]

centerpiece = list_of_cubefaces[0][1][1]

input = []
output = []
counter = 0

#converting everything from the face into an array
for i in list_of_cubefaces[0]:
    for j in i:
        if counter != 4:
            input.append(j)
        counter+=1

counter = 0
for i in list_of_cubefaces[1]:
    for j in i:
        if counter != 4:
            output.append(j)
        counter+=1

#returns the index of the different values in the lists in their respective order
def difference_in_lists (output): #input and output have to be the same length
    differences = [["", "", "", ""], ["", "", "", ""]]
    for i in range(0, len(output)):
        if input[i] != output[i]:
            if is_edge_piece(i):
                differences[0][edge_index(i, True)] = output[i]
            else:
                differences[1][edge_index(i, False)] = output[i]

    return differences


def is_edge_piece(index):
    edge = [1,3,4,6]
    return index in edge

def edge_index(index, is_edge):
    edge = [1,3,4,6]
    corner = [0,2,5,7]
    if is_edge:
        return edge.index(index)

    return corner.index(index)


def kill_char(string, n): # n = position of which character you want to remove
    begin = string[:n]    # from beginning to n (n not included)
    end = string[n+1:]    # n+1 through end of string
    return begin + end

def move_reverse(moveset):
    reversed = []
    moveset.reverse()
    for move in moveset:
        if move[-1] == "'":
            reversed.append(kill_char(move, len(move)-1))
        elif move[-1] == "2":
            reversed.append(move)
        else:
            reversed.append(move+"'")

    return reversed

def instructions(output):
    T_perm = ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"]
    Y_perm = ["R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R"]
    cube_labels = {
        white: ["A", "B", "C", "D"],
        green: ["E", "F", "G", "H"],
        red: ["I", "J", "K", "L"],
        blue: ["M", "N", "O", "P"],
        orange: ["Q", "R", "S", "T"],
        yellow: ["U", "V", "W", "X"]
    }
    ret = []

    difference_list = difference_in_lists(output)

    print("EDGE")
    for i in difference_list[0]:
        if i != '':
            label = cube_labels[i][0] #current cube label
            offset_label = offset(centerpiece, label) #returns the offsetted label if the centerpiece isn't red
            setup = edge_setup_move(offset_label) #returns the setup move to swap pieces

            ret.extend(setup)
            ret.extend(T_perm)
            ret.extend(move_reverse(setup))

            label = cube_labels[centerpiece][difference_list[0].index(i)]
            offset_label = offset(centerpiece, label) #returns the offsetted label if the centerpiece isn't red
            setup = edge_setup_move(offset_label) #returns the setup move to swap pieces

            ret.extend(setup)
            ret.extend(T_perm)
            ret.extend(move_reverse(setup))


    cube_labels[centerpiece].pop(0)#deletes the current label from the dictionary so it doesn't get reused


    cube_labels = {
        white: ["A", "B", "C", "D"],
        green: ["E", "F", "G", "H"],
        red: ["I", "J", "K", "L"],
        blue: ["M", "N", "O", "P"],
        orange: ["Q", "R", "S", "T"],
        yellow: ["U", "V", "W", "X"]
    }

    print("CORNER")
    for i in difference_list[1]:#corners tbd
        if i != '':
            label = cube_labels[i][0]  # current cube label

            offset_label = offset(centerpiece, label)  # returns the offsetted label if the centerpiece isn't red
            setup = corner_setup_move(offset_label)  # returns the setup move to swap pieces
            #print("corner piece")

            ret.extend(setup)
            ret.extend(Y_perm)
            ret.extend(move_reverse(setup))

            label = cube_labels[centerpiece][difference_list[1].index(i)]
            offset_label = offset(centerpiece, label)  # returns the offsetted label if the centerpiece isn't red
            setup = corner_setup_move(offset_label)  # returns the setup move to swap pieces

            ret.extend(setup)
            ret.extend(Y_perm)
            ret.extend(move_reverse(setup))

        cube_labels[centerpiece].pop(0)#deletes the current label from the dictionary so it doesn't get reused

    return ret


def edge_setup_move(piece):
    if piece == "A":
        return ["Lw2", "D", "L2"]
    elif piece == "C": #D and B doesn't need setup moves
        return ["Lw2", "D'", "L2"]
    elif piece == "E":
        return ["L'", "Dw", "L'"]
    elif piece == "F":
        return ["Dw'", "L"]
    elif piece == "G":
        return ["L", "Dw", "L'"]
    elif piece == "H":
        return ["Dw", "L'"]
    elif piece == "I":
        return ["Lw", "D'", "L2"]
    elif piece == "J":
        return ["Dw2", "L"]
    elif piece == "K":
        return ["Lw", "D'", "L2"]
    elif piece == "L":
        return ["L'"]
    elif piece == "M":
        return ["J perm"]
    elif piece == "N":
        return ["Dw", "L"]
    elif piece == "O":
        return ["D2", "L'", "Dw'", "L"]
    elif piece == "P":
        return ["Dw'", "L'"]
    elif piece == "Q":
        return ["Lw'", "D", "L2"]
    elif piece == "R":
        return ["L"]
    elif piece == "S":
        return ["Lw'", "D'", "L2"]
    elif piece == "T":
        return ["Lw2", "L'"]

def corner_setup_move(piece):
    if piece == "A":
        return "Y_perm"
    elif piece == "B":
        return ["R", "D'"]
    elif piece == "C":
        return ["F"]
    elif piece == "D":
        return ["F", "R'"]
    elif piece == "E":
        return []
    elif piece == "F":
        return ["F2"]
    elif piece == "G":
        return ["D2", "R"]
    elif piece == "H":
        return ["D2"]
    elif piece == "I":
        return ["F'", "D"]
    elif piece == "J":
        return ["F2", "D"]
    elif piece == "K":
        return ["D", "R"]
    elif piece == "L":
        return ["D"]
    elif piece == "M":
        return ["R'"]
    elif piece == "N":
        return ["R2"]
    elif piece == "O":
        return ["R"]
    elif piece == "P":
        return "Y_perm"
    elif piece == "Q":
        return ["R'", "F"]
    elif piece == "T":
        return ["D'"]
    elif piece == "S":
        return ["D'", "R"]
    elif piece == "U":
        return ["F'"]
    elif piece == "V":
        return ["D'", "F'"]
    elif piece == "W":
        return ["D2", "F'"]
    elif piece == "X":
        return ["D", "F'"]

def offset(centerpiece, label):
    if centerpiece == white:
        return chr(ord(label)-8)
    elif centerpiece == red:
        return label
    elif centerpiece == blue:
        return (chr(ord(label) + 4))
    elif centerpiece == green:
        return (chr(ord(label) - 4))
    elif centerpiece == orange:
        return (chr(ord(label) + 8))
    elif centerpiece == yellow:
        return (chr(ord(label) + 12))
