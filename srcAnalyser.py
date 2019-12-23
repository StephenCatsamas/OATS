import Compiler as ASTtools


fp = "Example.oat"
op = "comp.py"

AST = ASTtools.AST("root")

with open(fp, 'r') as srcf:
    src = srcf.read()
    print(src)

keywords = ["type"]

srcLines = list()

ilst = 0
for i, char in enumerate(src):
    if char == "\n":
        flushline = src[ilst:i].strip()
        if flushline != "":
            words = flushline.split()
            srcLines.append(words)
            ilst = i+1
    if char in ["{","}","(",")"]:
        flushline = src[ilst:i].strip()
        if flushline != "":
            words = flushline.split()
            srcLines.append(words)
            srcLines.append([src[i]])
            ilst = i + 1
    if char == ",":
        flushline = src[ilst:i].strip()
        if flushline != "":
            words = flushline.split()
            srcLines.append(words)
            ilst = i + 1

leaf = AST

types = ["int", "string", "hsdfs", "void", "basic"]
funcs = ["set"]

for line in srcLines:
    print("newline: ", end = "")
    print(line)

for line in srcLines:
    print()
    print("newline: ", end="")
    print(line)
    print()
    print(leaf)
    print()

    if line[0] == "type":
        leaf = leaf.add_child("def", "class")
        leaf.add_child("func", line[1])
    if line[0] == "{":
        if leaf.name != "classfunc":
            leaf = leaf.add_child("block")
    if line[0] == "}":
        if leaf.name != "classfunc":
            leaf = leaf.ascend()

    if line[0] == "}":
        if leaf.name == "prop":
            leaf = leaf.ascend()
    if line[0] == "prop":
        leaf = leaf.add_child("def", "prop")
        leaf = leaf.add_child("func", "__init__")
        leaf = leaf.ascend()

    if leaf.ascend().name == "prop":
        if line[0] in types:
            leaf = leaf.add_child("op", "set")
            leaf.add_child("var", line[1])
            leaf.add_child("func", line[0])
            leaf = leaf.ascend()

    if line[0] == "func":
        leaf = leaf.add_child("def", "classfunc")

    if leaf.key == "func":
        if line[0] in types:
            leaf.add_child("var", line[1])

    if leaf.name == "classfunc":
        if line[0] in types:
            leaf = leaf.add_child("def", "func")
            leaf = leaf.add_child("func", line[1])

    if leaf.key == "func":
        if line[0] == "(":
            pass
        if line[0] == ")":
            leaf = leaf.ascend()
    try:
        if line[1] == "=":
            leaf = leaf.add_child("op", "set")
            leaf.add_child("var", line[0])
            leaf.add_child("var", line[2])
            leaf = leaf.ascend()
    except IndexError:
        pass

    AST.print_children()


print()
AST.print_children()

print("##########")

itrp = ASTtools.ASTinterpreter(AST)

itrp.print_ast(AST)