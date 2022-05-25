f = open("main.fig", "r")
fig = str(f.read())

while 1:
  if "out-'" in fig:
    f1 = fig.split("out-'")
    f2 = f1[1].split("'")
    fig = fig.replace("out-'"+f2[0]+"';", '')
    print(f2[0])
  elif 'out-"' in fig:
    f1 = fig.split('out-"')
    f2 = f1[1].split('"')
    fig =  fig.replace('out-"'+f2[0]+'";', '')
    print(f2[0])
  elif "in-'" in fig:
    f1 = fig.split("in-'")
    f2 = f1[1].split("'")
    fig = fig.replace("in-'"+f2[0]+"';", '')
    inp = input(f2[0])
    print(inp)
  elif "stop;" in fig:
    print("\nExit Status 1")
    break
  else:
    print("\nExit Status 0")
    break
