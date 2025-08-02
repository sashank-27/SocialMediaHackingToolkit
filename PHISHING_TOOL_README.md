# Phishing Tool Contribution

## Overview

This contribution adds a comprehensive phishing tool to the Social Media Hacking Toolkit, providing realistic phishing pages for Instagram, Facebook, Twitter, and Gmail. The tool is designed for educational purposes and penetration testing.

## Features

### 🎯 Multi-Platform Support
- **Instagram**: Realistic Instagram login page with proper styling
- **Facebook**: Authentic Facebook login interface
- **Twitter/X**: Modern Twitter/X login design
- **Gmail**: Google Gmail login page

### 🔧 Advanced Features
- **QR Code Generation**: Easy mobile access via QR codes
- **Real-time Monitoring**: Live credential capture and display
- **Automatic Saving**: Results saved to JSON files with timestamps
- **IP Tracking**: Captures victim IP addresses
- **Success Pages**: Realistic success/redirect pages
- **Responsive Design**: Works on desktop and mobile devices

### 🛡️ Security Features
- **Educational Focus**: Clear warnings about educational use only
- **Responsible Disclosure**: Built-in ethical guidelines
- **Logging**: Comprehensive activity logging
- **Error Handling**: Robust error handling and recovery

## Installation

### Prerequisites
```bash
# Install Python dependencies
pip install -r requirements.txt

# Additional dependencies for phishing tool
pip install flask qrcode pillow
```

### File Structure
```
cmd/
├── phishing_tool.py          # Main phishing tool module
├── utils.py                  # Updated with phishing integration
├── requirements.txt          # Updated dependencies
└── main.py                  # Main application entry point
```

## Usage

### Running the Phishing Tool

1. **Start the toolkit**:
   ```bash
   cd cmd
   python main.py
   ```

2. **Select platform**:
   - Choose platform (1-4)
   - Select phishing option (3)

3. **Access the phishing page**:
   - URL: `http://localhost:8080`
   - QR Code: `http://localhost:8080/qr`

### Command Line Usage

```bash
# Direct phishing tool usage
python phishing_tool.py

# Platform-specific attacks
python -c "from phishing_tool import run_phishing_attack; run_phishing_attack('instagram')"
python -c "from phishing_tool import run_phishing_attack; run_phishing_attack('facebook')"
python -c "from phishing_tool import run_phishing_attack; run_phishing_attack('twitter')"
python -c "from phishing_tool import run_phishing_attack; run_phishing_attack('gmail')"
```

## Technical Details

### Architecture

The phishing tool uses a Flask-based web server with the following components:

- **PhishingTool Class**: Main orchestrator
- **Template System**: HTML templates for each platform
- **Credential Handler**: Secure credential storage
- **QR Generator**: Dynamic QR code generation
- **Server Management**: Threaded server with graceful shutdown

### Key Components

#### 1. Template System
```python
def get_instagram_template(self):
    # Returns realistic Instagram login HTML
```

#### 2. Credential Capture
```python
def handle_login(self):
    # Captures and stores credentials securely
```

#### 3. QR Code Generation
```python
def generate_qr_code(self):
    # Creates QR codes for easy mobile access
```

#### 4. Real-time Monitoring
```python
def run_phishing_attack(platform):
    # Main attack orchestration with live updates
```

### Security Considerations

1. **Educational Use Only**: Clear warnings and disclaimers
2. **Local Testing**: Designed for local network testing
3. **No Data Persistence**: Credentials stored in memory only
4. **Ethical Guidelines**: Built-in responsible disclosure

## Configuration

### Port Configuration
```python
# Default port (configurable)
self.port = 8080
```

### Template Customization
```python
# Add custom templates
self.templates = {
    'instagram': self.get_instagram_template(),
    'facebook': self.get_facebook_template(),
    'twitter': self.get_twitter_template(),
    'gmail': self.get_gmail_template(),
    'custom': self.get_custom_template()  # Add your own
}
```

## Output Format

### Credential Storage
```json
{
  "platform": "instagram",
  "username": "victim@example.com",
  "password": "captured_password",
  "timestamp": "2024-01-15T10:30:45.123456",
  "ip": "192.168.1.100"
}
```

### Results File
```
phishing_results_instagram_20240115_103045.json
```

## Integration with Existing Toolkit

### Updated Functions
- `insta_phishing()`: Instagram phishing integration
- `facebook_phishing()`: Facebook phishing integration
- `twitter_phishing()`: Twitter phishing integration
- `gmail_phishing()`: Gmail phishing integration

### Error Handling
```python
try:
    from phishing_tool import run_phishing_attack
    run_phishing_attack('instagram')
except ImportError as e:
    console.print(f"[red]Error importing phishing tool: {e}[/red]")
    console.print("[yellow]Please install required dependencies[/yellow]")
```

## Ethical Guidelines

### ⚠️ Important Disclaimers

1. **Educational Purpose Only**: This tool is for educational and penetration testing purposes
2. **Authorized Testing Only**: Only use on systems you own or have explicit permission to test
3. **Legal Compliance**: Ensure compliance with local laws and regulations
4. **Responsible Disclosure**: Report vulnerabilities through proper channels
5. **No Malicious Use**: Do not use for unauthorized access or data theft

### Best Practices

1. **Testing Environment**: Use only in controlled testing environments
2. **Documentation**: Keep detailed logs of all testing activities
3. **Consent**: Obtain proper consent before testing
4. **Reporting**: Report findings through responsible disclosure programs

## Troubleshooting

### Common Issues

1. **Import Errors**:
   ```bash
   pip install flask qrcode pillow
   ```

2. **Port Conflicts**:
   ```python
   # Change port in phishing_tool.py
   self.port = 8081  # or any available port
   ```

3. **QR Code Issues**:
   ```bash
   pip install pillow
   ```

4. **Server Not Starting**:
   - Check if port 8080 is available
   - Ensure firewall allows local connections
   - Verify all dependencies are installed

### Debug Mode
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

### Adding New Platforms

1. **Create Template**:
   ```python
   def get_newplatform_template(self):
       return """
       <!DOCTYPE html>
       <!-- Your HTML template here -->
       """
   ```

2. **Add to Templates**:
   ```python
   self.templates['newplatform'] = self.get_newplatform_template()
   ```

3. **Update Integration**:
   ```python
   def newplatform_phishing():
       # Add to utils.py
   ```

### Code Style

- Follow PEP 8 guidelines
- Add comprehensive docstrings
- Include error handling
- Write unit tests for new features

## License

This contribution follows the same license as the main Social Media Hacking Toolkit project.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Create an issue in the repository
4. Ensure you're using the latest version

## Changelog

### Version 1.0.0
- Initial phishing tool implementation
- Support for Instagram, Facebook, Twitter, Gmail
- QR code generation
- Real-time credential monitoring
- Automatic result saving
- Integration with existing toolkit

---

**Remember**: This tool is for educational purposes only. Always use responsibly and ethically. 