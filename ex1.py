# Use turtle graphics to make an infinite spiral

import turtle

#so turns out if you do the tool that instentlly draws something, WHEN YOU HAVE A INFINIT STRING, your computer crashes. 
turtle.speed(1000)

def infinit_spiral():
    i=1
    while(True):
       
       turtle.forward(i)
       turtle.right(1)
       i = i+0.001


infinit_spiral()

