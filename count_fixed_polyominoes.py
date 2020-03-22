import sys

def adjacencyList(G, u):
    ajdacent = []
    akmes = G[1] #oi akmes einai to 2o stoixeio toy grafoy G
    for akmh in akmes: #gia ka8e akmh
        if akmh[0] == u[0] and akmh[1] == u[1]: #o prwtos kombos ths akmhs einai to u
            ajdacent.append((akmh[2],akmh[3]))
    return ajdacent

def neighbors(G,pu):
    neighbourhood = []
    akmes = G[1]
    for kombos in pu:
        for akmh in akmes:
            if akmh[0] == kombos[0] and akmh[1] == kombos[1]:
                neighbourhood.append((akmh[2],akmh[3])) 
    return neighbourhood

def countFixedPolyominoes(G, untried, n, p, c):
    while not len(untried) == 0:
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            c[0] = c[0] + 1
        else:
            new_neighbors = set()
            #print(u,'@', adjacencyList(G,u))
            for v in adjacencyList(G, u):
                p.remove(u) #p\u
                pu = list(p) #p\u
                p.append(u) #epeidh to kaname remove
                if v not in untried and v not in p and v not in neighbors(G,pu):
                    new_neighbors.add(v)
            new_untried = untried.union(new_neighbors)
            countFixedPolyominoes(G, new_untried, n, p, c)
        p.remove(u)
    return c[0]

if len(sys.argv) == 3: #2 orismata
    pr = True
    n = int(sys.argv[2])
elif len(sys.argv) == 2: #1 orisma
    pr = False
    n = int(sys.argv[1])
else:
    print("invalid arguments") #la8os plh8os orismatwn
    sys.exit()

komboi=[] #lista me toys komboys
for x in range(-n+2,n):
    for y in range(n):
        if (y>0)or(y==0)and x>=0: #einai panw apo th grammh
            if abs(x) + abs(y) < n: #to a8roisma toys den 3eperna to n
                komboi.append([x,y])

akmes=[]
for x in range(-n+2,n):
    for y in range(n):
        if (y>0)or(y==0)and x>=0:
            if abs(x) + abs(y) < n:
                #oi akmes diaferoyn kata 1 kai einai valid komboi
                xtonos = x + 1
                ytonos = y
                if (ytonos>0)or(ytonos==0)and xtonos>=0:
                    if abs(xtonos) + abs(ytonos) < n:
                        akmes.append([x,y,xtonos,ytonos])
                xtonos = x - 1
                ytonos = y
                if (ytonos>0)or(ytonos==0)and xtonos>=0:
                    if abs(xtonos) + abs(ytonos) < n:
                        akmes.append([x,y,xtonos,ytonos])
                xtonos = x
                ytonos = y + 1
                if (ytonos>0)or(ytonos==0)and xtonos>=0:
                    if abs(xtonos) + abs(ytonos) < n:
                        akmes.append([x,y,xtonos,ytonos])
                xtonos = x
                ytonos = y - 1
                if (ytonos>0)or(ytonos==0)and xtonos>=0:
                    if abs(xtonos) + abs(ytonos) < n:
                        akmes.append([x,y,xtonos,ytonos])

G = [komboi, akmes]
untried = {(0,0)}
p = []
c = [0]

r = countFixedPolyominoes(G, untried, n, p, c)

if pr == True:
    print('{', end= "")
    for akmh in akmes:
        line = '(' + str(akmh[0]) + ', ' + str(akmh[1]) + '): [' 
        print(line, end = "")
        for kombos in adjacencyList(G, (akmh[0], akmh[1])):
            print(kombos, ', ', end = "", sep='')
        print(']')
    print('}')
print(r)