@echo off
setlocal enabledelayedexpansion
set /P searchterms="What do you want to search for? | "
REM echo %searchterms%
set searchterms2 = !searchterms: =%%20!
REM echo %searchterms: =+%
set /P file="What file to output? | "
scrapy runspider "ShopForMe.py" -a searchTerms="%searchTerms: =+%" -a log=False -o"%file%" --nolog
Line_DeDuper.exe %file%
Html_Tag_Remover %file%
pause