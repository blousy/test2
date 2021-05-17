class TimeTravelReomote():
    


    def __init__(self):

        self.remote = ["Past","Present","Future"]
        self.index = -1

    def __iter__(self):
        return self


    def __next__(self):
         
         self.index += 1

         if self.index == len(self.remote):
             raise StopIteration
         return self.remote[self.index]
        
    
r = TimeTravelReomote()

itr = iter(r)

print(next(itr))
print(next(itr))
