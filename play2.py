import turtle as t
import random as r

#shark
shark=t.Turtle()
shark.shape("triangle")
shark.color("salmon")
shark.speed(0)
shark.penup()
shark.goto(r.randint(-200,200),r.randint(-200,200))

#plain
plain=t.Turtle()
plain.shape("circle")
plain.color("teal")
plain.speed(0)
plain.penup()
plain.goto(r.randint(-200,200),r.randint(-200,200))

#rock
rock1=t.Turtle()
rock1.shape("circle")
rock1.color("teal")
rock1.speed(0)
rock1.penup()
rock1.goto(r.randint(-200,200),r.randint(-200,200))

rock2=t.Turtle()
rock2.shape("circle")
rock2.color("teal")
rock2.speed(0)
rock2.penup()
rock2.goto(r.randint(-200,200),r.randint(-200,200))


class Game():
    def turn_right(self):
        t.setheading(0)

    def turn_up(self):
        t.setheading(90)

    def turn_left(self):
        t.setheading(180)

    def turn_down(self):
        t.setheading(270)

    def play(self):
        t.clear()
        t.forward(15)
        ang=shark.towards(t.pos())
        shark.setheading(ang)
        shark.forward(13)

        duration=0
        if t.distance(plain)<15:
            self.result("find plain",duration)

        elif t.distance(rock1)<15 or t.distance(rock2)<15:
            duration=1
            self.result("it's rock",duration)

        elif t.distance(shark)<15:
            self.result("try again",duration)

        else:
            t.ontimer(g.play,100)
            
    def result(self,msg,dur):
        if dur==1:
            t.forward(15)
            t.write(msg,False,"center",("",20))
        else:
            t.goto(0,0)
            t.write(msg,False,"center",("",20))
            shark.goto(r.randint(-200,200),r.randint(-200,200))
            plain.goto(r.randint(-200,200),r.randint(-200,200))
            rock1.goto(r.randint(-200,200),r.randint(-200,200))
            rock2.goto(r.randint(-200,200),r.randint(-200,200))
g=Game()
t.setup(450,450)
t.bgcolor("lightsteelblue")
t.shape("turtle")
t.speed(0)
t.penup()
t.goto(0,0)
t.color("white")
t.onkeypress(g.turn_right,"Right")
t.onkeypress(g.turn_up,"Up")
t.onkeypress(g.turn_left,"Left")
t.onkeypress(g.turn_down,"Down")
t.onkeypress(g.play,"space")
t.listen()










                       

                
        
