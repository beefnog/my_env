header = r"""
" .vimrc

setlocal cm=blowfish2

"set tabstop=4
"set shiftwidth=4
"set ruler
syn on
set number
set ai
set hlsearch
set laststatus=2

set modeline
set modelines=5

set statusline=%t%m%r%h%w\ [lang=%Y]\ [a=\%03.3b\|0x\%02.2B]\ [p=%l,%v][%p%%]
hi StatusLine ctermbg=green ctermfg=black

set mouse=
set ttymouse=
"""

