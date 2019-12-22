
fp = "Example.oat"
op = "comp.py"

# with open(fp, 'r') as srcf:
    # src = srcf.read()
    # print(src)

class nodeAST:
    depth = 0
    
    def __getitem__(self, key):
        return self.children[key]
    
    def __iter__(self):
        return iter(self.children)
    
    def __init__(self,type,name = None):
        self.type = type
        self.name = name
        self.children = list()
        
    def printChildren(self):
            for child in self.children:
                for i in range(nodeAST.depth):
                    print("  ", end ="")
                print("--", child.type, child.name)
                
                nodeAST.depth += 1
                child.printChildren()
                nodeAST.depth -= 1
    
    def addChild(self,type,name = None):
        child = nodeAST(type,name)
        self.children.append(child)

def printAST(AST):
        stk = printOdr(AST)
        for node in stk:
            if node == AST:
                doPrint(node)
            else:
                printAST(node)

def printOdr(node):
    stk = list()
    if node.type == "root":
        for child in node:
            stk.append(child)
        return stk
        
    if node.type == "op":
        if node.name == "set":
            stk.append(node[0])
            stk.append(node)
            stk.append(node[1])
            stk.append(nodeAST("synt", "\n"))
            return stk

        if node.name == "in":
            stk.append(node[0])
            stk.append(node)
            stk.append(node[1])
            return stk
        
    if node.type == "ctrl":
        if node.name == "for":
            stk.append(node)
            stk.append(node[0])
            stk.append(nodeAST("synt", ": \n"))
            stk.append(node[1])
            return stk   
            
    if node.type == "func":
        stk.append(node)
        stk.append(nodeAST("synt", "("))
        for child in node:
            stk.append(child)
            stk.append(nodeAST("synt", ","))
        stk.pop()
        stk.append(nodeAST("synt", ")"))
        return stk  
    
    if node.type == "block":
        stk.append(nodeAST("tab", "lvp"))
        for child in node:
            stk.append(nodeAST("tab", "do"))
            stk.append(child)
            stk.append(nodeAST("synt", "\n"))
        stk.append(nodeAST("tab", "lvm"))    
        return stk
    
    stk.append(node)
    return stk
    
tab = 0
def doPrint(node):
    global tab
    if node.type == "block":
        return
    if node.type == "tab":
        if node.name == "lvp":
            tab += 1
        if node.name == "lvm":
            tab -= 1
        if node.name == "do":
            for i in range(tab):
                print("    ", end = "")
        return
        
    if node.type == "synt":
        print(getPrint(node), end = "")
        return
    print(getPrint(node), end = " ")

def getPrint(node):
    if node.type == "op":
        if node.name == "set":
            return "="
        if node.name == "in":
            return "in"
    if node.type == "var":
        return node.name
    if node.type == "basic":
        return node.name
    if node.type == "ctrl":
        if node.name == "for":
            return node.name
    if node.type == "func":
        return node.name
    if node.type == "synt":
        return node.name

    
    
root = nodeAST("root")

root.addChild("op", "set")
root[0].addChild("var","i")
root[0].addChild("basic","0")
root.addChild("ctrl", "for")
root[1].addChild("op", "in")
root[1][0].addChild("var","i")
root[1][0].addChild("func", "range")
root[1][0][1].addChild("basic", "7")
root[1].addChild("block")
root[1][1].addChild("func", "print")
root[1][1][0].addChild("var","i")
root[1][1].addChild("func", "print")
root[1][1][1].addChild("var","i")

root.printChildren()
print("##########")
printAST(root)
    