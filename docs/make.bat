@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build
set THEMENAME=sphinx_rtd_theme

REM Check if source directory exists
if not exist "%SOURCEDIR%" (
    echo Error: Source directory '%SOURCEDIR%' not found!
    exit /b 1
)

REM Check for theme
pip show %THEMENAME% >NUL 2>NUL
if errorlevel 1 (
    echo Warning: %THEMENAME% not found. Attempting to install...
    pip install %THEMENAME%
    if errorlevel 1 (
        echo Error: Failed to install %THEMENAME%. Please install manually.
        echo pip install %THEMENAME%
        exit /b 1
    )
)

if "%1" == "" goto help
if "%1" == "clean" (
    echo Cleaning build directory...
    rmdir /s /q %BUILDDIR%
    echo Clean complete!
    exit /b 0
)

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
    echo Error: The 'sphinx-build' command was not found.
    echo Please install Sphinx: pip install sphinx
    exit /b 1
)

echo Building documentation for target '%1'...
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
if errorlevel 0 (
    echo Build successful!
) else (
    echo Build failed!
)
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
