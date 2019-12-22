fp = "Example.oat"
op = "comp.py"


# with open(fp, 'r') as srcf:
#     src = srcf.read()
#     print(src)

class AST:

    def __getitem__(self, key):
        return self.leaves[key]

    def __iter__(self):
        return iter(self.leaves)

    def __init__(self, type, name=None):
        self.type = type
        self.name = name
        self.leaves = list()
        self.printDepth = 0

    def printChildren(self):
        for leaf in self.leaves:
            for i in range(self.printDepth):
                print("  ", end="")
            print("--", leaf.type, leaf.name)

            self.printDepth += 1
            leaf.printChildren()
            self.printDepth -= 1

    def addChild(self, type, name=None):
        leaf = AST(type, name)
        self.leaves.append(leaf)


class ASTinterpreter:

    def __init__(self, AST):
        self.tab = 0
        self.AST = AST

    def printAST(self, branch):
        stk = self.printStack(branch)
        for leaf in stk:
            if leaf == branch:
                self.doPrint(leaf)
            else:
                self.printAST(leaf)

    def printStack(self, branch):
        stk = list()
        if branch.type == "root":
            for node in branch:
                stk.append(node)
            return stk

        if branch.type == "op":
            if branch.name == "set":
                stk.append(branch[0])
                stk.append(branch)
                stk.append(branch[1])
                stk.append(AST("synt", "\n"))
                return stk

            if branch.name in ["in", "is"]:
                stk.append(branch[0])
                stk.append(branch)
                stk.append(branch[1])
                return stk

        if branch.type == "ctrl":
            if branch.name in ["for","if"]:
                stk.append(branch)
                stk.append(branch[0])
                stk.append(AST("synt", ": \n"))
                stk.append(branch[1])
                return stk

        if branch.type == "func":
            stk.append(branch)
            stk.append(AST("synt", "("))
            for child in branch:
                stk.append(child)
                stk.append(AST("synt", ","))
            stk.pop()
            stk.append(AST("synt", ")"))
            return stk

        if branch.type == "block":
            stk.append(AST("tab", "lvp"))
            for child in branch:
                stk.append(AST("tab", "do"))
                stk.append(child)
                stk.append(AST("synt", "\n"))
            stk.append(AST("tab", "lvm"))
            return stk

        stk.append(branch)
        return stk

    def doPrint(self, branch):
        self.tab
        if branch.type == "block":
            return
        if branch.type == "tab":
            if branch.name == "lvp":
                self.tab += 1
            if branch.name == "lvm":
                self.tab -= 1
            if branch.name == "do":
                for i in range(self.tab):
                    print("    ", end="")
            return

        if branch.type == "synt":
            print(self.getPrint(branch), end="")
            return
        print(self.getPrint(branch), end=" ")

    def getPrint(self, branch):
        if branch.type == "op":
            if branch.name == "set":
                return "="
            if branch.name == "is":
                return "=="
            if branch.name == "in":
                return "in"
        if branch.type == "var":
            return branch.name
        if branch.type == "basic":
            return branch.name
        if branch.type == "ctrl":
            if branch.name == "for":
                return branch.name
            if branch.name == "if":
                return branch.name
        if branch.type == "func":
            return branch.name
        if branch.type == "synt":
            return branch.name


root = AST("root")

root.addChild("op", "set")
root[0].addChild("var", "i")
root[0].addChild("basic", "0")
root.addChild("ctrl", "for")
root[1].addChild("op", "in")
root[1][0].addChild("var", "i")
root[1][0].addChild("func", "range")
root[1][0][1].addChild("basic", "7")
root[1].addChild("block")
root[1][1].addChild("func", "print")
root[1][1][0].addChild("var", "i")
root[1][1].addChild("func", "print")
root[1][1][1].addChild("var", "i")
root.addChild("ctrl", "if")
root[2].addChild("op", "is")
root[2][0].addChild("var", "i")
root[2][0].addChild("basic", "7")
root[2].addChild("block")
root[2][1].addChild("func", "print")
root[2][1][0].addChild("var", "i")

root.printChildren()
print("##########")

itrp = ASTinterpreter(root)

itrp.printAST(root)
