@echo off

set name=%1
if not "%name%"=="" goto LAUNCH

:CHOOSE
set /p num=请选择题号（1、2、3、4）：
for %%i in (1 2 3 4) do (
    if %num% EQU %%i (
        set name=question%num%.py
        goto LAUNCH
    )
)
echo 无效的输入，请重新选择
goto CHOOSE

:LAUNCH
python35_with_matplotlib\python.exe %name% %2 %3 %4 %5 %6 %7 %8 %9
