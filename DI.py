from dependency_injector import containers, providers
from Pipeline.Producer import Producer
from Pipeline.Consumer import Consumer


class DependencyContainer (containers.DeclarativeContainer):
    quequeService = providers.Singleton(Producer)
    consumerService = providers.Singleton(Consumer,quequeService) 