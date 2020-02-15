class rev:
    def reverse(self,string):
        str=""
        for i in string:
            str=i+str
        return str
string = input()
obj1=rev()
print(obj1.reverse(string))