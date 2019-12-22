
fp = "Example.oat"
op = "comp.py"

with open(fp, 'r') as srcf:
    src = srcf.read()
    print(src)

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
idx = 0
def printAST(AST):
    for child in AST:
        text = getPrint(child,idx)
        if text != None:
            outlst.insert(text,idx)
            idx += 1
        printAST(child)

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
        
    
        
    return None
    
    
root = nodeAST("root")

root.addChild("op", "set")
root[0].addChild("var","i")
root[0].addChild("basic","0")
root.addChild("ctrl", "for")
root[1].addChild("op", "in")
root[1][0].addChild("var","i")
root[1][0].addChild("func", "range")
root[1][0][1].addChild("basic", "7")
root[1].addChild("func", "print")
root[1][1].addChild("var","i")

root.printChildren()
print("##########")
printAST(root)
print(outlst)
    