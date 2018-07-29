@echo off
setlocal enabledelayedexpansion

set /P searchterms="What do you want to search for? | "
set /P file="What file to output? | "
echo Running spider...
scrapy runspider "ShopForMe.py" -a searchTerms="%searchTerms: =+%" -a log=False -o"%file%" --nolog
echo Done! Further processing output...
Line_DeDuper.exe %file%
Html_Tag_Remover %file%
echo Done!
pause