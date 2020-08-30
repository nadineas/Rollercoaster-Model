from visual import *
from random import *


scene = display(title= 'RollerCoaster', x= 0, y=0, width=2000, height=2000, center=(5,5,0),
                background=(0,1,1), color=color.gray)

ground = box(pos=(250,30,250), length=500, height=60, width=420,color=color.white, material=materials.wood)
marble = sphere(pos=(310,270,260),radius=8,material=materials.marble,color=color.blue)



sc = [];
p1 = vector(190,60,250)
p2 = vector(300,260,250)
p3 = vector(300,260,150)
p4 = vector(190,220,150)
p5 = vector(190,220,50)
p6 = vector(300,150,50)
p7 = vector(300,150,350)
p8 = vector(270,80,350)
p9 = vector(220,80,350)
p10 = vector(190,80,350)


rad1 = 50
angle = 0
angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
distx = 0
disty = 0
xx2=0
xx3=0
xx4=0
xx5=0
for x in range(0, 3300):
    if x<1000:
        sc.append( p1+x*(p2-p1)/1000 )
    elif x<1300 :
        angle = angle + (math.pi/300)
        xpoint = 300  + math.sin(angle)*50
        ypoint = 260
        zpoint = 200 + math.cos(angle)*50
        sc.append( vector(xpoint,ypoint,zpoint) )
    elif x<1600:
        sc.append(p3 + (xx2*(p4-p3))/300)
        xx2+=1
    elif x<1800:
        angle1 = angle1 + (math.pi/300)
        x1 = 190 + math.sin(angle1)*(-50)
        y1 = 220
        z1 = 100 + math.cos(angle1)*50
        sc.append(vector(x1,y1,z1))
    elif x<2000:
        sc.append(p5+(xx3*(p6-p5))/200)
        xx3+=1
    elif x<2300:
        angle2 = angle2 + (math.pi/300)
        x2 = 300 + math.sin(angle2)*150
        y2 = 150
        z2 = 200 + math.cos(angle2)*(-150)
        sc.append(vector(x2,y2,z2))
    elif x<2400:
        sc.append(vector(p7 - (xx5*(p7-p8))/100))
        xx5+=1
    elif x<2700:
        sc.append(vector(p8 - (xx4*(p8-p9))/300))
        xx4+=1
    elif x<3000:
        angle3 = angle3 + (math.pi/300)
        x3 = 205 + math.cos(angle3)*(15)
        y3 = 80 + math.sin(angle3)*(15)
        z3 = 350
        sc.append(vector(x3,y3,z3))
    elif x<3300:
        angle4 = angle4 + (math.pi/300)
        x4 = 190 + math.sin(angle4)*(-50)
        y4 = 80
        z4 = 300 + math.cos(angle4)*(50)
        sc.append(vector(x4,y4,z4)) 

    
base = shapes.rectangle(width=15,height = 5, scale = 2)
roller = extrusion(pos = sc, shape = base, color=color.white,material = materials.plastic)

column = box(pos=(300,130,250), length=10, height=260, width=10,color=color.white)
column1 = box(pos=(300,130,250), length=10, height=260, width=10,color=color.white)
column2 = box(pos=(300,130,150), length=10, height=260, width=10,color=color.white)
column3 = box(pos=(190,110,150), length=10, height=220, width=10,color=color.white)
column4 = box(pos=(190,110,50), length=10, height=220, width=10,color=color.white)
column5 = box(pos=(270,40,350), length=10, height=80, width=10,color=color.white)
column6 = box(pos=(220,40,350), length=10, height=80, width=10,color=color.white)
column7 = box(pos=(190,40,350), length=10, height=80, width=10,color=color.white)
column8 = box(pos=(300,75,50), length=10, height=150, width=10,color=color.white)
column9 = box(pos=(300,75,350), length=10, height=150, width=10,color=color.white)
i = 1000
while (i < 3300):
    rate(200)
    marble.pos = sc[i] + vector(12,12,12)
    i = i + 1


