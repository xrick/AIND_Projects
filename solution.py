def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows,cols)
unitlist = []
units = {}
peers = {}

def create_board():
    global unitlist, units, peers
    row_units = [cross(r,cols) for r in rows]
    col_units = [cross(rows,c) for c in cols]
    square_units =[cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    unitlist = row_units + col_units + square_units
    diagonal1 = [r + c for r, c in zip(rows, cols)]
    diagonal2 = [r + c for r, c in zip(rows, sorted(cols, reverse=True))]
    unitlist.append(diagonal1)
    unitlist.append(diagonal2)
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[])) - set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy)
    return values

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    boxes_with_two_values = [box for box in values.keys() if len(values[box]) == 2]
    for box in boxes_with_two_values:
        d1 = values[box][0]
        d2 = values[box][1]
        for peer in peers[box]:
            if values[peer] == values[box]:
                for unit in units[box]:
                    if peer in unit:
                        for square in unit:
                            if square != peer and square != box:
                                assign_value(values, square, values[square].replace(d1,''))
                                assign_value(values, square, values[square].replace(d2,''))
                                if square in boxes_with_two_values:
                                    boxes_with_two_values.remove(square)
    return values 


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits ='123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes,chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    rows = 'ABCDEFGHI'
    cols = '123456789'
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width).center(width) + ('|' if c in '36' else '') 
        for c in cols))

        if r in 'CF':
            print(line)
    print()


def eliminate(values):
    solved_boxes = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_boxes:
        digits =  values[box]
        for peer in peers[box]:
            if len(values[peer]) > 1:
                assign_value(values, peer, values[peer].replace(digits,''))
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in "123456789":
            digit_exist = [box for box in unit if digit in values[box]]
            if len(digit_exist) == 1:
                assign_value(values, digit_exist[0], digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if not values:
        return False

    if all(len(values[box]) == 1 for box in boxes):
        return values
    
    min_pos, square = min((len(values[square]), square) for square in boxes if len(values[square]) > 1)

    for value in values[square]:
        new_grid = values.copy()
        new_grid = assign_value(new_grid, square, value)
        tried = search(new_grid)
        if tried:
            return tried

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    create_board()
    return search(grid_values(grid))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')