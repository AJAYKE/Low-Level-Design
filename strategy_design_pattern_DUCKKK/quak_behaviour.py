from abc import ABC, abstractmethod


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehaviour):
    def quack(self):
        print("I can Quackkkkk")

class Squeak(QuackBehaviour):
    def quack(self):
        print("I can ssqueekkk")

class MuteQuack(QuackBehaviour):
    def quack(self):
        print("I cant quackk")