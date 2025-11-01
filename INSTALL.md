# Installation Guide for AstraTerm AI

## System Requirements

- **Operating System**: Linux, macOS, or Windows (with WSL)
- **Python**: 3.8 or higher
- **RAM**: Minimum 512MB, Recommended 2GB+
- **Disk Space**: 100MB for base installation

## Installation Methods

### Method 1: Quick Install (Recommended)

```bash
# Install from source
git clone https://github.com/astraterm/astraterm-ai.git
cd astraterm-ai
pip install -r requirements.txt
pip install -e .

# Run the application
astraterm
```

### Method 2: Using pip (when published)

```bash
# Install from PyPI
pip install astraterm-ai

# Run the application
astraterm
```

### Method 3: Development Installation

```bash
# Clone repository
git clone https://github.com/astraterm/astraterm-ai.git
cd astraterm-ai

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all extras
pip install -e ".[ai,osint,dev]"

# Run tests
pytest

# Run the application
astraterm
```

## Post-Installation Setup

### 1. Configuration File

Create a configuration file at `~/.astraterm/config.json`:

```bash
mkdir -p ~/.astraterm
cp config.json ~/.astraterm/config.json
```

Edit the file and add your API keys:

```json
{
  "xai_api_key": "your-xai-api-key-here",
  "github_token": "your-github-token-here",
  "openai_api_key": "your-openai-key-here",
  "anthropic_api_key": "your-anthropic-key-here",
  "deepseek_api_key": "your-deepseek-key-here"
}
```

### 2. Optional Dependencies

#### Security Tools

```bash
# Nmap (network scanner)
sudo apt install nmap  # Debian/Ubuntu
brew install nmap      # macOS

# Metasploit Framework
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall
```

#### OSINT Tools

```bash
# Sherlock (username search)
pip install sherlock-project

# theHarvester (email/subdomain enumeration)
pip install theharvester

# Shodan CLI
pip install shodan
shodan init YOUR_API_KEY
```

#### Linux Distributions (via proot-distro)

```bash
# Install proot-distro (Termux/Android)
pkg install proot-distro

# Install a distribution
proot-distro install kali
proot-distro install ubuntu
```

### 3. Verify Installation

```bash
# Check version
astraterm --version

# Run help
astraterm --help

# Test import
python3 -c "import astraterm; print(astraterm.__version__)"
```

## Troubleshooting

### Issue: "Command not found: astraterm"

**Solution**: Make sure the installation directory is in your PATH:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Reload shell
source ~/.bashrc
```

### Issue: "ModuleNotFoundError: No module named 'textual'"

**Solution**: Install dependencies:

```bash
pip install -r requirements.txt
```

### Issue: "Permission denied" when installing

**Solution**: Use user installation:

```bash
pip install --user -e .
```

### Issue: AI features not working

**Solution**: 
1. Check your API keys in `config.json`
2. Verify internet connection
3. Check API provider status

### Issue: Security tools not found

**Solution**: Install system packages:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nmap metasploit-framework

# macOS
brew install nmap
```

## Uninstallation

```bash
# Uninstall the package
pip uninstall astraterm-ai

# Remove configuration
rm -rf ~/.astraterm

# Remove cache
rm -rf ~/.cache/astraterm
```

## Getting Help

- **Documentation**: https://astraterm.dev/docs
- **GitHub Issues**: https://github.com/astraterm/astraterm-ai/issues
- **Community**: https://discord.gg/astraterm

## Next Steps

After installation:

1. Configure your API keys in `config.json`
2. Read the [User Guide](USER_GUIDE.md)
3. Try the [Quick Start Tutorial](QUICKSTART.md)
4. Explore [Examples](examples/)

---

**Happy Hacking! 🚀**
