from enum import Enum
class OrderStatus(Enum):
    CREATED = 'EN PROCESO'
    ACCEPTED = 'EN CAMINO'
    PAYED = 'PAGADO'
    COMPLETED = 'FINALIZADO'
    CANCELED = 'CANCELADO'
    
choices = [(tag, tag.value) for tag in OrderStatus]