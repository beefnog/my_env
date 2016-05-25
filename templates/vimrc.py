header = r"""
" .vimrc

" blowfish is *way* more secure than the old vim crypt method
setlocal cm=blowfish

"set tabstop=4
"set shiftwidth=4
"set ruler
syn on
set number
set ai
set hlsearch
set laststatus=2
set statusline=%t%m%r%h%w\ [lang=%Y]\ [a=\%03.3b\|0x\%02.2B]\ [p=%l,%v][%p%%]
hi StatusLine ctermbg=green ctermfg=black
"""

