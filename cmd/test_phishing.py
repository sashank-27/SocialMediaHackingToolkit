#!/usr/bin/env python3
"""
Test script for the phishing tool contribution
Verifies functionality and integration with existing toolkit
"""

import os
import sys
import time
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def test_imports():
    """Test if all required modules can be imported"""
    console.print("[blue]Testing imports...[/blue]")
    
    try:
        import requests
        console.print("[green]✓[/green] requests imported successfully")
    except ImportError:
        console.print("[red]✗[/red] requests import failed")
        return False
    
    try:
        import flask
        console.print("[green]✓[/green] flask imported successfully")
    except ImportError:
        console.print("[red]✗[/red] flask import failed")
        return False
    
    try:
        import qrcode
        console.print("[green]✓[/green] qrcode imported successfully")
    except ImportError:
        console.print("[red]✗[/red] qrcode import failed")
        return False
    
    try:
        from PIL import Image
        console.print("[green]✓[/green] PIL imported successfully")
    except ImportError:
        console.print("[red]✗[/red] PIL import failed")
        return False
    
    try:
        from phishing_tool import PhishingTool, run_phishing_attack
        console.print("[green]✓[/green] phishing_tool imported successfully")
    except ImportError as e:
        console.print(f"[red]✗[/red] phishing_tool import failed: {e}")
        return False
    
    return True

def test_phishing_tool_creation():
    """Test if PhishingTool can be instantiated"""
    console.print("\n[blue]Testing PhishingTool creation...[/blue]")
    
    try:
        from phishing_tool import PhishingTool
        phisher = PhishingTool()
        console.print("[green]✓[/green] PhishingTool created successfully")
        return True
    except Exception as e:
        console.print(f"[red]✗[/red] PhishingTool creation failed: {e}")
        return False

def test_templates():
    """Test if all templates are available"""
    console.print("\n[blue]Testing templates...[/blue]")
    
    try:
        from phishing_tool import PhishingTool
        phisher = PhishingTool()
        
        platforms = ['instagram', 'facebook', 'twitter', 'gmail']
        for platform in platforms:
            if platform in phisher.templates:
                console.print(f"[green]✓[/green] {platform} template available")
            else:
                console.print(f"[red]✗[/red] {platform} template missing")
                return False
        
        return True
    except Exception as e:
        console.print(f"[red]✗[/red] Template test failed: {e}")
        return False

def test_utils_integration():
    """Test if utils.py integration works"""
    console.print("\n[blue]Testing utils.py integration...[/blue]")
    
    try:
        # Import utils to check if phishing functions are available
        import utils
        
        # Check if phishing functions exist
        if hasattr(utils, 'insta_phishing'):
            console.print("[green]✓[/green] insta_phishing function available")
        else:
            console.print("[red]✗[/red] insta_phishing function missing")
            return False
        
        if hasattr(utils, 'facebook_phishing'):
            console.print("[green]✓[/green] facebook_phishing function available")
        else:
            console.print("[red]✗[/red] facebook_phishing function missing")
            return False
        
        if hasattr(utils, 'twitter_phishing'):
            console.print("[green]✓[/green] twitter_phishing function available")
        else:
            console.print("[red]✗[/red] twitter_phishing function missing")
            return False
        
        if hasattr(utils, 'gmail_phishing'):
            console.print("[green]✓[/green] gmail_phishing function available")
        else:
            console.print("[red]✗[/red] gmail_phishing function missing")
            return False
        
        return True
    except Exception as e:
        console.print(f"[red]✗[/red] Utils integration test failed: {e}")
        return False

def test_requirements():
    """Test if requirements.txt is properly updated"""
    console.print("\n[blue]Testing requirements.txt...[/blue]")
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        required_packages = ['flask', 'qrcode', 'pillow']
        missing_packages = []
        
        for package in required_packages:
            if package in content:
                console.print(f"[green]✓[/green] {package} in requirements.txt")
            else:
                console.print(f"[red]✗[/red] {package} missing from requirements.txt")
                missing_packages.append(package)
        
        if missing_packages:
            return False
        
        return True
    except Exception as e:
        console.print(f"[red]✗[/red] Requirements test failed: {e}")
        return False

