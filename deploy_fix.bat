@echo off
echo ========================================
echo  SafarSathi Deployment Fix
echo ========================================
echo.

cd /d "%~dp0"

echo [1/7] Checking current status...
echo.

REM Check if .git exists
if not exist ".git" (
    echo Git repository not initialized. Initializing now...
    git init
    echo Git initialized!
) else (
    echo Git repository already exists.
)

echo.
echo [2/7] Checking Git configuration...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo.
    echo Git user not configured. Let's set it up:
    set /p git_name="Enter your name: "
    set /p git_email="Enter your email: "
    git config user.name "%git_name%"
    git config user.email "%git_email%"
    echo Git configured successfully!
) else (
    echo Git is already configured.
)

echo.
echo [3/7] Adding files to Git...
git add .
if errorlevel 1 (
    echo Error adding files!
    pause
    exit /b 1
)
echo Files added successfully!

echo.
echo [4/7] Checking for existing commits...
git log --oneline -1 >nul 2>&1
if errorlevel 1 (
    echo No commits yet. Creating first commit...
    git commit -m "Initial commit: SafarSathi AI Travel Planner"
    if errorlevel 1 (
        echo.
        echo Error creating commit!
        echo Make sure files were added properly.
        pause
        exit /b 1
    )
    echo First commit created!
) else (
    echo.
    echo Commits exist. Creating new commit with any changes...
    git commit -m "Update: SafarSathi deployment"
    if errorlevel 1 (
        echo No new changes to commit, using existing commits.
    ) else (
        echo New commit created!
    )
)

echo.
echo [5/7] Setting up remote repository...
echo.
echo Your GitHub repository should be:
echo https://github.com/kshamadwivedi004/safarsathi-travel-planner.git
echo.
set /p confirm="Is this correct? (y/n): "
if /i not "%confirm%"=="y" (
    echo.
    echo Please enter your correct GitHub repository URL:
    set /p repo_url="Repository URL: "
) else (
    set repo_url=https://github.com/kshamadwivedi004/safarsathi-travel-planner.git
)

echo.
echo Configuring remote...
REM Remove existing origin if present
git remote remove origin >nul 2>&1

REM Add new origin
git remote add origin %repo_url%
if errorlevel 1 (
    echo Error setting remote!
    pause
    exit /b 1
)
echo Remote configured successfully!

echo.
echo [6/7] Ensuring main branch exists...
REM Get current branch name
for /f "tokens=*" %%a in ('git branch --show-current') do set current_branch=%%a

if "%current_branch%"=="" (
    echo Creating main branch...
    git checkout -b main
) else (
    if not "%current_branch%"=="main" (
        echo Renaming branch to main...
        git branch -M main
    ) else (
        echo Already on main branch.
    )
)

echo.
echo [7/7] Pushing to GitHub...
echo.
echo CREDENTIALS:
echo Username: kshamadwivedi004
echo Password: Use Personal Access Token (NOT your GitHub password!)
echo.
echo Get token from: https://github.com/settings/tokens/new
echo 1. Click "Generate new token (classic)"
echo 2. Give it a name: SafarSathi
echo 3. Check ONLY "repo" scope
echo 4. Click "Generate token" at bottom
echo 5. COPY the token immediately ^(starts with ghp_^)
echo 6. Paste it when asked for password below
echo.
echo Pushing code to GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo  Push failed!
    echo ========================================
    echo.
    echo Common solutions:
    echo.
    echo 1. AUTHENTICATION FAILED?
    echo    - Make sure you're using Personal Access Token
    echo    - NOT your GitHub password
    echo    - Get token: https://github.com/settings/tokens/new
    echo.
    echo 2. REPOSITORY DOESN'T EXIST?
    echo    - Go to: https://github.com/new
    echo    - Name: safarsathi-travel-planner
    echo    - Make it PUBLIC
    echo    - DON'T initialize with README
    echo    - Create repository
    echo    - Run this script again
    echo.
    echo 3. ALREADY EXISTS?
    echo    - The repository might have content already
    echo    - Try: git push -f origin main
    echo    - Or delete and recreate the repository
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  SUCCESS! Code pushed to GitHub!
echo ========================================
echo.
echo Your code is now at:
echo https://github.com/kshamadwivedi004/safarsathi-travel-planner
echo.
echo NEXT STEPS:
echo.
echo 1. Go to: https://share.streamlit.io/
echo 2. Click "Continue with GitHub"
echo 3. Click "New app"
echo 4. Fill in:
echo    Repository: kshamadwivedi004/safarsathi-travel-planner
echo    Branch: main
echo    Main file: app.py
echo.
echo 5. Click "Advanced settings" -^> "Secrets"
echo 6. Add your GROQ API key:
echo    GROQ_API_KEY = "your_key_from_env_file"
echo.
echo 7. Click "Deploy!"
echo.
echo Your app will be live in ~5 minutes!
echo.
pause
