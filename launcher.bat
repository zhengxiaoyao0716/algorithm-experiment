@echo off

set name=%1
if not "%name%"=="" goto LAUNCH

:CHOOSE
set /p num=��ѡ����ţ�1��2��3��4����
for %%i in (1 2 3 4) do (
    if %num% EQU %%i (
        set name=question%num%.py
        goto LAUNCH
    )
)
echo ��Ч�����룬������ѡ��
goto CHOOSE

:LAUNCH
python35_with_matplotlib\python.exe %name% %2 %3 %4 %5 %6 %7 %8 %9
