
class Food: # TODO refactor code for consistency with main.py
    def starving(moves, head, food):
        move = get_food(moves, head, food)

        if (not (move == None)):
            return move

        for f in food:
            xdist = f[0] - head[0]
            ydist = f[1] - head[1]

            if ((abs(xdist) == 2 and ydist == 0) ^ (abs(ydist) == 2 and xdist == 0)):

                if (xdist == 2 and 'right' in moves):
                    return 'right'

                elif (xdist == -2 and 'left' in moves):
                    return 'left'

                elif (ydist == 2 and 'down' in moves):
                    return 'down'

                elif (ydist == -2 and 'up' in moves):
                    return 'up'

    def get_food(moves, head, food):
        for f in food:
            xdist = f[0] - head[0]
            ydist = f[1] - head[1]

            if ((abs(xdist) == 1 and ydist == 0) ^ (abs(ydist) == 1 and xdist == 0)):

                if (xdist == 1 and 'right' in moves):
                    return 'right'

                elif (xdist == -1 and 'left' in moves):
                    return 'left'

                elif (ydist == 1 and 'down' in moves):
                    return 'down'

                elif (ydist == -1 and 'up' in moves):
                    return 'up'