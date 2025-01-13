from abc import ABCMeta, abstractclassmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, user : User):
        raise NotImplementedError
    
    @abstractclassmethod
    def find_by_email(self, email:str) -> User:
        #이메일로 유저 검색 -> 없다면 422애러
        raise NotImplementedError

