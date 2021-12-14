
class Staff():

    def __init__(self,status,staff):
        self._status = status
        self._staff = staff

    def change_status(self,stat):
        self._status.order_state_change(stat)