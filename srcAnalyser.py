import Compiler as ASTtools


fp = "Example.oat"
op = "comp.py"

AST = ASTtools.AST("root")

with open(fp, 'r') as srcf:
    src = srcf.read()
    print(src)

#srcAST = AST("root")

keywords = ["type"]

srcLines = list()

ilst = 0
for i,char in enumerate(src):
    if char == "\n":
        flushline = src[ilst:i]
        srcLines.append(flushline.strip())
        ilst = i+1

for line in srcLines:
        print("newline: ", end = "")
        print(line)

        if line[0:4] == "type":



AST.print_children()