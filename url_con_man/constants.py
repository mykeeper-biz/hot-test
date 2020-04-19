
class UrlConstants():
    REQUEST_ACTIONS = ['GET', 'POST']
    RETRIES = [3, 10, 100, True, False]

    def __init__(self):
        pass

    @property
    def actions(self):  # getter
        return self.REQUEST_ACTIONS

    @property
    def retries(self):  # getter
        return self.RETRIES

