# def default_arg(id,name="spectrum"):
#     print("ID",id)
#     print("NAME",name)
#     return
# default_arg(10)

# required arguments

# def required_arg(str):
#     print("input strings",str)
# required_arg("spectrum")

# keywords arguments

# def keyword_arg(str,id):
#     print("id",id)
#     print("name",str)
# keyword_arg(id=13,str="spectrum")

# variable length argumets

# def myfun(*argv):
#     for arg in argv:
#             print(arg)
# myfun('hello','welcome','to','geeksforgeeks')


# args

# def myfun(*argv):
#     for arg in argv:
#         print(arg)
# myfun('hello','welcome','to','geeksforgeeks')

# kwargs

# def myfun(**kwargs):
#     d={}
#     for key,value in kwargs.items():
#         d[key]=value
#     print(d)
# myfun(first="geeks",mid="for",last="geeks")