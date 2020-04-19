import certifi
import urllib3
import url_con_man.constants as UrlConstants


class PoolMan():
    REQUEST_ACTIONS = ['GET', 'POST']
    RETRIES = [3, 10, 100, True, False]
    _http = None
    _url = ""
    _action = 'GET'  # defined in constants.
    _retries = True  # default to 3 retries with follow
    _action_constants = REQUEST_ACTIONS
    _retry_constants = RETRIES



    def __init__(self) -> object:
        # c = UrlConstants
        # _action_constants = c.UrlConstants.actions
        # _retry_constants = c.UrlConstants.retries
        try:
            # Set up the pool mannager session
            self._http = urllib3.PoolManager(ca_certs=certifi.where())
        except:
            raise Exception('Something went wrong creating the PoolManager!')

    @property
    def url(self):  # getter
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def action(self):  # getter
        return self._action

    @action.setter
    def action(self, value):
        # assert value in self._action_constants, "Allowed values are [{}]".format(self._action_constants)
        if value in self._action_constants:
            self._action = value
        else:
            raise Exception("Allowed values are [{}]".format(str(self._action_constants)))

    @property
    def retries(self):  # getter
        return self._retries

    @retries.setter
    def retries(self, value):
        # assert value in self._retry_constants , "Allowed values are [{}]".format(self._retry_constants)
        if value in self._retry_constants:
            self._retries = value
        else:
            raise Exception("Allowed values are [{}]".format(str(self._retry_constants)))

    def __str__(self):
        return '{}'.format(self.url)

    def __eq__(self, other):
        return self.url == other.url

    def request(self):
        # assert len(self._url) > 0, "There doesnt appear to be a valid request string to process"
        if len(self._url) > 0:
            try:
                resp = self._http.request(self._action, self._url)
            except:
                raise Exception('Something went wrong!')
        else:
            raise Exception("There doesnt appear to be a valid request string to process")

        return resp
