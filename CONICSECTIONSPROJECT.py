import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import math
mydb=mysql.connector.connect(host='localhost',user='root',passwd='singh2003',database='Conic')
mycursor=mydb.cursor()
x=np.linspace(-80,80,400)
y=np.linspace(-80,80,400)
x,y=np.meshgrid(x,y)

def axes():
    plt.axhline(0,alpha=0.5)
    plt.axvline(0,alpha=0.5)

def conic():
    while True:
        print("Which geometrical figure do you want to plot[Circle,Parabola,Ellipse,Hyperbola,Line]:")
        print("Enter 'None' if you want to quit.")
        q=input()
        flag=0



        if q.capitalize()=='Circle':
            r=int(input('Enter radius:'))
            a=int(input('Enter x co-ordinate of centre:'))
            b=int(input('Enter y co-ordinate of centre:'))
            axes()
            plt.contour(x,y,((x-a)**2/r**2+ (y-b)**2/r**2),[1],colors='k')
            plt.plot(a,b,'.',alpha=1) #centre
            plt.show()
            print('Press the corresonding number to ask the respective questions.')
            mycursor.execute('select*from circle')
            data=mycursor.fetchall()
            for i in data:
                print(i)
            print()
            print('Type 0 to plot another conic section.')
            ans=int(input('....'))
            if ans==0:
                flag=-1
            else:
                x1=int(input('Enter x co-ordinate of point:'))
                y1=int(input('Enter y co-ordinate of point:'))
                pos=((x1-a)**2/r**2 + (y1-b)**2/r**2) -1
                if pos<0:
                    print('Point lies inside circle')
                elif pos==0:
                    print('Point lies on circle')
                    print()
                else:
                    print('Point lies outside circle')
                    print()
    



        elif q.capitalize()=='Parabola':
            a=eval(input('Enter co-ordinates of focus[x,y]:'))
            a1=int(input('Enter x co-ordinate of vertex:'))
            b1=int(input('Enter y co-ordinate of vertex:'))
            axes()
            if int(a[1])==0:
                A=a[1]
                plt.contour(x,y,((y-b1)**2 - 4*A*(x-a1)),[1],colors='k',alpha=1)
                plt.plot(A+a1,b1,'.',alpha=1) #focus
                plt.axvline(-(A+a1),color='red') #directrix
                plt.show()
                graph=1
            else:
                A=a[1]
                plt.contour(x,y,((x-a1)**2 - 4*A*(y-b1)),[1],colors='k',alpha=1)
                plt.plot(a1,A+b1,'.',alpha=1) #focus
                plt.axhline(-(A+a1),color='red') #directrix
                plt.show()
            while True:
                print('Press the corresonding number to ask the respective questions.')
                mycursor.execute('select*from parabola')
                data=mycursor.fetchall()
                for i in data:
                    print(i)
                print( )
                print('Type 0 to plot another conic section.')
                ans=int(input('....'))
                if ans==0:
                    flag=-1
                    break
                elif ans==1:
                    print(4*a,'units')
                    print()
                    pass
                elif ans==2:
                    print('x= -',a)
                    print()
                    pass
                else:
                    x1=int(input('Enter x co-ordinate of point:'))
                    y1=int(input('Enter y co-ordinate of point:'))
                if graph==1:
                    pos=(y1)**2 - 4*a*x1
                    if pos<0:
                        print('Point lies inside parabola')
                        print()
                        pass
                    elif pos==0:
                        print('Point lies on parabola')
                        print()
                        pass
                    else:
                        print('Point lies outside parabola')
                        print()
                        pass
                else:
                    pos=(x1)**2 - 4*a*x1
                    if pos<0:
                        print('Point lies inside parabola')
                        print() 
                        pass
                    elif pos==0:
                        print('Point lies on parabola')
                        print()
                        pass
                    else:   
                        print('Point lies outside parabola')
                        print()
                        pass



        elif q.capitalize()=='Ellipse':
            a=int(input('Enter length of horizontal axis:'))
            b=int(input('Enter length of vertical axis:'))
            a1=int(input('Enter x co-ordinate of centre:'))
            b1=int(input('Enter y co-ordinate of centre:'))
            axes()
            if a>b:
                plt.contour(x,y,((x-a1)**2/a**2+ (y-b1)**2/b**2),[1],colors='k')
                e=np.sqrt(1- b**2/a**2) #eccentricity
                plt.plot((a+a1)*e,b1,'.',(-a+a1)*e,b1,'.') #Foci
                plt.axvline((a+a1)/e,color='green'),plt.axvline(-(a+a1)/e,color='yellow') #Directrices
                plt.show()
                lr=2*(b**2)/a
            else:
                plt.contour(x,y,((x-a1)**2/a**2+ (y-b1)**2/b**2),[1],colors='k')
                e=np.sqrt(1- a**2/b**2) #eccentricity
                plt.plot(a1,(b+b1)*e,'.',a1,(-b+b1)*e,'.') #Foci
                plt.axhline((b+a1)/e,color='green'),plt.axhline(-(b+a1)/e,color='yellow') #Directrices
                plt.show()
                lr=2*(a**2)/b
            while True:
                print('Press the corresonding number to ask the respective questions.')
                mycursor.execute('select*from ellipse')
                data=mycursor.fetchall()
                for i in data:
                    print(i)
                print( )
                print('Type 0 to plot another conic section.')
                ans=int(input('....'))
                if ans==0:
                    flag=-1
                    break
                else:
                    if ans==1:
                        print(e)
                        print()
                        pass
                    else:
                        print(lr)
                        print()
                        pass




        elif q.capitalize()=='Hyperbola':
            a=int(input('Enter length of Tranverse axis:'))
            b=int(input('Enter length of Conjugate axis:'))
            axes()
            e=(np.sqrt(a**2 +b**2))/a
            plt.contour(x,y,(x**2/a**2 - y**2/b**2),[1],colors='k')
            plt.show()
            lr=(2*b**2)/a
            while True:
                print('Press the corresonding number to ask the respective questions.')
                mycursor.execute('select*from hyperbola')
                data=mycursor.fetchall()
                for i in data:
                    print(i)
                print( )
                print('Type 0 to plot another conic section.')
                ans=int(input('....'))
                if ans==0:
                    flag=-1
                    break
                else:
                    if ans==1:
                        print(e)
                        print()
                        pass
                    else:
                        print(lr)
                        print()
                        pass



        elif q.capitalize()=='Line':
            print('Enter co-ordinates of any two points lying on the line.')
            a1=int(input('Enter x co-ordinate of the first point:'))
            b1=int(input('Enter y co-ordinate of the first point:'))
            a2=int(input('Enter x co-ordinate of the second point:'))
            b2=int(input('Enter y co-ordinate of the first point:'))
            m=(a2-a1)/(b2-b1)
            axes()
            plt.plot([a1,a2],[b1,b2])
            plt.show()
            while True:
                print('Press the corresonding number to ask the respective questions.')
                mycursor.execute('select*from Line')
                data=mycursor.fetchall()
                for i in data:
                    print(i)
                print( )
                print('Type 0 to plot another conic section.')
                ans=int(input('....'))
                if ans==0:
                    flag=-1
                    break
                else:
                    if ans==1:
                        print(m)
                        print()
                        pass
                    else:
                        theta= math.atan(m)
                        f=math.degrees(theta)
                        print('The angle made with x axis is:',f,'degrees')
                        print()
                        pass



        elif q.capitalize()=='None':
            flag=-1
            break   
        
        else:
            print('Conic section Unavavailable!!')
    return flag
flag1=conic()
while True:
    if flag1==-1:
        break
    else:
        conic()
        continue