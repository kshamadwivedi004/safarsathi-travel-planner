@echo off
echo ======================================
echo   PUSH TO GITHUB - FINAL STEP
echo ======================================
echo.
echo Your code is committed and ready to push!
echo.
echo Repository: https://github.com/kshamadwivedi004/safarsathi-travel-planner
echo.
echo.
echo IMPORTANT: When git asks for credentials:
echo.
echo Username: kshamadwivedi004
echo.
echo Password: USE PERSONAL ACCESS TOKEN!
echo          NOT your GitHub password!
echo.
echo Get token NOW from:
echo https://github.com/settings/tokens/new
echo.
echo Steps:
echo 1. Click "Generate new token (classic)"
echo 2. Note: Type "SafarSathi"
echo 3. Check ONLY the "repo" box
echo 4. Click "Generate token" at bottom
echo 5. COPY the token (starts with ghp_)
echo 6. Come back here and continue
echo.
pause
echo.
echo Pushing to GitHub now...
echo.

cd /d "%~dp0"

git push -u origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo   PUSH FAILED!
    echo ========================================
    echo.
    echo Possible issues:
    echo.
    echo 1. WRONG PASSWORD?
    echo    - Don't use GitHub password
    echo    - Use Personal Access Token
    echo    - Get it from: https://github.com/settings/tokens/new
    echo.
    echo 2. REPOSITORY NOT EMPTY?
    echo    - Go to your repository page
    echo    - Delete any existing files
    echo    - OR use: git push -f origin main
    echo.
    echo 3. REPOSITORY DOESN'T EXIST?
    echo    - Go to: https://github.com/new
    echo    - Name: safarsathi-travel-planner
    echo    - Make it PUBLIC
    echo    - Don't add README
    echo    - Create it, then run this again
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS! YOUR CODE IS ON GITHUB!
echo ========================================
echo.
echo View your code at:
echo https://github.com/kshamadwivedi004/safarsathi-travel-planner
echo.
echo.
echo ========================================
echo   NEXT: DEPLOY TO INTERNET
echo ========================================
echo.
echo 1. Go to: https://share.streamlit.io/
echo.
echo 2. Click "Continue with GitHub"
echo.
echo 3. Click "New app"
echo.
echo 4. Fill these details:
echo    Repository: kshamadwivedi004/safarsathi-travel-planner
echo    Branch: main
echo    Main file path: app.py
echo.
echo 5. Click "Advanced settings" -^> "Secrets"
echo.
echo 6. Add this (get key from your .env file):
echo    GROQ_API_KEY = "your_actual_key_here"
echo.
echo 7. Click "Deploy!"
echo.
echo 8. Wait 5 minutes...
echo.
echo 9. You'll get a URL like:
echo    https://safarsathi-travel-planner-xxxxx.streamlit.app/
echo.
echo THAT'S YOUR LIVE APP! Share it with anyone!
echo.
echo.
pause
