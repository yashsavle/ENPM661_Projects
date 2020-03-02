from math import*

# return "1" if colliding with obstacle or else zero

def obstactle_check(x,y,r,c):
#circle
    circle = (x-225)**2 + (y-150)**2 - ((25+ r + c))**2
    if circle <=0:
        return 1
#ellipse
    ellipse= ((x-150)/(40+r+c))**2 + ((y-100)/(20+r+c))**2 -1
    if ellipse<=0:
        return 1


    # square
    l1 = (y + (0.6*x) -145)
    l2 = (y - 0.2*x + 35)
    l3 = (y + x - 265)
    l4 = (y - x -185)
    d1= (0.6*x - y -145)/(sqrt(0.6**2 + 1)) -(r+c)
    d2 = (abs(-0.2*x - y +35))/(sqrt(0.2**2 + 1)) -(r+c)
    d3 = (abs(x - y + 265))/(sqrt(1 + 1)) -(r+c)
    d4 = (abs(-x + y -185))/(sqrt(2)) -(r+c)

    if l1 >= 0 and l2 >= 0 and l3 <= 0 and l4 <= 0 :
        return 1

    #check for rigid
    if r!=0:
        if l1 < 0 and l2>=0 and l4 <= 0:
            if d1 < 0:
                return 1
            elif l1 < 0 and l2<=0 and l4 <= 0:
                if ((abs(sqrt((x-225)**2 + (y-10)**2))) - (r+c)) < 0:
                    return 1
        if l2 < 0 and l1 >= 0 and l3 <= 0:
            if d2 < 0:
                return 1
        elif l2 < 0 and l1 <= 0 and l3 >= 0:
            if ((abs(sqrt((x - 250) ** 2 + (y - 15) ** 2))) - (r + c)) < 0:
                return 1
        if l3 > 0 and l2 >= 0 and l4 <= 0:
            if d3 < 0:
                return 1
        elif l3 < 0 and l2 >= 0 and l4 <= 0:
            if ((abs(sqrt((x - 225) ** 2 + (y - 40) ** 2))) - (r + c)) < 0:
                return 1

        if l4 > 0 and l1 >= 0 and l3 <= 0:
            if d4 < 0:
                return 1
        elif l4>0 and l1 <= 0 and l3 >= 0:
            if ((abs(sqrt((x - 200) ** 2 + (y - 15) ** 2))) - (r + c)) < 0:
                return 1


 # Rectangle
    l5 = y + 0.577*x - 84.815
    l6 = y - 1.72*x + 133.4
    d5 = (abs(0.577*x + y - 84.815))/(sqrt(0.577**2 + 1)) -(r+c)
    d6 = (abs(-1.72*x + y - 133.4))/(sqrt(1.72**2 + 1)) -(r+c)


    if l5 >= 0:
        if (d5+10 - (r+c)) < 0:
            return 1
    else:
        if (d5 - (r+c)) < 0:
            return 1

    if l6 >= 0:
        if (d6 + 75 - (r + c)) < 0:
            return 1
    else:
        if (d6 - (r + c)) < 0:
            return 1


    # Polygon

    p1 = y -13*x + 140
    p2 = y - x - 100
    p3 = y +  1.2*x - 210
    p4 = y - 1.2*x - 30
    p5 = y + 1.2*x - 275
    p6 = y - 185

    if p1 <= 0 and p2>=0 and p3>=0 and p4>=0 and p5<=0 and p6<=0:
        return 1
    else:
        if


