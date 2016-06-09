import dmenu_extended
from numpy import *
from subprocess import Popen, PIPE


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

    def printResult(self, query, result):
        '''Print the result into the query window in the format query = answer

        :param query: the query
        :param result: the result of the evaluated query

        :type query: str'''
        yOrN = self.menu('{} = {}'.format(query, result))

        if yOrN.trim().lower() == 'y':
            paste(c=result)

    def evalExpression(self, expr):
        '''Eval the expression `expr`. This is *not* safe at all (you can execute
        whatever you like (for example `import sh; sh.rm(r=True, f=True, '/')` will
        delete all the files at the root of your computer.

        :param expr: the expression to parse
        :type expre: str'''
        try:
            res = eval(expr)
        except:
            res = ''
        return res

    def paste(self, str, p=True, c=True):
        '''Method to paste the result contained in str into clipboard.

        :param str: the string to copy in the clipboard
        :param p:   set to True to copy into primary buffer
        :param c:   set to True to copy into third buffer.

        :type str: str
        :type p: bool
        :type c: bool
        '''
        if p:
            p = Popen(['xsel', '-pi'], stdin=PIPE)
            p.communicate(input=str)
        if c:
            p = Popen(['xsel', '-bi'], stdin=PIPE)
            p.communicate(input=str)
