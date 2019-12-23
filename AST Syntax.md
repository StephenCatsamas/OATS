op
==
operator of form a op b

    in          (in)
        child 0:    LHS block
        child 1:    RHS block

    set         (=)
        child 0:    LHS block
        child 1:    RHS block

    is          (==)
        child 0:    LHS block
        child 1:    RHS block

crtl
====
control structures

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

func
====
functions with arguments

    @name       (@name)
        child n:    argument block

def
===
define classes and functions and other things
    
    func        (def)
        child 0:    func.@name
        child 1:    body block
        
    class        (class)
        child 1:    func.@name
        child 0:    body block

block
=====
indented block

    child n:        code line
    
var
===
variable

    @name       (@name)

basic
=====
integer

    @number     (@number)

synt
====
syntax strings

    @string     (@string)