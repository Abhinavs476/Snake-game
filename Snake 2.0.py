import curses
from random import randint
name = str(input("Enter name: "))
choice = 1
high = 0
while choice == 1:
    curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    win = curses.newwin(30,90,15,60)
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    snake = [(4,10),(4,9),(4,8)]
    food = (randint(1,28),randint(1,88))
    ESC = 27
    key = curses.KEY_RIGHT
    score = 0
    reason = 0
    win.addch(food[0],food[1],"+")
    while key!=ESC:
        win.addstr(0,2, "Score : " + str(score)+" ")
        win.addstr(0,70, "High score : " + str(high)+" ")
        win.addstr(0,35, "Player : " + str(name)+" ")
        win.timeout(100)

        prev_key = key
        event = win.getch()
        key = event if event!= 1 else prev_key

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = prev_key

        #next coordinates

        y = snake[0][0]
        x = snake[0][1]

        if key == curses.KEY_DOWN: 
            y+=1
        if key == curses.KEY_UP:
            y-=1
        if key == curses.KEY_LEFT:
            x-=1
        if key == curses.KEY_RIGHT:
            x+=1
        snake.insert(0,(y,x))

        #check border

        if y==0: 
            reason = 1
            break
        if x==0: 
            reason = 1
            break
        if y==29: 
            reason = 1
            break
        if x==89: 
            reason = 1
            break

        #if snake bites itself

        if snake[0] in snake[1:] : 
            reason = 2
            break

        #check if food is eaten

        if snake[0] == food:
            score+=1
            food = ()
            while food == ():
                food = (randint(1,28), randint(1,88))
                if food in snake:
                    food = ()
            
            win.addch(food[0],food[0],"+")

        else:
            #snake moves
            last = snake.pop()
            win.addch(last[0],last[1], " ")
        win.addch(snake[0][0], snake[0][1], "*")


        '''
        if event == ord("q"):
            break
        for c in snake: 
            win.addch(c[0],c[1],"*")
        '''
    if score>high:
        high = score
    curses.beep()
    curses.delay_output(900)
    win.clear()
    curses.endwin()

    print("Cause of death:")
    if reason == 1:
        print("Hit a wall")
    if reason == 2:
        print("Bit itself")
    print("Score: " + str(score))
    print("High score: " + str(high))
    print("Wanna play again?")
    choice = int(input("Enter 1 for YES and 2 for NO: "))