# AstraTerm AI 🚀


A modded terminal app inspired by Termux and Andronix, enhanced with AI assistants, Linux distro support, OSINT tools, and security frameworks like Metasploit and Nmap. Built for developers, pentesters, and power users—cross-platform (Android, Linux, Desktop, Web).

This is the official maintained version by **rawdripcollective-codec**. Forked and expanded from conceptual blueprints.

## 🌟 Features

- **Core Terminal**: Multi-window TUI with split panes, save/edit/run/deploy, copy/paste, search bar, repo favorites, and code snippets.
- **AI Assistant**: Code hints, predictive text (via Jedi), GitHub repo search in floating pop-up. Integrations with Deepseek R1, Anthropic Claude, ChatGPT, and Grok (real-time search/reasoning).
- **Linux Distros**: Kali, Debian, Ubuntu via proot; full package management (apt).
- **Security Tools**:
  - Metasploit Framework (msfconsole, msfvenom) for ethical pentesting.
  - Nmap Scanner with Scripting Engine (NSE) for network discovery, vuln scanning, and OS detection.
  - 10 OSINT Tools: Maltego, Shodan, Recon-ng, SpiderFoot, theHarvester, Sherlock, Have I Been Pwned, Intelligence X, PimEyes, **Eye of God** (Telegram API).
- **Resources & Extensibility**: Auto-updated Python libraries, cheat sheets (bash/Python/etc.), web resource modules, multi-language support (Node.js, Rust, Go), plugin system for extensions.
- **Performance & Security**: 1s startup, sandboxed executions, consent prompts, audit logs.
- **Bonus**: Voice commands (Whisper API), themes (Dark/Light/Dracula), SSH client, Docker support, VSCode Server integration.

## 📸 Screenshots

Here are example visualizations of AstraTerm AI's interface, inspired by core components (multi-window terminal, AI popups, Linux setups). More custom screenshots coming in v1.3!

### 1. Main Terminal Dashboard (Multi-Window TUI)
![Main Terminal Dashboard](https://raw.githubusercontent.com/Textualize/textual/develop/docs/images/screenshot.gif)  
*Split panes for commands, output, and AI hints—powered by Textual for smooth 60fps rendering.*<grok:render card_id="539501" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">10</argument>
</grok:render>

### 2. GitHub Repo Search Popup
![GitHub Search Popup](https://textual.textualize.io/_images/textual-console.png)  
*Floating overlay for real-time repo queries and favorites.*<grok:render card_id="6d5a7a" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">13</argument>
</grok:render>

### 3. Linux Distro Installation (Kali Setup)
![Kali Linux Setup](https://andronix.app/wp-content/uploads/2021/02/1.png)  
*Proot-based install and launch of Kali/Ubuntu—seamless like Andronix.*<grok:render card_id="45cdd2" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">5</argument>
</grok:render>

### 4. Nmap Scan Results in TUI
![Nmap Scan View](https://termuxpc.com/wp-content/uploads/2023/07/Termux-Screenshot-1-1024x576.png)  
*Interactive table output for ports, services, and NSE scripts.*<grok:render card_id="db395c" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">0</argument>
</grok:render>

### 5. AI Assistant with Code Hints
![AI Code Assistant](https://fedoramagazine.org/wp-content/uploads/2024/01/textual-log-scroller-1024x576.png)  
*Predictive text and Deepseek/Claude suggestions in a dedicated pane.*<grok:render card_id="aaa694" card_type="citation_card" type="render_inline_citation">
<argument name="citation_id">11</argument>
</grok:render>

## 📦 Installation

### Desktop/Linux
```bash
pip install astraterm-ai
astraterm-ai
```

### Android (via Termux)
1. Install Termux from F-Droid.
2. Run:
   ```bash
   pkg install python
   pip install astraterm-ai
   astraterm-ai
   ```

### Web Demo
Try it live: [https://astraterm-ai.vercel.app](https://astraterm-ai.vercel.app)

### From Source
```bash
git clone https://github.com/rawdripcollective-codec/AstraTerm-AI.git
cd AstraTerm-AI
pip install .
astraterm-ai
```

## 🎮 Usage

Launch: `astraterm-ai`

Key Commands:
- `ctrl+w`: Split window
- `ctrl+g`: GitHub search (floating pop-up)
- `ctrl+space`: Toggle AI assistant
- `linux install kali`: Install Kali
- `nmap scanme.nmap.org -sV -sC`: Run Nmap with NSE
- `msfconsole`: Launch Metasploit
- `osint eye-of-god "target"`: OSINT search
- `ai-assist "complete this code"`: Get AI hints

For full docs, see [docs.md](docs.md) or run `astraterm-ai --help`.

## 🤝 Contributing

Contributions welcome! Fork, create a branch, and submit a PR. Focus on ethical features only.

- Issues: Report bugs or suggest ideas [here](https://github.com/rawdripcollective-codec/AstraTerm-AI/issues).
- Code Style: PEP8, tested with pytest.
- Roadmap: v1.3 - Custom NSE scripts, more AI tools.

## 💰 Support & Sponsorship

If AstraTerm AI helps you, consider sponsoring development:
- [GitHub Sponsors](https://github.com/sponsors/rawdripcollective-codec): Monthly tiers for early access/custom features.
- [Buy Me a Coffee](https://www.buymeacoffee.com/rawdripcollective): One-time donations.
- Premium Plans: Coming soon—unlimited AI queries, enterprise support.

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

Maintained by [rawdripcollective-codec](https://github.com/rawdripcollective-codec). Original concept inspired by collaborative builds. ⭐ Star the repo to show support!