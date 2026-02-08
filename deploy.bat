@echo off
echo ========================================
echo SafarSathi - Deployment Script
echo ========================================
echo.

echo Checking git status...
git status
echo.

echo Adding all changes...
git add .
echo.

echo Committing changes...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Update SafarSathi - Ready for deployment

git commit -m "%commit_msg%"
echo.

echo Pushing to GitHub...
git push origin main --force
echo.

echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Go to https://share.streamlit.io/
echo 2. Create new app or update existing one
echo 3. Select repository: kshamadwivedi004/safarsathi-travel-planner
echo 4. Set Main file: app.py
echo 5. Add GROQ_API_KEY in Secrets
echo.
echo Your app will be live in 2-5 minutes!
echo ========================================
pause
