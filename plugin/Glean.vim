if !has('python')
    echo "Error: Glean requires vim to be compiled with python>=2.7"
    finish
endif
let s:pyscript = resolve(expand('<sfile>:p:h:h')) . "/plugin/Glean.py"
function! Glean()
    execute 'pyfile ' s:pyscript
endfunc


command! Glean call Glean()
