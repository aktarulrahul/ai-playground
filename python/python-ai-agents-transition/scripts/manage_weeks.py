#!/usr/bin/env python3
"""
Week Management Script for Python FastAPI Monorepo
Manages all 6 weeks of FastAPI backends
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

WEEKS = [1, 2, 3, 4, 5, 6]
PORTS = {1: 8001, 2: 8002, 3: 8003, 4: 8004, 5: 8005, 6: 8006}

def run_command(command, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def install_week(week):
    """Install dependencies for a specific week"""
    week_dir = f"week-{week}"
    if not os.path.exists(week_dir):
        print(f"❌ Week {week} directory does not exist")
        return False
    
    print(f"📦 Installing dependencies for week {week}...")
    result = run_command("pip install -r requirements.txt", cwd=week_dir)
    if result:
        print(f"✅ Week {week} dependencies installed successfully")
        return True
    else:
        print(f"❌ Failed to install dependencies for week {week}")
        return False

def setup_env(week):
    """Set up environment for a specific week"""
    week_dir = f"week-{week}"
    env_example = os.path.join(week_dir, "env.example")
    env_file = os.path.join(week_dir, ".env")
    
    if not os.path.exists(env_example):
        print(f"⚠️  No env.example found for week {week}")
        return False
    
    if os.path.exists(env_file):
        print(f"⚠️  .env already exists for week {week}")
        return False
    
    print(f"🔧 Setting up environment for week {week}...")
    result = run_command(f"cp env.example .env", cwd=week_dir)
    if result:
        print(f"✅ Environment setup for week {week}")
        return True
    else:
        print(f"❌ Failed to setup environment for week {week}")
        return False

def run_week(week, port=None):
    """Run a specific week"""
    if port is None:
        port = PORTS.get(week, 8000 + week)
    
    week_dir = f"week-{week}"
    if not os.path.exists(week_dir):
        print(f"❌ Week {week} directory does not exist")
        return False
    
    print(f"🚀 Starting week {week} on port {port}...")
    command = f"uvicorn main:app --reload --host 0.0.0.0 --port {port}"
    try:
        subprocess.run(command, shell=True, cwd=week_dir)
    except KeyboardInterrupt:
        print(f"\n🛑 Week {week} stopped")
        return True
    return True

def test_week(week):
    """Test a specific week"""
    week_dir = f"week-{week}"
    if not os.path.exists(week_dir):
        print(f"❌ Week {week} directory does not exist")
        return False
    
    print(f"🧪 Testing week {week}...")
    result = run_command("pytest -v", cwd=week_dir)
    if result:
        print(f"✅ Week {week} tests completed")
        return True
    else:
        print(f"❌ Week {week} tests failed")
        return False

def list_weeks():
    """List all available weeks"""
    print("📋 Available weeks:")
    for week in WEEKS:
        week_dir = f"week-{week}"
        status = "✅" if os.path.exists(week_dir) else "❌"
        port = PORTS.get(week, 8000 + week)
        print(f"  {status} Week {week} (Port: {port})")

def main():
    parser = argparse.ArgumentParser(description="Manage FastAPI weeks")
    parser.add_argument("action", choices=["install", "setup", "run", "test", "list"], 
                       help="Action to perform")
    parser.add_argument("--week", type=int, choices=WEEKS, 
                       help="Specific week to work with")
    parser.add_argument("--port", type=int, 
                       help="Port to run the week on")
    parser.add_argument("--all", action="store_true", 
                       help="Perform action on all weeks")
    
    args = parser.parse_args()
    
    if args.action == "list":
        list_weeks()
        return
    
    if args.all:
        weeks = WEEKS
    elif args.week:
        weeks = [args.week]
    else:
        print("❌ Please specify --week or --all")
        return
    
    for week in weeks:
        print(f"\n{'='*50}")
        print(f"Processing Week {week}")
        print(f"{'='*50}")
        
        if args.action == "install":
            install_week(week)
        elif args.action == "setup":
            setup_env(week)
        elif args.action == "run":
            run_week(week, args.port)
        elif args.action == "test":
            test_week(week)

if __name__ == "__main__":
    main() 