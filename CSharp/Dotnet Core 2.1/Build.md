### 1. Introduction
.net core 2.1 app can be run on multiple platforms such as Linux and PC.

### 2. Create
To write a .net core app, open Visual Basic and choose .net core 2.1 application.

### 3. Build
To build the application, go to menu -> build -> build project

### 4. Run
To run the application, go to the build folder and see if your <project-name>.dll is found. Open console or terminal, type:
> dotnet \<project-name\>.dll

### 5. Install .Net SDK in Linux(Ubuntu)
> wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb

> sudo dpkg -i packages-microsoft-prod.deb

> sudo apt-get install apt-transport-https

> sudo apt-get update

> sudo apt-get install dotnet-sdk-2.1
