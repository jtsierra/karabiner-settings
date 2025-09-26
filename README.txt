## How It Works

1. **Modular Files**: Each `hyper-*.json` file contains one keyboard modification rule
2. **Compile Script**: `compile.sh` merges all `hyper-*.json` files into `karabiner.json`
3. **Auto-Deploy**: The script automatically copies the compiled config to `~/.config/karabiner/karabiner.json`

## Current Hotkeys

### Navigation
| Shortcut | Action |
|----------|--------|
| `Caps Lock` (hold) | Acts as Hyper modifier |
| `Hyper + I` | Up Arrow |
| `Hyper + J` | Left Arrow |
| `Hyper + K` | Down Arrow |
| `Hyper + L` | Right Arrow |
| `Hyper + Backspace` | Forward Delete |

### System
| Shortcut | Action |
|----------|--------|
| `Hyper + Q` | Switch Input Language |

### Rectangle Window Management
| Shortcut | Action |
|----------|--------|
| `Hyper + W` | Window Top Half |
| `Hyper + A` | Window Left Half |
| `Hyper + S` | Window Bottom Half |
| `Hyper + D` | Window Right Half |
| `Hyper + C` | Window Centered |
| `Hyper + Enter` | Window Maximize (Almost Full Screen) |

### VS Code (only when VS Code is active)
| Shortcut | Action |
|----------|--------|
| `Hyper + \` | Split Editor |
| `Hyper + T` | Focus Terminal |

## Workflow

### Adding a New Hotkey

1. Create a new file: `hyper-<name>.json`
2. Add your rule configuration
3. Run `./compile.sh` to merge and deploy
4. Test the hotkey in any application
5. If it works, commit; if not, iterate

### Testing Changes
```bash
# Make changes to any hyper-*.json file
./compile.sh
# Test immediately - changes are live in Karabiner