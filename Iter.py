class topten:
    def __init__(self):
        self.num =1
    def __iter__(self):
        return self
    

val = topten()

print(next((val)))
for  i in (val):
    print(i)


