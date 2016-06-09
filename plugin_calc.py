import dmenu_extended
from numpy import *
import sh


def paste(str, p=True, c=True):
    from subprocess import Popen, PIPE

    if p:
        p = Popen(['xsel', '-pi'], stdin=PIPE)
        p.communicate(input=str)
    if c:
        p = Popen(['xsel', '-bi'], stdin=PIPE)
        p.communicate(input=str)


class extension(dmenu_extended.dmenu):

    # Set the name to appear in the menu
    title = '='

    # Determines whether to attach the submenu indicator
    is_submenu = True

    # Required function, runs when the user fires the menu item
    def run(self, inputText):
        inp = inputText
        if inp != '':
            res = self.evalExpression(inputText)
            self.printResult(inp, res)
        else:
            inp = ''
            while inp == '':
                inp = self.menu('', prompt='Query:=')

            res = self.evalExpression(inp)
            self.printResult(inp, res)
            # self.menu(input='Enter question:')

        # try:
        #     res = eval(inp[1:])
        #     self.menu('{}= {}'.format(inp[1:], res))
        # except:
        #     self.menu('You have just fired the example plugin')
        #     res = ''

    def printResult(self, query, result):
        result = self.evalExpression(query)
        yOrN = self.menu('{} = {}'.format(query, result))

        if yOrN.trim().lower() == 'y':
            paste(c=result)

    def evalExpression(self, expr):
        try:
            res = eval(expr)
        except:
            res = ''
        return res
