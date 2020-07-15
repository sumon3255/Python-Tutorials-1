#Ram is a volatile
#volatile is when you shut down Your Computer ALl Data will be vanished
#Hardisk is non volatile
#non volatile is  data will save in Your computer memory.you put all these things it will be save forever

#File Io Basics
"""

  "r"- Open file for reading-default
  "w"- Open file for Writing
  "x"- Creats file if not exists
  "a"- Add more content to file
  "t"- text mode-default
  "b"- binary mode
  "+"- read and write
"""

#   question
def function1(a,b):
      """This is doc string"""
      sum = a+ b
      return sum


V=function1(2,4)
print(V)
print(function1.__doc__)