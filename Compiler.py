class AST:
    printDepth = 0

    def __str__(self):
        strn = str(self.key) + ": " + str(self.name)
        return strn

    def __getitem__(self, key):
        return self.leaves[key]

    def __iter__(self):
        return iter(self.leaves)

    def __init__(self, key, name=None, branch = None):
        self.key = key
        self.name = name
        self.leaves = list()
        self.branch = branch

    def print_children(self):
        for leaf in self.leaves:
            for i in range(self.printDepth):
                print("  ", end="")
            print("--", leaf)

            AST.printDepth += 1
            leaf.print_children()
            AST.printDepth -= 1

    def ascend(self, lv = 1):
        if lv != 1:
            return self.branch.ascend(lv - 1)
        else:
            return self.branch



    def add_child(self, key, name=None):
        leaf = AST(key, name, self)
        self.leaves.append(leaf)
        return self.leaves[-1]

    def give_branch(self):
        return self.branch


class ASTinterpreter:

    def __init__(self, AST):
        self.tab = 0
        self.AST = AST

    def print_ast(self, branch):
        stk = self.print_stack(branch)
        for leaf in stk:
            if leaf == branch:
                self.do_print(leaf)
            else:
                self.print_ast(leaf)

    def print_stack(self, branch):
        stk = list()
        if branch.key == "root":
            for leaf in branch:
                stk.append(leaf)
            return stk

        if branch.key == "def":
            if branch.name == "func":
                stk.append(AST("synt", "def "))
                stk.append(branch[0])
                stk.append(AST("synt", ": \n"))
                stk.append(branch[1])
                return stk
            if branch.name == "class":
                stk.append(AST("synt", "class "))
                stk.append(branch[0])
                stk.append(AST("synt", ": \n"))
                stk.append(branch[1])
                return stk

        if branch.key == "op":
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

        if branch.key == "ctrl":
            if branch.name in ["for", "if", "while"]:
                stk.append(branch)
                stk.append(branch[0])
                stk.append(AST("synt", ": \n"))
                stk.append(branch[1])
                return stk
            if branch.name == "return":
                stk.append(branch)
                stk.append(AST("synt", "("))
                for leaf in branch:
                    stk.append(leaf)
                    stk.append(AST("synt", ","))
                stk.pop()
                stk.append(AST("synt", ")"))
                return stk
            if branch.name in ["break", "continue"]:
                stk.append(branch)
                return stk

        if branch.key == "func":
            pop = False
            stk.append(branch)
            stk.append(AST("synt", "("))
            for leaf in branch:
                stk.append(leaf)
                stk.append(AST("synt", ","))
                pop = True
            if pop:
                stk.pop()
                pop = False
            stk.append(AST("synt", ")"))
            return stk

        if branch.key == "block":
            stk.append(AST("tab", "lvp"))
            for leaf in branch:
                stk.append(AST("tab", "do"))
                stk.append(leaf)
                stk.append(AST("synt", "\n"))
            stk.append(AST("tab", "lvm"))
            return stk

        stk.append(branch)
        return stk

    def do_print(self, branch):
        if branch.key == "block":
            return
        if branch.key == "tab":
            if branch.name == "lvp":
                self.tab += 1
            if branch.name == "lvm":
                self.tab -= 1
            if branch.name == "do":
                for i in range(self.tab):
                    print("    ", end="")
            return

        if branch.key == "synt":
            print(self.get_print(branch), end="")
            return
        print(self.get_print(branch), end=" ")

    def get_print(self, branch):
        if branch.key == "op":
            if branch.name == "set":
                return "="
            if branch.name == "is":
                return "=="
            if branch.name == "in":
                return "in"
        if branch.key == "var":
            return branch.name
        if branch.key == "basic":
            return branch.name
        if branch.key == "ctrl":
            if branch.name in ["for", "if", "while", "return", "break", "continue"]:
                return branch.name
        if branch.key == "func":
            return branch.name
        if branch.key == "synt":
            return branch.name

        return branch.key, branch.name


root = AST("root")

leaf = root.add_child("op", "set")
leaf.add_child("var", "i")
leaf.add_child("basic", "0")
leaf = leaf.ascend()
leaf = leaf.add_child("ctrl", "for")
leaf = leaf.add_child("op", "in")
leaf.add_child("var", "i")
leaf = leaf.add_child("func", "range")
leaf.add_child("basic", "7")
leaf = leaf.ascend(2)
leaf = leaf.add_child("block")
leaf = leaf.add_child("func", "print")
leaf.add_child("var", "i")
leaf = leaf.ascend()
leaf = leaf.add_child("ctrl", "return")
leaf.add_child("var", "i")
leaf.add_child("var", "j")
leaf = leaf.ascend(3)
leaf = leaf.add_child("ctrl", "while")
leaf = leaf.add_child("op", "is")
leaf.add_child("var", "i")
leaf.add_child("basic", "7")
leaf = leaf.ascend()
leaf = leaf.add_child("block")
leaf = leaf.add_child("func", "myfunc")
leaf.add_child("var", "i")
leaf.add_child("var", "t")
leaf.add_child("var", "j")
leaf = leaf.ascend()
leaf.add_child("ctrl", "break")
leaf = leaf.ascend(2)
leaf = leaf.add_child("def", "class")
leaf.add_child("func", "thisfunc")
leaf = leaf.add_child("block")
leaf.add_child("var", "i")
leaf.add_child("var", "t")


print("------------")
root.print_children()

print("##########")

itrp = ASTinterpreter(root)

itrp.print_ast(root)