def test_file_structure():
    """Test if all required files exist"""
    console.print("\n[blue]Testing file structure...[/blue]")
    
    required_files = [
        'phishing_tool.py',
        'utils.py',
        'requirements.txt',
        'main.py'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            console.print(f"[green]✓[/green] {file} exists")
        else:
            console.print(f"[red]✗[/red] {file} missing")
            return False
    
    return True

def run_comprehensive_test():
    """Run all tests"""
    console.print(Panel.fit(
        "[bold blue]Phishing Tool Test Suite[/bold blue]\n"
        "Testing the phishing tool contribution",
        title="Social Media Hacking Toolkit"
    ))
    
    tests = [
        ("File Structure", test_file_structure),
        ("Requirements", test_requirements),
        ("Imports", test_imports),
        ("PhishingTool Creation", test_phishing_tool_creation),
        ("Templates", test_templates),
        ("Utils Integration", test_utils_integration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            console.print(f"[red]✗[/red] {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Display results
    console.print("\n[bold blue]Test Results:[/bold blue]")
    
    table = Table(title="Test Results")
    table.add_column("Test", style="cyan")
    table.add_column("Status", style="green")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        if result:
            table.add_row(test_name, "PASS")
            passed += 1
        else:
            table.add_row(test_name, "FAIL")
    
    console.print(table)
    
    # Summary
    console.print(f"\n[bold]Summary:[/bold] {passed}/{total} tests passed")
    
    if passed == total:
        console.print("[green]✓[/green] All tests passed! Phishing tool is ready to use.")
        return True
    else:
        console.print("[red]✗[/red] Some tests failed. Please check the issues above.")
        return False

def test_quick_phishing():
    """Quick test of phishing functionality (without starting server)"""
    console.print("\n[blue]Testing phishing functionality...[/blue]")
    
    try:
        from phishing_tool import PhishingTool
        
        # Create phishing tool
        phisher = PhishingTool()
        
        # Test credential storage
        test_credential = {
            'platform': 'instagram',
            'username': 'test@example.com',
            'password': 'testpassword',
            'timestamp': datetime.now().isoformat(),
            'ip': '127.0.0.1'
        }
        
        phisher.credentials.append(test_credential)
        
        if len(phisher.credentials) == 1:
            console.print("[green]✓[/green] Credential storage working")
        else:
            console.print("[red]✗[/red] Credential storage failed")
            return False
        
        # Test credential retrieval
        creds = phisher.get_credentials()
        if len(creds) == 1 and creds[0]['username'] == 'test@example.com':
            console.print("[green]✓[/green] Credential retrieval working")
        else:
            console.print("[red]✗[/red] Credential retrieval failed")
            return False
        
        # Test credential clearing
        phisher.clear_credentials()
        if len(phisher.get_credentials()) == 0:
            console.print("[green]✓[/green] Credential clearing working")
        else:
            console.print("[red]✗[/red] Credential clearing failed")
            return False
        
        return True
        
    except Exception as e:
        console.print(f"[red]✗[/red] Phishing functionality test failed: {e}")
        return False

if __name__ == "__main__":
    # Run comprehensive test
    success = run_comprehensive_test()
    
    if success:
        # Run quick phishing test
        test_quick_phishing()
        
        console.print("\n[bold green]🎉 Phishing tool contribution is ready![/bold green]")
        console.print("\n[bold]Next steps:[/bold]")
        console.print("1. Install dependencies: pip install -r requirements.txt")
        console.print("2. Run the toolkit: python main.py")
        console.print("3. Select platform and choose phishing option")
        console.print("4. Access the phishing page at http://localhost:8080")
    else:
        console.print("\n[bold red]❌ Some tests failed. Please fix the issues before contributing.[/bold red]") 