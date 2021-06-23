class Human:
    def __init__(self, n, o):
        self.name = n
        self.occup=o

    def do_work(self):
        if self.occup=="tennis":
            print(self.name,"plays tennis")
        elif self.occup=="actor":
            print(self.name,"shoot a film")

    def speaks(self):
        print(self.name,"says how are you?")   

tom =Human("tom cruise","actor")
tom.do_work()
tom.speaks()                 