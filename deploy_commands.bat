@echo off
echo ========================================
echo  SafarSathi Deployment Script
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/downloads
    echo.
    pause
    exit /b 1
)

echo [1/6] Checking Git configuration...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo.
    echo Git user not configured. Let's set it up:
    set /p git_name="Enter your name: "
    set /p git_email="Enter your email: "
    git config user.name "%git_name%"
    git config user.email "%git_email%"
    echo Git configured successfully!
)

echo.
echo [2/6] Initialize Git repository...
if not exist ".git" (
    git init
    echo Git repository initialized!
) else (
    echo Git repository already exists.
)

echo.
echo [3/6] Adding files to Git...
git add .
echo Files added!

echo.
echo [4/6] Committing changes...
git commit -m "Deploy SafarSathi AI Travel Planner to Streamlit Cloud"
if errorlevel 1 (
    echo No changes to commit or already committed.
)

echo.
echo [5/6] Setting up remote repository...
echo.
echo Please enter your GitHub repository URL
echo Example: https://github.com/YOUR_USERNAME/safarsathi-travel-planner.git
echo.
set /p repo_url="Repository URL: "

REM Remove existing origin if present
git remote remove origin >nul 2>&1

REM Add new origin
git remote add origin %repo_url%

echo.
echo [6/6] Pushing to GitHub...
echo.
echo If prompted for credentials:
echo   Username: Your GitHub username
echo   Password: Use Personal Access Token (not your password!)
echo   Get token from: https://github.com/settings/tokens/new
echo.
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo  Push failed! Common issues:
    echo ========================================
    echo 1. Authentication failed - Use Personal Access Token
    echo 2. Repository doesn't exist - Create it on GitHub first
    echo 3. Network issues - Check internet connection
    echo.
    echo Visit DEPLOY_NOW.md for detailed troubleshooting!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  SUCCESS! Code pushed to GitHub!
echo ========================================
echo.
echo Next steps:
echo 1. Go to: https://share.streamlit.io/
echo 2. Click "New app"
echo 3. Select your repository
echo 4. Set main file: app.py
echo 5. Add secret: GROQ_API_KEY
echo 6. Deploy!
echo.
echo Your app will be live in ~5 minutes!
echo.
echo See DEPLOY_NOW.md for detailed instructions.
echo.
pause
