#txt = "we are so-called "Vikings" from the north" -> error
#print(txt)

txt = "we are so-called \"Vikings\" from the north"
print(txt)  #we are so-called "Vikings" from the north
print("\n")

txt = 'it\'s alright'   #'it's alright' -> error
print(txt)  #it's alright
print("\n")

txt = "this will insert one \\ (backslash)"
print(txt)  #this will insert one \ (backslash)
print("\n")

txt = "hello\nworld"
print(txt) 
"""hello
   world"""
print("\n")

txt = "hello\tworld"
print(txt)  #hello   world
print("\n")

txt = "hello \bworld"
print(txt)  #helloworld erases one character (backspace)
print("\n")

txt = "\110\145\154\154\157"    #backslash followed by three integers will result in a octal value:
print(txt)                      #Hello
print("\n")

txt = "\x48\x65\x6c\x6c\x6f"    #backslash followed by an 'x' and a hex number represents a hex value:
print(txt)                      #Hello

