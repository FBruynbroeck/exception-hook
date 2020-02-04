# encoding: utf-8
from hook import exception_hook

import sys

sys.excepthook = exception_hook


class User(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


def main():
    users = []
    users.append(User('Pierre', 'Dupont'))
    users.append(User('Paul', 'Dupond'))
    users.append(User('Jacque', 'Foo'))
    users.append(None)
    for user in users:
        print "%s %s" % (user.firstname, user.lastname)


if __name__ == '__main__':
    main()
