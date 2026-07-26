# Obsidian Headless Sync

Use `obsidian-headless` on machines without a display to sync the wiki through Obsidian Sync.

```bash
# Requires Node.js 22+ and an Obsidian Sync subscription
npm install -g obsidian-headless
ob login --email <email> --password '<password>'
ob sync-create-remote --name "LLM Wiki"
cd "$(pwd -P)"
ob sync-setup --vault "<vault-id>"
ob sync
ob sync --continuous
```

For continuous background sync:

```ini
# ~/.config/systemd/user/obsidian-wiki-sync.service
[Unit]
Description=Obsidian Wiki Sync
After=network-online.target

[Service]
ExecStart=/path/to/ob sync --continuous
WorkingDirectory=/absolute/path/to/wiki
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-wiki-sync
sudo loginctl enable-linger "$USER"
```
