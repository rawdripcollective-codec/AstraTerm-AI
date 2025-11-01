# AstraTerm AI v1.2.0

**AI-Powered Terminal with Security Tools Integration**

AstraTerm is a modern, AI-enhanced terminal application that combines powerful command-line capabilities with artificial intelligence assistance, security tools, and OSINT (Open Source Intelligence) features.

## Features

### 🤖 AI Integration
- **Multiple AI Providers**: Support for Grok (xAI), OpenAI GPT-4, Claude (Anthropic), and DeepSeek
- **Code Completion**: Get intelligent code suggestions and completions
- **Natural Language Commands**: Interact with your terminal using natural language

### 🔒 Security Tools
- **Nmap Integration**: Network scanning and port discovery
- **Metasploit Support**: Penetration testing framework integration
- **Linux Distro Management**: Install and manage multiple Linux distributions via proot-distro

### 🔍 OSINT Tools
- Maltego
- Shodan
- Recon-ng
- SpiderFoot
- theHarvester
- Sherlock (username search)
- Have I Been Pwned (breach checking)
- IntelligenceX
- PimEyes
- Eye of God

### 🎨 Modern UI
- Built with Textual framework
- Split window support
- Command history
- Session saving/loading
- GitHub repository search

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/astraterm/astraterm-ai.git
cd astraterm-ai

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

# Run AstraTerm
astraterm
```

### Development Install

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Install with AI support
pip install -e ".[ai]"

# Install with OSINT tools
pip install -e ".[osint]"

# Install everything
pip install -e ".[ai,osint,dev]"
```

## Configuration

Create a `config.json` file in your home directory or project root:

```json
{
  "xai_api_key": "your-xai-api-key",
  "github_token": "your-github-token",
  "openai_api_key": "your-openai-key",
  "anthropic_api_key": "your-anthropic-key",
  "deepseek_api_key": "your-deepseek-key",
  "shodan_api_key": "your-shodan-key",
  "settings": {
    "theme": "dark",
    "default_ai_provider": "grok",
    "terminal_history_size": 1000,
    "auto_save_session": false,
    "enable_ai_suggestions": true
  }
}
```

## Usage

### Basic Commands

```bash
# Start AstraTerm
astraterm

# Show help
help

# Clear terminal
clear

# AI assistance
ai How do I list files in Python?

# GitHub search
github python terminal

# Exit
exit
```

### Keyboard Shortcuts

- `Ctrl+W` - Split window
- `Ctrl+G` - GitHub search popup
- `Ctrl+Space` - Toggle AI assistant
- `Ctrl+L` - Clear terminal
- `Ctrl+Q` - Quit application

### AI Commands

```bash
# Get code completion
ai Complete this Python function: def factorial(n):

# Ask for help
ai How do I scan a network with nmap?

# Code explanation
ai Explain this bash command: find . -name "*.py" -exec grep -l "import os" {} \;
```

### Security Tools

```bash
# Nmap scanning
nmap -sV 192.168.1.1

# Install Kali Linux
proot-distro install kali

# Start Metasploit
msfconsole
```

### OSINT Operations

```bash
# Search for username across social media
sherlock username

# Check email breach
haveibeenpwned email@example.com

# Domain enumeration
theharvester -d example.com -b all
```

## Project Structure

```
astraterm-ai/
├── astraterm/
│   ├── __init__.py
│   ├── main.py              # Main application
│   ├── config.py            # Configuration management
│   ├── terminal.py          # Terminal session handler
│   ├── ai_assistant.py      # AI integration
│   ├── github.py            # GitHub integration
│   ├── linux.py             # Linux distro management
│   ├── metasploit.py        # Metasploit integration
│   ├── nmap.py              # Nmap scanner
│   ├── osint.py             # OSINT tools
│   ├── plugins.py           # Plugin system
│   └── resources.py         # Resource management
├── tests/                   # Test files
├── scripts/                 # Utility scripts
├── config.json              # Configuration file
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
├── README.md                # This file
└── LICENSE                  # License file
```

## API Keys

To use AI features, you'll need API keys from:

- **xAI (Grok)**: https://x.ai/api
- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic (Claude)**: https://console.anthropic.com/
- **DeepSeek**: https://platform.deepseek.com/
- **GitHub**: https://github.com/settings/tokens
- **Shodan**: https://account.shodan.io/

## Security Notice

⚠️ **Important**: 
- Never commit your `config.json` with API keys to version control
- Use environment variables for sensitive data in production
- Some security tools require root/sudo privileges
- Always obtain proper authorization before scanning networks

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Textual](https://textual.textualize.io/)
- Powered by multiple AI providers
- Integrates various open-source security and OSINT tools

## Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/astraterm/astraterm-ai/issues
- Documentation: https://astraterm.dev/docs

## Roadmap

- [ ] Multi-pane terminal support
- [ ] Custom plugin system
- [ ] Cloud sync for sessions
- [ ] Mobile companion app
- [ ] Advanced AI code generation
- [ ] Integrated vulnerability scanner
- [ ] Custom themes and styling
- [ ] Collaborative terminal sessions

---

**Made with ❤️ by the AstraTerm Team**
