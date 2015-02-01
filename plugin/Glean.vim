if !has('python')
    echo "Error: Glean requires vim to be compiled with python>=2.7"
    finish
endif
function! Glean()
    pyfile Glean.py
endfunc


command! Glean call Glean()
