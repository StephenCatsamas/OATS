#operator of form a op b
op
    in          (in)
        child 0:    LHS block
        child 1:    RHS block

    set         (=)
        child 0:    LHS block
        child 1:    RHS block

    is          (==)
        child 0:    LHS block
        child 1:    RHS block

#control structures
crtl
    for         (for)
        child 0:    condition block
        child 1:    body block

    if          (if)
        child 0:    condition block
        child 1:    body block

    while       (while)
        child 0:    condition block
        child 1:    body block

    continue    (continue)

    break       (break)

    return      (return)
        child n:    argument block

#functions with arguments
func
    @name       (@name)
        child n:    argument block

#indented block
block
    child n:        code line
    
#variable
var
    @name       (@name)

#integer
basic
    @number     (@number)

#syntax strings
synt
    @string     (@string)