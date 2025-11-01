# AstraTerm AI - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Verify Installation

```bash
# Navigate to project directory
cd /path/to/astraterm-ai

# Run verification script
python3 verify_project.py
```

### Step 2: Install Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt

# Or install with pip (if available)
pip install textual rich requests python-nmap
```

### Step 3: Configure API Keys (Optional)

Edit `config.json` and add your API keys:

```json
{
  "xai_api_key": "your-xai-key",
  "github_token": "your-github-token",
  "openai_api_key": "your-openai-key"
}
```

**Note**: API keys are optional. You can use AstraTerm without them, but AI features will be limited.

### Step 4: Run AstraTerm

**Option A: Direct Run (No Installation)**
```bash
python3 run.py
```

**Option B: Install and Run**
```bash
pip install -e .
astraterm
```

## 📖 Basic Usage

### Terminal Commands

```bash
# Show help
help

# Clear screen
clear

# Run any shell command
ls -la
pwd
echo "Hello AstraTerm"

# Exit
exit
```

### AI Features

```bash
# Ask AI for help
ai How do I create a Python virtual environment?

# Code completion
ai Complete this function: def fibonacci(n):

# Explain commands
ai What does this command do: grep -r "pattern" .
```

### GitHub Integration

```bash
# Search repositories
github python terminal

# Search by topic
github machine-learning
```

### Security Tools

```bash
# Network scanning (requires nmap)
nmap -sV 192.168.1.1

# Quick port scan
nmap -F localhost
```

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Q` | Quit application |
| `Ctrl+L` | Clear terminal |
| `Ctrl+W` | Split window (coming soon) |
| `Ctrl+G` | GitHub search popup |
| `Ctrl+Space` | AI assistant overlay |

## 🎯 Common Tasks

### 1. Code Assistance

```bash
# Get Python help
ai How do I read a file in Python?

# JavaScript help
ai Show me async/await example in JavaScript

# Bash scripting
ai Create a bash script to backup files
```

### 2. Network Scanning

```bash
# Scan local network
nmap -sn 192.168.1.0/24

# Scan specific host
nmap -A 192.168.1.1

# Quick scan
nmap -F scanme.nmap.org
```

### 3. OSINT Operations

```bash
# Search username (requires sherlock)
sherlock username123

# Check email breach (requires internet)
haveibeenpwned email@example.com
```

### 4. Session Management

```bash
# Commands are automatically saved to history
# Use up/down arrows to navigate history

# Save session (feature in terminal module)
# Load session (feature in terminal module)
```

## 🔧 Troubleshooting

### Issue: Dependencies not installed

```bash
# Install manually
pip install textual rich requests python-nmap
```

### Issue: AI features not working

- Check your API keys in `config.json`
- Verify internet connection
- Try different AI provider

### Issue: Permission denied for security tools

```bash
# Some tools require sudo
sudo nmap -sS 192.168.1.1
```

## 📚 Learn More

- **Full Documentation**: [README.md](README.md)
- **Installation Guide**: [INSTALL.md](INSTALL.md)
- **API Reference**: Check individual module files in `astraterm/`

## 🎓 Example Workflows

### Workflow 1: Web Development

```bash
# Start AstraTerm
astraterm

# Ask AI for help
ai How do I create a REST API in Python?

# Search for examples
github python flask rest api

# Run development server
python app.py
```

### Workflow 2: Security Testing

```bash
# Start AstraTerm
astraterm

# Scan network
nmap -sV 192.168.1.0/24

# Get AI advice
ai What are common web vulnerabilities?

# Search security tools
github penetration testing tools
```

### Workflow 3: Learning & Research

```bash
# Start AstraTerm
astraterm

# Learn new language
ai Teach me Python basics

# Get cheat sheet
ai Python cheat sheet

# Search tutorials
github python tutorial
```

## 🌟 Pro Tips

1. **Use Tab Completion**: Press Tab to autocomplete commands (if supported by your shell)

2. **Command History**: Use Up/Down arrows to navigate through previous commands

3. **Multiple AI Providers**: Configure multiple AI providers and switch between them

4. **Customize Config**: Edit `config.json` to customize behavior

5. **Save Sessions**: Use the session save feature to preserve your work

## 🆘 Getting Help

- Type `help` in AstraTerm for built-in help
- Check [README.md](README.md) for detailed documentation
- Visit GitHub Issues for community support
- Read module docstrings for API details

## 🎉 You're Ready!

Start exploring AstraTerm AI and boost your productivity!

```bash
python3 run.py
```

---

**Happy Coding! 💻**
