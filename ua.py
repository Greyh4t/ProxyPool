#coding:utf-8
import codecs
import json
import random

class UserAgent(object):
    def __init__(self):
        self.data = self.load('ua.json')
        self.SHORTCUTS = {
            'ie': 'internetexplorer',
        }

    def load(self, db):
        with codecs.open(db, encoding='utf-8', mode='rb',) as fp:
            return json.load(fp)
        
    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __getattr__(self, attr):
        attr = attr.lower()

        if attr == 'random':
            attr = self.data['randomize'][
                str(random.randint(0, len(self.data['randomize']) - 1))
            ]
        else:
            if attr in self.SHORTCUTS:
                attr = self.SHORTCUTS[attr]

        try:
            return self.data['browsers'][attr][
                random.randint(
                    0, len(self.data['browsers'][attr]) - 1
                )
            ]
        except KeyError:
            return None
