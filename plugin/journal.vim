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

func! g:OpenJournal(...)
	py3 << EOF
	from journal import Journals

	journals_dir = vim.eval('g:journals_directory')
	journals = Journals(journals_dir)
	path = journals.open()
	vim.command(f":e {path}")

	EOF
endfunc

func! g:SearchJournal(...)
	py3 << EOF
	from journal import Journals

	journals_dir = vim.eval('g:journals_directory')
	journals = Journals(journals_dir)

	search_term = vim.eval("a:1")

	entries = journals.search_single_word(search_term)
	for entry in entries:
		print(entries)

	EOF
endfunc

command! -bar -bang Journal call OpenJournal()
command! -bar -bang -nargs=? JournalSearch call SearchJournal(<q-args>)
