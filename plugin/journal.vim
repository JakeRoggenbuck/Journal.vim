" journal.vim
" Authors:      Jake Roggenbuck
" Version:      0.1
" License:      MIT

if exists('g:loaded_journal_plugin') || &compatible || v:version < 700
	finish
endif

let g:loaded_journal_plugin = 1

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

func! s:SourcePython()
py3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF
endfunc


call s:SourcePython()


func! g:NewDraft(...)
py3 << EOF
from journal import Journals
EOF
endfunc
