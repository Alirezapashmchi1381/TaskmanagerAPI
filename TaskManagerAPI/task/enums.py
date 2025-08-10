from enum import Enum

class status_enum(str , Enum  ):
    Todo = 'TODO'
    InProgress = 'IN_PROGRESS'
    Resolved =  'RESOLVED'
    Done = 'DONE'

class priority_enum(str , Enum):
    Low = 'LOW'
    Medium = 'MEDIUM'
    High = 'HIGH' 
