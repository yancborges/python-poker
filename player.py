from random import shuffle, randint


class player:

    def __init__(self, hand, name=None):

        self.hand = hand
        if not name:
            self.name = self.get_random_name()
        else:
            self.name = name

    
    def __str__(self):
        return '{}: game: {}'.format(self.name, self.hand.game_name)


    def get_random_name(self):

        ltr = 'qwertyuiopasdfghjklzxcvbnm'
        size = randint(0, 12) + 3
        name = ''

        for i in range(size):
            name += ltr[randint(0, len(ltr) - 1)]

        return name