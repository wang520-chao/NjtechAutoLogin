@echo off
::设置程序或文件的完整路径
set Program=%cd%\bin\NjtechAutologin.exe

::设置快捷方式名称
set LnkName=南工认证

::设置程序的工作路径，一般为程序主目录，此项若留空，脚本将自行分析路径
set WorkDir=

::设置快捷方式显示的说明
set Desc=南工大 上网认证 自动登录 @Herk

if not defined WorkDir call:GetWorkDir "%Program%"
(echo Set WshShell=CreateObject("WScript.Shell"^)
echo strDesKtop=WshShell.SPEcialFolders("DesKtop"^)
echo Set oShellLink=WshShell.CreateShortcut(strDesKtop^&"\%LnkName%.lnk"^)
echo oShellLink.TargetPath="%Program%"
echo oShellLink.WorkingDirectory="%WorkDir%"
echo oShellLink.Windowstyle=1
echo oShellLink.Description="%Desc%"
echo oShellLink.Save)>makelnk.vbs
echo 桌面快捷方式创建成功！
makelnk.vbs
del /f /q makelnk.vbs
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof
