f = open("main.fig", "r")
fig = str(f.read())
variables = {}
while 1:
  
 if "var-" in fig:
   f1 = fig.replace("var-", "")
   f2 = f1.split(" = ")
   varname = f2[0]
   f3 = f2[1].split(";")
   f4 = f3[0]
   varvalue = f4
   variables[varname] = varvalue
   
   fig = fig.replace(f"var-{varname} = {f4};", "")
 
 if "/-" in fig or '/-' in fig:
    f1 = fig.replace("/-", "")
    
    
    
    
    fig = fig.replace("/-"+f1, "")
 if "out-'" in fig or 'out-"' in fig:
   f1 = fig.replace("out-", "")
   f2 = f1.replace("'", "")
   f3 = f2.replace('"', '')
   f4 = f3.split(";")
   print(f4[0])
   fig = fig.replace("out-"+f1, "")
 if "outvar-" in fig:
   f1 = fig.replace("outvar-", "")
   f4 = f1.split(";")
   vv = f4[0]
   vvv = vv.replace("\n", "")
   v4 = vvv.replace("'", "")
   v5 = v4.replace('"', '')
   vartoprint = variables[v5]
   print(vartoprint)
   fig = fig.replace("outvar-"+f1, "")
  
 if "in-'" in fig:
    f1 = fig.split("in-'")
    f2 = f1[1].split("'")
    fig = fig.replace("in-'"+f2[0]+"';", '')
    inp = input(f2[0])
    print(inp)
 if "stop;" in fig:
    print("Exit Status 1")
    
    break
 else:
    print("Exit Status 0")
    break