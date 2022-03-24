# coding: utf-8


class Maxipago(object):

    def __init__(self, maxid, api_key, api_version='3.1.1.15', sandbox=False):
        self.maxid = maxid
        self.api_key = api_key
        self.api_version = api_version
        self.sandbox = sandbox

    def __getattr__(self, name):
        try:
            class_name = ''.join([n.title() for n in name.split('_') + ['manager']])
            module = __import__('maxipago.managers.{0}'.format(name), fromlist=[''])
            klass = getattr(module, class_name)
            return klass(self.maxid, self.api_key, self.api_version, self.sandbox)
        except (ImportError, AttributeError) as e:
            if name in self.__dict__:
                return self.__dict__.get('name')
            else:
                raise AttributeError
