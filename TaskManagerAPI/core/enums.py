from enum import Enum

class role_enum(str , Enum ):
    admin = 'ADMIN'
    manager = 'MANAGER'
    user = 'USER'