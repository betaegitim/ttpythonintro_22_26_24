# dosya = open("datasrc.csv","r+")
# with open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/datasrc.csv","r+") as dosya,\
#     open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data1.csv","a") as d1,\
#         open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data2.csv","a") as d2: 
#     liste = dosya.readlines()
#     for i in range(len(liste)):
#         print(liste[i])
#         a,b,c,d = liste[i].split(",")
#         print(",".join((a,c,d)),file=d1,end="")
#         print(",".join((a,b,c)),file=d2)
        
d1 = open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data1.csv","r+")
d2 = open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data2.csv","r+")