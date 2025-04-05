from collections import deque

class gameStateManager:

    def __init__(self, currentState) -> None:
        self.currentState = currentState
        self.defualtState = self.currentState
        self.previousStates = deque()
        self.previousStates.append(self.defualtState)

    def getState(self):
        return self.currentState
    
    def returnToPrevState(self):
        if len(self.previousStates) > 1:
            self.previousStates.pop()
            self.currentState = self.previousStates[-1]
        else: self.currentState = self.defualtState
    
    def setState(self, state):
        self.currentState = state
        self.previousStates.append(self.currentState)

game_state_manager = gameStateManager('menu')