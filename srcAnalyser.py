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


for line in srcLines:
    print("newline: ", end = "")
    print(line)
    if line[0] == "type":
        leaf = leaf.add_child("def", "class")
        leaf.add_child("func", line[1])
        leaf.add_child("block")

print()
AST.print_children()

print("##########")

itrp = ASTtools.ASTinterpreter(AST)

itrp.print_ast(AST)