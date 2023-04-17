from abc import ABC, abstractmethod


class Environment(object):
    @abstractmethod
    def __init__(self, rooms):
        self.rooms = rooms
        self.n = len(rooms)
        self.currentRoom = rooms[0]

    def executeStep(self, n=1, max_steps=None):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n


class Agent:
    def __init__(self):
        pass

    def sense(self, environment):
        pass

    def act(self):
        pass


class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


class VaccumAgent(Agent):
    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        return 'left'


class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, rooms):
        super().__init__(rooms)
        self.agent = agent
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1, max_steps=None):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            else:
                self.currentRoom = self.rooms[(
                    self.rooms.index(self.currentRoom) + 1) % self.n]
            self.displayAction()
            self.step += 1
            if self.step > max_steps:
                break

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n


if __name__ == '__main__':
    vcagent = VaccumAgent()
    rooms = [Room('A', 'dirty'), Room('B', 'clean'),
             Room('C', 'dirty'), Room('D', 'dirty'), Room('E', 'dirty')]
    env = NRoomVaccumCleanerEnvironment(vcagent, rooms)
    env.executeStep(50, (len(rooms)*2))
