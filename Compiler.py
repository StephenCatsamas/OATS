
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
    
    def __init__(self,name):
        self.name = name
        self.children = list()
        
    def printChildren(self):
            for child in self.children:
                for i in range(nodeAST.depth):
                    print("  ", end ="")
                print("--", child.name)
                nodeAST.depth += 1
                child.printChildren()
                nodeAST.depth -= 1
    
    def addChild(self,name):
        child = nodeAST(name)
        self.children.append(child)
        

root = nodeAST("root")

root.addChild("fnoo")
root.addChild("fboo")
root[0].addChild("xnoo")
root[0][0].addChild("znoo")

root.printChildren()


    