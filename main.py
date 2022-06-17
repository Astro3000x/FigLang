f = open("main.fig", "r")
fig = str(f.read())
variables = {}
discord = False
web = False
tkinter = False
while 1:
 if "import-" in fig:
   f1 = fig.replace("import-", "")
   f2 = f1.split(";")
   f4 = f2[0]
   if f4 == "discord":
     discord = True
     import discord
   elif f4 == "web":
     web = True
     from flask import Flask
   elif f4 == "ui":
     from tkinter import *
     tkinter = True
   else:
     print(f"Error: Library {f4} not found")
   fig = fig.replace(f"import-{f4};", "")
 if "var-" in fig:
   f1 = fig.replace("var-", "")
   f2 = f1.split(" = ")
   varname = f2[0]
   f3 = f2[1].split(";")
   f4 = f3[0]
   varvalue = f4
   variables[varname] = varvalue
   
   fig = fig.replace(f"var-{varname} = {f4};", "")
 
    
 if "for-" in fig:
   
   f1 = fig.replace("for-", "")
   f2 = f1.split("(")
   f3 = f2[1].split(')')
   f4 = f3[0].split(" ")
   v1 = f1.split("[")
   v2 = v1[1].split("]")
   for i in range(0, int(f3[0])):
     
      if "out-'" in v2[0] or 'out-"' in v2[0]:
        f1 = v2[0].replace("out-", "")
        f2 = f1.replace("'", "")
        f3 = f2.replace('"', '')
        f4 = f3.split(";")
        print(f4[0])
        fig = fig.replace("out-"+f1, "")
      if "var-" in fig:
        f1 = fig.replace("var-", "")
        f2 = f1.split(" = ")
        varname = f2[0]
        f3 = f2[1].split(";")
        f4 = f3[0]
        varvalue = f4
        variables[varname] = varvalue
        fig = fig.replace(f"var-{varname} = {f4};", "")
   
   
 if "when-" in fig:
   f1 = fig.replace("when-", "")
   f2 = f1.split("(")
   f3 = f2[1].split(')')
   f4 = f3[0].split(" ")
   v1 = f1.split("[")
   v2 = v1[1].split("]")
   
   if f4[1] == '==':
     if f4[0] == f4[2]:
       if "out-'" in v2[0] or 'out-"' in v2[0]:
        f1 = v2[0].replace("out-", "")
        f2 = f1.replace("'", "")
        f3 = f2.replace('"', '')
        f4 = f3.split(";")
        print(f4[0])
        fig = fig.replace("out-"+f1, "")
       if "var-" in fig:
        f1 = fig.replace("var-", "")
        f2 = f1.split(" = ")
        varname = f2[0]
        f3 = f2[1].split(";")
        f4 = f3[0]
        varvalue = f4
        variables[varname] = varvalue
        fig = fig.replace(f"var-{varname} = {f4};", "")
       elif "out-" in v2[0]:
        f1 = v2[0].replace("out-", "")
        f4 = f1.split(";")
        vv = f4[0]
        vvv = vv.replace("\n", "")
        v4 = vvv.replace("'", "")
        v5 = v4.replace('"', '')
        if v5 in variables:
         vartoprint = variables[v5]
         v7 = vartoprint.replace("'", "")
         v8 = v7.replace('"', '')
         print(v8)
        else:
         print(f"Error: Variable {v5} Not Found")
        fig = fig.replace("out-"+f1, "")
   elif f4[1] == '!=':
     if f4[0] != f4[2]:
       if "out-'" in v2[0] or 'out-"' in v2[0]:
        f1 = v2[0].replace("out-", "")
        f2 = f1.replace("'", "")
        f3 = f2.replace('"', '')
        f4 = f3.split(";")
        print(f4[0])
        fig = fig.replace("out-"+f1, "")
       elif "out-" in v2[0]:
        f1 = v2[0].replace("out-", "")
        f4 = f1.split(";")
        vv = f4[0]
        vvv = vv.replace("\n", "")
        v4 = vvv.replace("'", "")
        v5 = v4.replace('"', '')
        if v5 in variables:
         vartoprint = variables[v5]
         v7 = vartoprint.replace("'", "")
         v8 = v7.replace('"', '')
         print(v8)
        else:
         print(f"Error: Variable {v5} Not Found")
        fig = fig.replace("out-"+f1, "")
       if "var-" in fig:
         f1 = fig.replace("var-", "")
         f2 = f1.split(" = ")
         varname = f2[0]
         f3 = f2[1].split(";")
         f4 = f3[0]
         varvalue = f4
         variables[varname] = varvalue
         fig = fig.replace(f"var-{varname} = {f4};", "")
 if "out-'" in fig or 'out-"' in fig:
   f1 = fig.replace("out-", "")
   f2 = f1.replace("'", "")
   f3 = f2.replace('"', '')
   f4 = f3.split(";")
   print(f4[0])
   fig = fig.replace("out-"+f1, "")
 elif "out-" in fig:
   f1 = fig.replace("out-", "")
   f4 = f1.split(";")
   vv = f4[0]
   vvv = vv.replace("\n", "")
   v4 = vvv.replace("'", "")
   v5 = v4.replace('"', '')
   if v5 in variables:
     vartoprint = variables[v5]
     v7 = vartoprint.replace("'", "")
     v8 = v7.replace('"', '')
     print(v8)
   else:
     print(f"Error: Variable {v5} Not Found")
   fig = fig.replace("outvar-"+f1, "")
 if "outvar-" in fig:
   f1 = fig.replace("outvar-", "")
   f4 = f1.split(";")
   vv = f4[0]
   vvv = vv.replace("\n", "")
   v4 = vvv.replace("'", "")
   v5 = v4.replace('"', '')
   vartoprint = variables[v5]
   v7 = vartoprint.replace("'", "")
   v8 = v7.replace('"', '')
   print(v8)
   fig = fig.replace("outvar-"+f1, "")
  
 if "in-'" in fig:
    f1 = fig.split("in-'")
    f2 = f1[1].split("'")
    fig = fig.replace("in-'"+f2[0]+"';", '')
    inp = input(f2[0])
    print(inp)
 if "math-" in fig:
   f1 = fig.split("math-")
   
   f2 = f1[1].split(";")
   f3 = f2[0]
   
   if "+" in f3:
     f4 = f3.split("+")
     num1 = float(f4[0])
     num2 = float(f4[1])
     print(num1+num2)
     fig = fig.replace(f"math-{f1[1]}", "")
   elif "-" in f3:
     f4 = f3.split("-")
     num1 = float(f4[0])
     num2 = float(f4[1])
     print(num1-num2)
     fig = fig.replace(f"math-{f1[1]}", "")
   elif "*" in f3:
     f4 = f3.split("*")
     num1 = float(f4[0])
     num2 = float(f4[1])
     print(num1*num2)
     fig = fig.replace(f"math-{f1[1]}", "")
   elif "/" in f3:
     f4 = f3.split("/")
     num1 = float(f4[0])
     num2 = float(f4[1])
     print(num1/num2)
     fig = fig.replace(f"math-{f1[1]}", "")
 if "web-start" in fig:
   f1 = fig.split("web-start-")
   f2 = f1[1].split(";")
   f2[0] = f2[0].replace("'", "")
   f2[0] = f2[0].replace('"', '')
   if web == True:
     from flask import Flask
     app = Flask('app')

     @app.route('/')
     def hello_world():
       return f"{f2[0]}"

     app.run(host='0.0.0.0', port=8080)
   else:
     print("Error: Library Web Not Imported")
   fig = fig.replace(f"web-start-{f2[0]};", "")
 if "ui-start" in fig:
   f1 = fig.split("ui-start-")
   f2 = f1[1].split(";")
   f2[0] = f2[0].replace("'", "")
   f2[0] = f2[0].replace('"', '')
   if tkinter == True:
     tk = Tk()
     tk.geometry("300x300")
     canvas = Canvas(tk, width=300, height=300)
     canvas.pack()
     canvas.create_text(150, 10, text=f'{f2[0]}')
     tk.title("UI")
   else:
     print("Error: Library Ui Not Imported")
   fig = fig.replace(f"web-start-{f2[0]};", "")
 
 if "stop;" in fig:
    print("Exit Status 1")
    
    break
 else:
    print("Exit Status 0")
    break