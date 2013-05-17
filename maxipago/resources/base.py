# coding: utf-8


class Resource(object):

    def __init__(self, data, requester, manager):
        self.data = data
        self.requester = requester
        self.manager = manager
        self.process()

    def process(self):
        raise NotImplementedError()
