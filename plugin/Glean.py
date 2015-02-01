#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=C0111,W0703,F0401

import vim
from time import time


def cpprun():
    code_f = '/tmp/{0:.6}.cc'.format(time())
    code = list(vim.current.buffer)
    inp = code[code.index('/*GleanStart') + 1: code.index('GleanEnd*/')]
    inp_f = '/tmp/{0:.6}.in'.format(time())
    open(inp_f, 'w').writelines(['\n'.join(inp), '\n'])
    open(code_f, 'w').writelines(['\n'.join(code), '\n'])
    vim.command('!g++ -Wall {0:s} -o {1:s} && echo "---executing..." && {1:s} < {2:s}'.format(
        code_f,
        code_f[:-2],
        inp_f
    ))

def crun():
    code_f = '/tmp/{0:.6}.c'.format(time())
    code = list(vim.current.buffer)
    inp = code[code.index('/*GleanStart') + 1: code.index('GleanEnd*/')]
    inp_f = '/tmp/{0:.6}.in'.format(time())
    open(inp_f, 'w').writelines(['\n'.join(inp), '\n'])
    open(code_f, 'w').writelines(['\n'.join(code), '\n'])
    vim.command('!g++ -Wall {0:s} -o {1:s} && echo "---executing..." && {1:s} < {2:s}'.format(
        code_f,
        code_f[:-2],
        inp_f
    ))

def pyrun():
    code_f = vim.eval("expand('%:p')")
    vim.command('w')
    code = list(vim.current.buffer)
    inp = code[code.index('# GleanStart') + 1: code.index('# GleanEnd')]
    inp_f = '/tmp/{0}.in'.format(time())
    open(inp_f, 'w').writelines(line[1:] + '\n' for line in inp)
    vim.command('!cat {1:s} | python {0:s}'.format(code_f, inp_f))

def main():
    runit = {
        'python': pyrun,
        'cpp': cpprun,
        'c': crun
    }
    runit[vim.eval('&filetype')]()

main()
