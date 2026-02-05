# In file handling we give two arguments 1st file name and 2nd mode:
# 'r' for reading, 'w' writing, and 'a' for append
# 'r' mode is a default if we can't write it it by default execute in read mode


#      READING THE FILE
# f = open('_14FIleIO/myfile.txt', 'r')
# # print(f) we cannot print the content of file like this
# text = f.read()
# print(text)
# f.close()


# if we want to write the the file so we can simply write 'w'
# but after that we can't use .read() and .close() bcz it is for
# reading not for writing

# if we opens the file in write mode it can delete all the data from it
# so avoiding the this situation we use append 'a'
# and 'w' mode is useful when there is an empty file

# f = open('_14FIleIO/myfile.txt', 'rb')
# it opens the file in binary form 'rb'(read binary) it is for when we opens 
# pdf, jpeg, etc. and 't' is for text there is no need to write 't' bcz it is default


#     WRITING THE FILE
# f = open("_14FileIO/myfile2.txt", 'x') #for creating the file
# f.write("Hello! World. ")
# f.close()

# if file already exists then we use f = open("_14FileIO/myfile2.txt", 'w')

#        APPEND THE FILE
# f = open("_14FileIO/myfile2.txt", 'a')
# f.write("Hello! World. ")
# f.close()

# now every time we run this command it append the hello! world at the end

# if we want to not use .close() so we are doing  like :
# f = open("_14FileIO/myfile2.txt", 'a') or
with open("_14FileIO/myfile2.txt", 'a') as f:
    f.write("i am using with()")


