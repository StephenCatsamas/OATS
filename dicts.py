class func:

    def __init__(self, name , namespace = None):
        self.args = list()
        self.name = name
        self.type = type
        self.namespace = namespace

    def add_arg(self, name, type):
        self.args.append((name,type))

    def give_fullname(self, path = ""):
        if path == "":
            path = self.name
        if self.namespace != None:
            path = self.namespace.give_fullname(path) + "." + path
        else:
            return self.name
        return(path)

func1 = func("func1")
func2 = func("func2", func1)

print(func2.give_fullname())


