import random
import sys
import curses

def battleship():
    screen = curses.initscr()
    player_board = []
    comp_board = []
    player_view_board = []
    comp_view_board = []

    def wait():
        screen.addstr(40, 0, 'Press any key to continue...')
        screen.refresh()
        key = screen.getch()

    def make_player_board():
        for i in range(0, 10):
            pb = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            player_board.append(pb)
        return player_board

    def make_comp_board():
        for i in range (0, 10):
            cb = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            comp_board.append(cb)
        return comp_board

    def make_comp_ship1():
        xc = random.randint(0, 8)
        yc = random.randint(0, 8)
        xoye = random.randint(0, 2)

        if xoye == 1:
            xc2 = xc + 1
            comp_board[xc][yc] = '1'
            comp_board[xc2][yc] = '1'


        else:
            yc2 = yc + 1
            comp_board[xc][yc] = '1'
            comp_board[xc][yc2] = '1'

    def make_comp_ship2():
        xc = random.randint(0, 7)
        yc = random.randint(0, 7)
        xoye = random.randint(0, 2)

        if xoye == 1:
            xc2 = xc + 1
            xc3 = xc2 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc2][yc] == 'O' and comp_board[xc3][yc] == 'O':
                    comp_board[xc][yc] = '2'
                    comp_board[xc2][yc] = '2'
                    comp_board[xc3][yc] = '2'
                    break

                else:
                    xc = random.randint(0, 7)
                    yc = random.randint(0, 7)
                    xc2 = xc + 1
                    xc3 = xc2 + 1
                    continue

        else:
            yc2 = yc + 1
            yc3 = yc2 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc][yc2] == 'O' and comp_board[xc][yc3] == 'O':
                    comp_board[xc][yc] = '2'
                    comp_board[xc][yc2] = '2'
                    comp_board[xc][yc3] = '2'
                    break

                else:
                    xc = random.randint(0, 7)
                    yc = random.randint(0, 7)
                    yc2 = yc + 1
                    yc3 = yc2 + 1
                    continue

    def make_comp_ship3():
        xc = random.randint(0, 7)
        yc = random.randint(0, 7)
        xoye = random.randint(0, 2)

        if xoye == 1:
            xc2 = xc + 1
            xc3 = xc2 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc2][yc] == 'O' and comp_board[xc3][yc] == 'O':
                    comp_board[xc][yc] = '3'
                    comp_board[xc2][yc] = '3'
                    comp_board[xc3][yc] = '3'
                    break

                else:
                    xc = random.randint(0, 7)
                    yc = random.randint(0, 7)
                    xc2 = xc + 1
                    xc3 = xc2 + 1
                    continue

        else:
            yc2 = yc + 1
            yc3 = yc2 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc][yc2] == 'O' and comp_board[xc][yc3] == 'O':
                    comp_board[xc][yc] = '3'
                    comp_board[xc][yc2] = '3'
                    comp_board[xc][yc3] = '3'
                    break

                else:
                    xc = random.randint(0, 7)
                    yc = random.randint(0, 7)
                    yc2 = yc + 1
                    yc3 = yc2 + 1
                    continue

    def make_comp_ship4():
        xc = random.randint(0, 6)
        yc = random.randint(0, 6)
        xoye = random.randint(0, 2)

        if xoye == 1:
            xc2 = xc + 1
            xc3 = xc2 + 1
            xc4 = xc3 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc2][yc] == 'O' and comp_board[xc3][yc] == 'O' and comp_board[xc4][yc] == 'O':
                    comp_board[xc][yc] = '4'
                    comp_board[xc2][yc] = '4'
                    comp_board[xc3][yc] = '4'
                    comp_board[xc4][yc] = '4'
                    break

                else:
                    xc = random.randint(0, 6)
                    yc = random.randint(0, 6)
                    xc2 = xc + 1
                    xc3 = xc2 + 1
                    xc4 = xc3 + 1
                    continue

        else:
            yc2 = yc + 1
            yc3 = yc2 + 1
            yc4 = yc3 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc][yc2] == 'O' and comp_board[xc][yc3] == 'O' and comp_board[xc][yc4] == 'O':
                    comp_board[xc][yc] = '4'
                    comp_board[xc][yc2] = '4'
                    comp_board[xc][yc3] = '4'
                    comp_board[xc][yc4] = '4'
                    break

                else:
                    xc = random.randint(0, 6)
                    yc = random.randint(0, 6)
                    yc2 = yc + 1
                    yc3 = yc2 + 1
                    yc4 = yc3 + 1
                    continue

    def make_comp_ship5():
        xc = random.randint(0, 5)
        yc = random.randint(0, 5)
        xoye = random.randint(0, 2)

        if xoye == 1:
            xc2 = xc + 1
            xc3 = xc2 + 1
            xc4 = xc3 + 1
            xc5 = xc4 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc2][yc] == 'O' and comp_board[xc3][yc] == 'O' and comp_board[xc4][yc] == 'O' and comp_board[xc5][yc] == 'O':
                    comp_board[xc][yc] = '5'
                    comp_board[xc2][yc] = '5'
                    comp_board[xc3][yc] = '5'
                    comp_board[xc4][yc] = '5'
                    comp_board[xc5][yc] = '5'
                    break

                else:
                    xc = random.randint(0, 5)
                    yc = random.randint(0, 5)
                    xc2 = xc + 1
                    xc3 = xc2 + 1
                    xc4 = xc3 + 1
                    xc5 = xc4 + 1
                    continue

        else:
            yc2 = yc + 1
            yc3 = yc2 + 1
            yc4 = yc3 + 1
            yc5 = yc4 + 1

            while True:
                if comp_board[xc][yc] == 'O' and comp_board[xc][yc2] == 'O' and comp_board[xc][yc3] == 'O' and comp_board[xc][yc4] == 'O' and comp_board[xc][yc5] == 'O':
                    comp_board[xc][yc] = '5'
                    comp_board[xc][yc2] = '5'
                    comp_board[xc][yc3] = '5'
                    comp_board[xc][yc4] = '5'
                    comp_board[xc][yc5] = '5'
                    break

                else:
                    xc = random.randint(0, 5)
                    yc = random.randint(0, 5)
                    yc2 = yc + 1
                    yc3 = yc2 + 1
                    yc4 = yc3 + 1
                    yc5 = yc4 + 1
                    continue

    def make_player_ship1():
        screen.addstr(0, 0, 'We will generate your first ship. Please answer the following questions correctly, because if your answer doesn\'t meet our set requirements, the question will be asked again.\n')
        screen.refresh()
        wait()
        while True:
            try:
                screen.clear()
                prompt_str = 'Where do you want the first x coordinate of this ship to be? Enter a number between 0 to 9: '
                l = len(prompt_str)
                screen.addstr(0, 0, prompt_str)
                x = int(screen.getstr(0, l))
                while x >= 10 or x <= -1:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
                    screen.clear()
                    screen.addstr(0, 0, prompt_str)
                    x = int(screen.getstr(0, l))
                break
            except:
                screen.clear()
                screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                screen.refresh()
                wait()
        screen.clear()
        wait()
        while True:
            try:
                prompt_str = 'Where do you want the first y coordinate of this ship to be? Enter a number between 0 to 9: '
                l = len(prompt_str)
                screen.addstr(0, 0, prompt_str)
                y = int(screen.getstr(0, l))
                while y >= 10 or y <= -1:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
                    screen.clear()
                    screen.addstr(0, 0, prompt_str)
                    y = int(screen.getstr(0, l))
                break
            except:
                screen.clear()
                screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                screen.refresh()
                wait()
        screen.clear()
        wait()
        xc = x
        yc = 9 - y
        if xc == 0 and yc != 0 and yc != 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'down' and zc != 'right':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif xc == 9 and yc != 0 and yc != 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or left: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'down' and zc != 'left':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif yc == 0 and xc != 0 and xc != 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter down, left, or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'left' and zc != 'down' and zc != 'right':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif yc == 9 and xc != 0 and xc != 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'left' and zc != 'right':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif xc == 0 and yc == 0:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter down or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'down' and zc != 'right':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif xc == 0 and yc == 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'right':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif xc == 9 and yc == 9:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up or left: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'left':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        elif xc == 9 and yc == 0:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter down or left: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'left' and zc != 'down':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()

        else:
            while True:
                try:
                    prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, left, or right: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    zc = screen.getstr(0, l).lower()
                    while zc != 'up' and zc != 'down' and zc != 'right' and zc != 'left':
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                    screen.refresh()
                    wait()
        if zc == 'up':
            yc2 = yc - 1
            player_board[yc][xc] = '1'
            player_board[yc2][xc] = '1'
        elif zc == 'down':
            yc2 = yc + 1
            player_board[yc][xc] = '1'
            player_board[yc2][xc] = '1'
        elif zc == 'right':
            xc2 = xc + 1
            player_board[yc][xc] = '1'
            player_board[yc][xc2] = '1'
        else:
            xc2 = xc - 1
            player_board[yc][xc] = '1'
            player_board[yc][xc2] = '1'
        screen.clear()
        wait()
        screen.clear()
        screen.refresh()

    def make_player_ship2():
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Now we will generate your second ship. Please answer the following questions correctly, because if your answer doesn\'t meet our set requirements, the question will be asked again.\n')
        screen.refresh()
        wait()
        while True:
            while True:
                try:
                    screen.clear()
                    prompt_str = 'Where do you want the first x coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    x = int(screen.getstr(0, l))
                    while x >= 10 or x <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        x = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            while True:
                try:
                    prompt_str = 'Where do you want the first y coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    y = int(screen.getstr(0, l))
                    while y >= 10 or y <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        y = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            xc = x
            yc = 9 - y
            if xc <= 1 and yc != 1 and yc != 8 and yc != 0 and yc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc != 1 and yc != 8 and yc != 0 and yc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc <= 1 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'left' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc >= 8 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 1 and yc <= 1:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 1 and yc >= 8:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc >= 8:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc <= 1:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            else:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                screen.clear()
                wait()
            if zc == 'up':
                yc2 = yc - 1
                yc3 = yc - 2
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O':
                    player_board[yc][xc] = '2'
                    player_board[yc2][xc] = '2'
                    player_board[yc3][xc] = '2'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'down':
                yc2 = yc + 1
                yc3 = yc + 2
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O':
                    player_board[yc][xc] = '2'
                    player_board[yc2][xc] = '2'
                    player_board[yc3][xc] = '2'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'right':
                xc2 = xc + 1
                xc3 = xc + 2
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O':
                    player_board[yc][xc] = '2'
                    player_board[yc][xc2] = '2'
                    player_board[yc][xc3] = '2'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            else:
                xc2 = xc - 1
                xc3 = xc - 2
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O':
                    player_board[yc][xc] = '2'
                    player_board[yc][xc2] = '2'
                    player_board[yc][xc3] = '2'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
        screen.clear()
        wait()

    def make_player_ship3():
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Now we will generate your third ship. Please answer the following questions correctly, because if your answer doesn\'t meet our set requirements, the question will be asked again.\n')
        screen.refresh()
        wait()
        while True:
            while True:
                try:
                    screen.clear()
                    prompt_str = 'Where do you want the first x coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    x = int(screen.getstr(0, l))
                    while x >= 10 or x <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        x = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            while True:
                try:
                    prompt_str = 'Where do you want the first y coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    y = int(screen.getstr(0, l))
                    while y >= 10 or y <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        y = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            xc = x
            yc = 9 - y
            if xc <= 1 and yc != 1 and yc != 8 and yc != 0 and yc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc != 1 and yc != 8 and yc != 0 and yc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc <= 1 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'left' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc >= 8 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'right' and zc != 'left' and zc != 'down':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 1 and yc <= 1:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 1 and yc >= 8:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc >= 8:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 8 and yc <= 1:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            else:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                screen.clear()
                wait()
            if zc == 'up':
                yc2 = yc - 1
                yc3 = yc - 2
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O':
                    player_board[yc][xc] = '3'
                    player_board[yc2][xc] = '3'
                    player_board[yc3][xc] = '3'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'down':
                yc2 = yc + 1
                yc3 = yc + 2
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O':
                    player_board[yc][xc] = '3'
                    player_board[yc2][xc] = '3'
                    player_board[yc3][xc] = '3'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'right':
                xc2 = xc + 1
                xc3 = xc + 2
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O':
                    player_board[yc][xc] = '3'
                    player_board[yc][xc2] = '3'
                    player_board[yc][xc3] = '3'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            else:
                xc2 = xc - 1
                xc3 = xc - 2
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O':
                    player_board[yc][xc] = '3'
                    player_board[yc][xc2] = '3'
                    player_board[yc][xc3] = '3'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
        screen.clear()
        wait()
    def make_player_ship4():
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Now we will generate your fourth ship. Please answer the following questions correctly, because if your answer doesn\'t meet our set requirements, the question will be asked again.\n')
        screen.refresh()
        wait()
        while True:
            while True:
                try:
                    screen.clear()
                    prompt_str = 'Where do you want the first x coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    x = int(screen.getstr(0, l))
                    while x >= 10 or x <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        x = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            while True:
                try:
                    prompt_str = 'Where do you want the first y coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    y = int(screen.getstr(0, l))
                    while y >= 10 or y <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        y = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            xc = x
            yc = 9 - y
            if xc <= 2 and yc != 1 and yc != 8 and yc != 0 and yc != 9 and yc != 2 and yc != 7:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 7 and yc != 1 and yc != 8 and yc != 0 and yc != 9 and yc != 2 and yc != 7:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc <= 2 and xc != 2  and xc != 7 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'left' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc >= 7 and xc != 2  and xc != 7 and xc != 1 and xc != 8 and xc != 0 and xc != 9:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 2 and yc <= 2:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 2 and yc >= 7:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 7 and yc >= 7:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 7 and yc <= 2:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            else:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                screen.clear()
                wait()
            if zc == 'up':
                yc2 = yc - 1
                yc3 = yc - 2
                yc4 = yc - 3
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O' and player_board[yc4][xc] == 'O':
                    player_board[yc][xc] = '4'
                    player_board[yc2][xc] = '4'
                    player_board[yc3][xc] = '4'
                    player_board[yc4][xc] = '4'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'down':
                yc2 = yc + 1
                yc3 = yc + 2
                yc4 = yc + 3
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O' and player_board[yc4][xc] == 'O':
                    player_board[yc][xc] = '4'
                    player_board[yc2][xc] = '4'
                    player_board[yc3][xc] = '4'
                    player_board[yc4][xc] = '4'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'right':
                xc2 = xc + 1
                xc3 = xc + 2
                xc4 = xc + 3
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O' and player_board[yc][xc4] == 'O':
                    player_board[yc][xc] = '4'
                    player_board[yc][xc2] = '4'
                    player_board[yc][xc3] = '4'
                    player_board[yc][xc4] = '4'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            else:
                xc2 = xc - 1
                xc3 = xc - 2
                xc4 = xc - 3
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O' and player_board[yc][xc4] == 'O':
                    player_board[yc][xc] = '4'
                    player_board[yc][xc2] = '4'
                    player_board[yc][xc3] = '4'
                    player_board[yc][xc4] = '4'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
        screen.clear()
        wait()

    def make_player_ship5():
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Now we will generate your fifth ship. Please answer the following questions correctly, because if your answer doesn\'t meet our set requirements, the question will be asked again.\n')
        screen.refresh()
        wait()
        while True:
            while True:
                try:
                    screen.clear()
                    prompt_str = 'Where do you want the first x coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    x = int(screen.getstr(0, l))
                    while x >= 10 or x <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        x = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            while True:
                try:
                    prompt_str = 'Where do you want the first y coordinate of this ship to be? Enter a number between 0 to 9: '
                    l = len(prompt_str)
                    screen.addstr(0, 0, prompt_str)
                    y = int(screen.getstr(0, l))
                    while y >= 10 or y <= -1:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                        screen.refresh()
                        wait()
                        screen.clear()
                        screen.addstr(0, 0, prompt_str)
                        y = int(screen.getstr(0, l))
                    break
                except:
                    screen.clear()
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
            screen.clear()
            wait()
            xc = x
            yc = 9 - y
            if xc <= 3 and yc != 1 and yc != 8 and yc != 0 and yc != 9 and yc != 2 and yc != 7 and yc != 3 and yc != 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 6 and yc != 1 and yc != 8 and yc != 0 and yc != 9 and yc != 2 and yc != 7 and yc != 3 and yc != 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc <= 3 and xc != 2  and xc != 7 and xc != 1 and xc != 8 and xc != 0 and xc != 9 and xc != 3 and xc != 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'left' and zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif yc >= 6 and xc != 2  and xc != 7 and xc != 1 and xc != 8 and xc != 0 and xc != 9 and xc != 3 and xc != 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, left, or rights: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 3 and yc <= 3:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc <= 3 and yc >= 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 6 and yc >= 6:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            elif xc >= 6 and yc <= 3:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter down or left: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'down' and zc != 'left':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()

            else:
                while True:
                    try:
                        prompt_str = 'Which direction do you want your ship to extend in? Enter up, down, left, or right: '
                        l = len(prompt_str)
                        screen.addstr(0, 0, prompt_str)
                        zc = screen.getstr(0, l).lower()
                        while zc != 'up' and zc != 'down' and zc != 'left' and zc != 'right':
                            screen.clear()
                            screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                            screen.refresh()
                            wait()
                            screen.clear()
                            screen.addstr(0, 0, prompt_str)
                            zc = screen.getstr(0, l).lower()
                        break
                    except:
                        screen.clear()
                        screen.addstr(0, 0, 'You didn\'t enter a direction that was allowed.')
                        screen.refresh()
                        wait()
                screen.clear()
                wait()
            if zc == 'up':
                yc2 = yc - 1
                yc3 = yc - 2
                yc4 = yc - 3
                yc5 = yc - 4
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O' and player_board[yc4][xc] == 'O' and player_board[yc5][xc] == 'O':
                    player_board[yc][xc] = '5'
                    player_board[yc2][xc] = '5'
                    player_board[yc3][xc] = '5'
                    player_board[yc4][xc] = '5'
                    player_board[yc5][xc] = '5'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'down':
                yc2 = yc + 1
                yc3 = yc + 2
                yc4 = yc + 3
                yc4 = yc + 4
                if player_board[yc][xc] == 'O' and player_board[yc2][xc] == 'O' and player_board[yc3][xc] == 'O' and player_board[yc4][xc] == 'O' and player_board[yc5][xc] == 'O':
                    player_board[yc][xc] = '5'
                    player_board[yc2][xc] = '5'
                    player_board[yc3][xc] = '5'
                    player_board[yc4][xc] = '5'
                    player_board[yc5][xc] = '5'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            elif zc == 'right':
                xc2 = xc + 1
                xc3 = xc + 2
                xc4 = xc + 3
                xc5 = xc + 4
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O' and player_board[yc][xc4] == 'O' and player_board[yc][xc5] == 'O':
                    player_board[yc][xc] = '5'
                    player_board[yc][xc2] = '5'
                    player_board[yc][xc3] = '5'
                    player_board[yc][xc4] = '5'
                    player_board[yc][xc5] = '5'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
            else:
                xc2 = xc - 1
                xc3 = xc - 2
                xc4 = xc - 3
                xc5 = xc - 4
                if player_board[yc][xc] == 'O' and player_board[yc][xc2] == 'O' and player_board[yc][xc3] == 'O' and player_board[yc][xc4] == 'O' and player_board[yc][xc5] == 'O':
                    player_board[yc][xc] = '5'
                    player_board[yc][xc2] = '5'
                    player_board[yc][xc3] = '5'
                    player_board[yc][xc4] = '5'
                    player_board[yc][xc5] = '5'
                    break
                else:
                    screen.addstr('Your coordinates for this ship are colliding with the coordinates for another ship. Please re-enter the coordinates carefully and pick a direction which won\'t collide with another ship.')
                    wait()
                    continue
        screen.clear()
        wait()

    def print_board(a_board, x = 0, y = 0):
        for i, row in enumerate(a_board):
            screen.addstr(x + i, y + 0, " ".join(row))
            screen.refresh()

    def player_view():
        for i in range(0, 10):
            pv = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            player_view_board.append(pv)
        return player_view_board

    def comp_view():
        for i in range(0, 10):
            cv = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            comp_view_board.append(cv)
        return comp_view_board

    def player_turn():
        #import pdb; pdb.set_trace()
        while True:
            try:
                prompt_str = 'Where do you want the first x coordinate of your guess to be? Enter a number between 0 to 9: '
                l = len(prompt_str)
                screen.addstr(0, 0, prompt_str)
                guessx = int(screen.getstr(0, l))
                screen.clear()
                screen.refresh()
                while guessx >= 10 or guessx <= -1:
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
                    screen.clear()
                    screen.refresh()
                    screen.addstr(0, 0, prompt_str)
                    guessx = int(screen.getstr(0, l))
                    screen.clear()
                    screen.refresh()
                break
            except:
                screen.clear()
                screen.refresh()
                screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                screen.refresh()
                wait()
                screen.clear()
                screen.refresh()

        while True:
            try:
                prompt_str = 'Where do you want the first y coordinate of your guess to be? Enter a number between 0 to 9: '
                l = len(prompt_str)
                screen.addstr(0, 0, prompt_str)
                guessy = int(screen.getstr(0, l))
                screen.clear()
                screen.refresh()
                while guessy >= 10 or guessy <= -1:
                    screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                    screen.refresh()
                    wait()
                    screen.clear()
                    screen.refresh()
                    screen.addstr(0, 0, prompt_str)
                    guessy = int(screen.getstr(0, l))
                    screen.clear()
                    screen.refresh()
                break
            except:
                screen.clear()
                screen.refresh()
                screen.addstr(0, 0, 'You didn\'t enter a number between 0 and 9.')
                screen.refresh()
                wait()
                screen.clear()
                screen.refresh()
        xc = guessx
        yc = 9 - guessy
        screen.clear()
        screen.refresh()
        if comp_board[yc][xc] == 'O' or comp_board[yc][xc] == 'M':
            screen.addstr(0, 0, 'You didn\'t hit any of their ships.')
            screen.addstr(1, 0, 'The following board is your board containing the guesses of where the computer\'s ships are so far:')
            player_view_board[yc][xc] = 'M'
            print_board(player_view_board, x = 2, y = 0)
            screen.refresh()
            wait()
            screen.clear()
            screen.refresh()
        else:
            screen.addstr(0, 0, 'You hit one of the computer\'s ships!')
            screen.addstr(1, 0, 'The following board is your board containing the guesses of where the computer\'s ships are so far:')
            player_view_board[yc][xc] = 'H'
            print_board(player_view_board, x = 2, y = 0)
            screen.refresh()
            wait()
            screen.clear()
            screen.refresh()

    def comp_turn():
        x = None
        y = None
        for i, row in enumerate(player_board):
            for j, item in enumerate(row):
                if item == 'H':
                    xc = j
                    yc = i
                    yc2 = yc - 1
                    yc3 = yc + 1
                    xc2 = xc - 1
                    xc3 = xc + 1
                    if yc2 >= 0 and player_board[yc2][xc] != 'M' and player_board[yc2][xc] != 'H':
                        x = xc
                        y = yc2
                        break
                    elif yc3 <= 9 and player_board[yc3][xc] != 'M' and player_board[yc3][xc] != 'H':
                        x = xc
                        y = yc3
                        break
                    elif xc2 >= 0 and player_board[yc][xc2] != 'M' and player_board[yc][xc2] != 'H':
                        x = xc2
                        y = yc
                        break
                    elif xc3 <= 9 and player_board[yc][xc3] != 'M' and player_board[yc][xc3] != 'H':
                        x = xc3
                        y = yc
                        break
        if x == None or y == None:
            screen.addstr(0, 0, 'The computer is picking randomly!')
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                xc = x
                yc = 9 - y
                if player_board[yc][xc] == 'M' or player_board[yc][xc] == 'H':
                    continue
                else:
                    break
        else:
            screen.addstr(0, 0, 'The computer is picking smartly!')
            xc = x
            yc = y
            y = 9 - y
        screen.addstr(1, 0, 'The computer guessed the coordinates ' + str(x) + ', ' + str(y))
        if player_board[yc][xc] == 'O':
            screen.addstr(2, 0, 'It\'s not a hit!')
            screen.addstr(3, 0, 'So far in the battle, the following board is your board.')
            player_board[yc][xc] = 'M'
            print_board(player_board, x = 4, y = 0)
        else:
            screen.addstr(2, 0, 'It\'s a hit!')
            screen.addstr(3, 0, 'So far in the battle, the following board is your board.')
            player_board[yc][xc] = 'H'
            print_board(player_board, x = 4, y = 0)

    def win():
        pc = 0
        cc = 0
        for row in player_board:
            for item in row:
                if item == 'H':
                    cc += 1
        for row in player_view_board:
            for item in row:
                if item == 'H':
                    pc += 1
        if pc == 17 and cc != 17:
            screen.addstr(0, 0, 'The player has won!')
            wait()
            curses.endwin()
            sys.exit(1)
        elif pc != 17 and cc == 17:
            screen.addstr(0, 0, 'The computer has won!')
            wait()
            curses.endwin()
            sys.exit(1)
        elif pc == 17 and cc == 17:
            screen.addstr(0, 0, 'It\'s a draw!')
            wait()
            curses.endwin()
            sys.exit(1)
        else:
            pass

    def turn():
        count = 0
        while True:
            count += 1
            if count % 2 == 0:
                comp_turn()
                wait()
                screen.clear()
                screen.refresh()
                win()
            else:
                player_turn()
                screen.clear()
                screen.refresh()

    make_player_board()
    make_comp_board()
    make_comp_ship1()
    make_comp_ship2()
    make_comp_ship3()
    make_comp_ship4()
    make_comp_ship5()

    screen.addstr(0, 0, 'This is the game of battleship. It is like the regular battleship, with the same rules, except you will play against the computer. The key is: H = Hit, M = Miss, 1s = Ship 1, 2s = Ship 2, 3s = Ship 3, 4s = Ship 4, 5s = Ship 5, and Os = Unmarked Areas.')
    screen.refresh()
    wait()
    screen.clear()
    screen.refresh()
    prompt_str = 'Do you want to generate your board randomly? y/n:'
    screen.addstr(0, 0, prompt_str)
    generate_player_board_randomly = screen.getstr(0, len(prompt_str)).lower()
    if generate_player_board_randomly == 'y':
        for i, row in enumerate(comp_board):
            for j, item in enumerate(row):
                player_board[i][j] = comp_board[i][j]
        comp_board = []
        make_comp_board()
        make_comp_ship1()
        make_comp_ship2()
        make_comp_ship3()
        make_comp_ship4()
        make_comp_ship5()
    else:
        make_player_ship1()
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Your board looks like this:')
        print_board(player_board, x = 1, y = 0)
        wait()
        screen.clear()
        screen.refresh()


        make_player_ship2()
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Your board looks like this:')
        print_board(player_board, x = 1, y = 0)
        wait()
        screen.clear()
        screen.refresh()


        make_player_ship3()
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Your board looks like this:')
        print_board(player_board, x = 1, y = 0)
        wait()
        screen.clear()
        screen.refresh()

        make_player_ship4()
        screen.clear()
        screen.refresh()
        screen.addstr(0, 0, 'Your board looks like this:')
        print_board(player_board, x = 1, y = 0)
        wait()
        screen.clear()
        screen.refresh()

        make_player_ship5()
        screen.clear()
        screen.refresh()

    screen.clear()
    screen.refresh()
    screen.addstr(0, 0, 'Your final board looks like this:')
    print_board(player_board, x = 1, y = 0)
    wait()
    screen.clear()
    screen.refresh()

    screen.addstr(0, 0, 'Your board containing your guesses of where the computer\'s ships are looks like this:')
    player_view()
    print_board(player_view_board, x = 1, y = 0)
    wait()
    screen.clear()
    screen.refresh()

    turn()

battleship()
