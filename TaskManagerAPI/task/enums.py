from enum import Enum

class status_enum(str , Enum  ):
    T = 'TODO'
    I = 'IN_PROGRESS'
    R =  'RESOLVED'
    D = 'DONE'

class priority_enum(str , Enum):
    L = 'LOW'
    M = 'MEDIUM'
    H = 'HIGH' 
