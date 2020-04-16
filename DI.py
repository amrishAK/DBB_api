from dependency_injector import containers, providers
from Pipeline.Producer import Producer
from Pipeline.Consumer import Consumer
from twoPhaseCommit.Participant import Participant
from Handler.CronHandler import CronJob

class DependencyContainer (containers.DeclarativeContainer):
    quequeService = providers.Singleton(Producer)
    cronService = providers.Singleton(CronJob)
    participantService = providers.Singleton(Participant)
    consumerService = providers.Singleton(Consumer,quequeService) 