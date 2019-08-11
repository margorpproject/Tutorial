### 1. Modify termsrv.dll to enable rdp connection

source: https://www.mysysadmintips.com/windows/clients/545-multiple-rdp-remote-desktop-sessions-in-windows-10

locate C:\Windows\System32\termsrv.dll and open it with a hex editor. (eg. Tiny Hexer, Ultra Edit)

find
> 39 81 3C 06 00 00 0F 84 5D 61 01 00

replace by
> B8 00 01 00 00 89 81 38 06 00 00 90

if your Windows 10 is in older version, try the following edition:
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 x64 v1809
Find:
> 39 81 3C 06 00 00 0F 84 3B 2B 01 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Find:
> 39 81 3C 06 00 00 0F 84 7F 2C 01 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 x64 v1803 - Spring 2018 Update (March 2018)
Windows 10 Spring 2018 Update (1803) updates termsrv.dll to version 10.0.17134.1. 
Find:
> 8B 99 3C 06 00 00 8B B9 38 06 00 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 Fall Creators Update (1709 -  Redstone 3) 
Updates termsrv.dll to version 10.0.16299.15. 
Find:
> 39 81 3C 06 00 00 0F 84 B1 7D 02 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 x64 v1703 - Creators Update (April 2017)
Windows 10 Creators Update (1703 -  Redstone 2) updates termsrv.dll to version 10.0.15063.0. 
Find:
> 39 81 3C 06 00 00 0F 84 53 71 02 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 x64 Threshold 2 (November 2015)
Windows 10 Fall Update (also called "Threshold Wave 2 Update") updates termsrv.dll to version 10.0.10586.0. 
Find:
> 39 81 3C 06 00 00 0F 84 3F 42 02 00
replace with:
> B8 00 01 00 00 89 81 38 06 00 00 90
-----------------------------------------------------------------------------------------------------------------------------
Windows 10 x64 RTM (August 2015)
termsrv.dll file version 10.0.10240.16384.
In termsrv.dll find:
> 39 81 3C 06 00 00 0F 84 73 42 02 00
and replace it with:
> B8 00 01 00 00 89 81 38 06 00 00 90

