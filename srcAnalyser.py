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

leaf = AST

types = ["INT", "STRING", "VOID", "BASIC"]
funcs = ["IS", "SET"]

for line in srcLines:
    print("newline: ", end="")
    print(line)

    try:
        if line[0] == "TYPE":
            leaf = leaf.add_child("def", "type")
            leaf.add_child("func", line[1])
            leaf = leaf.add_child("block")
            continue

        if line[1] == "PROPS":
            if line[0] == "START":
                leaf = leaf.add_child("def", "func")
                leaf.add_child("func", "__init__")
                leaf = leaf.add_child("block")
                continue
            if line[0] == "END":
                leaf = leaf.ascend(2)
                continue

        if leaf.ascend()[0].name == "__init__":
            if line[0] in types:
                leaf = leaf.add_child("op", "set")
                leaf.add_child("var", line[1])
                leaf.add_child("func", line[0])
                leaf = leaf.ascend()
                continue


        if line[1] == "FUNCS":
            if line[0] == "START":
                leaf = leaf.add_child("def", "typefunc")
                continue
            if line[0] == "END":
                leaf = leaf.ascend()
                continue


        if leaf.key == "func":
            if line[0] in types:
                if line[1] in funcs:
                    leaf = leaf.add_child("func", line[1])
                else:
                    leaf.add_child("var", line[1])
                continue

        if leaf.name == "typefunc":
            if line[0] in types:
                leaf = leaf.add_child("def", "func")
                leaf = leaf.add_child("func", line[1])
                continue

        if line[1] == "ARGS":
            if line[0] == "START":
                pass
            if line[0] == "END":
                leaf = leaf.ascend()
                continue

        if line[1] == "METHOD":
            if line[0] == "START":
                leaf = leaf.add_child("block")
                continue
            if line[0] == "END":
                leaf = leaf.ascend(2)
                continue

        if line[0] in types:
            if line[1] in funcs:
                leaf = leaf.add_child("func", line[1])
                continue

    except IndexError:
        pass
    #AST.print_children()


print()
AST.print_children()

print("##########")

itrp = ASTtools.ASTinterpreter(AST)

itrp.print_ast(AST)