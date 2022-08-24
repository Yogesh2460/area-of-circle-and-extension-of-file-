filename=input("Input the Filename: ")
f_extns=filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
#cap i made this so that it prints extensions of all types file
#if I want to make the code print 'python' for py then
if f_extns[-1] == 'py':
  print("The extension of the file is : python ")
