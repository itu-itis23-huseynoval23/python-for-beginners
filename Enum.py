from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State(1)) # ACTIVE
print(State['ACTIVE'].value)# 1
print(list(State)) #State.INACTIVE: 0 State.ACTIVE: 1