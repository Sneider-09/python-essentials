def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

class Timer:
    def __init__(self, hour = 0, min = 0, sec = 0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec
    
    def __str__(self):
        return two_digits(self.__hour) + ":" + \
               two_digits(self.__min) + ":" + \
               two_digits(self.__sec)
    
    def next_second(self):
        self.__sec += 1
        if self.__sec > 59:
            self.__sec = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hour += 1
                if self.__hour > 23:
                    self.__hour = 0

    def previous_second(self):
        self.__sec -= 1
        if self.__sec < 0:
            self.__sec = 59
            self.__min -= 1
            if self.__min < 0:
                self.__min = 59
                self.__hour -= 1
                if self.__hour < 0:
                    self.__hour = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    