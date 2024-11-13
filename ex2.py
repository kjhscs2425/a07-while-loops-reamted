# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle


turtle.speed(1000)
amount = 1
def circle(amount):
    for i in range(360):
        turtle.forward(amount)
        turtle.right(1)


while True:
    circle(amount)
    turtle.up()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
    '''
    something random to note about this, so it turns our if you look at the forward command in the while true loop and look at the very \
    command the amount = amount + (whatever I decide the final version to be). If you want to make the circles perfectly go around eachother, you take the amount you go forwarod \
    then you double it, and devide by 100. I cant tell if its actually pefect put around there is probully some geometry I can do \
    to prove it, but I find this preatty cool. so if you want to play around with it go ahead
    
    '''

    
    amount=amount+0.2


