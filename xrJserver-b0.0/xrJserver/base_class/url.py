from re import match


class url(object):
    def __init__(self, path, view):
        self.__url_tab = []
        self.__url_tab.append((path, view))

    def verify(self, path):
        for __url in self.__url_tab:
            if match(__url[0], path):
                return __url
        return False

    def get_url_tab(self):
        return self.__url_tab

    def insert_url(self, path, view):
        self.__url_tab.append((path, view))

