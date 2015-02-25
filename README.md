##INSTALL##
Добавьте в конец файла `./git/hooks/pre-commit`   
такие строки:   
```
#!/bin/sh
# Если вы создали новый файл

echo "Set version"
versioning_lang="%lang%"
versioning_path="%path%"
./version_set.py $versioning_lang $versioning_path
git add $versioning_path

```