import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for x,y in kwargs.items():
            for i in range(int(y)):
                self.contents.append(x)
    
    def draw(self, num):
        draw_balls = []
        if num >= len(self.contents):
            draw_balls = self.contents
            self.contents = []
            return draw_balls

        for i in range(num):
            rand = random.randrange(0, len(self.contents))
            draw_balls.append(self.contents.pop(rand))
        return draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    for i in range(num_experiments):
        dic = {}
        flag = True
        c = copy.deepcopy(hat)
        drawn_balls = c.draw(num_balls_drawn)

        for j in drawn_balls:
            dic[j] = dic.get(j, 0) + 1

        for j in expected_balls.keys():
            if (j not in dic.keys()) or (dic[j] < expected_balls[j]):
                flag = False
                break

        if flag:
            match += 1

    prob = match / num_experiments

    return prob
