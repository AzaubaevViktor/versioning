##INSTALL##
Добавьте в конец файла `./git/hooks/pre-commit`   
такие строки:   
```
echo "Set version"
$LANG = "%lang%"
$PATH = "%path/to/file%"
./version_set.py $LANG $PATH
git add $PATH
```