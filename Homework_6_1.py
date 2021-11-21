from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    time_sec = (7,2,5)

    def __init__(self):
        self.__color = 'red'

    def chcolors (self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.time_sec[self.colors.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.chcolors()