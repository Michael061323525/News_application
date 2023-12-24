from abc import ABC, abstractmethod


class ExternalServiceInterface(ABC):

    @abstractmethod
    def get_data(self):
        pass
