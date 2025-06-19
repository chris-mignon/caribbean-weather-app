# Set your project root directory
$ProjectRoot = "caribbean-weather-app"

# Create directories
New-Item -ItemType Directory -Path "$ProjectRoot\data" -Force
New-Item -ItemType Directory -Path "$ProjectRoot\templates" -Force
New-Item -ItemType Directory -Path "$ProjectRoot\static\css" -Force
New-Item -ItemType Directory -Path "$ProjectRoot\static\js" -Force
New-Item -ItemType Directory -Path "$ProjectRoot\tests" -Force

# Create files
New-Item -ItemType File -Path "$ProjectRoot\app.py" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\requirements.txt" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\Dockerfile" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\README.md" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\data\cities.json" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\templates\index.html" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\static\css\custom.css" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\static\js\main.js" -Force | Out-Null
New-Item -ItemType File -Path "$ProjectRoot\tests\test_app.py" -Force | Out-Null

Write-Host "Project structure created under $ProjectRoot\"