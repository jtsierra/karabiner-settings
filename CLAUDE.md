# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a modular Karabiner-Elements configuration system that uses individual JSON rule files compiled into a single configuration. The system implements a "Hyper key" modifier (Caps Lock) for custom keyboard shortcuts across macOS.

## Build and Deploy

### Compile Configuration
```bash
./compile.sh
```
This script:
- Merges all `hyper-*.json` files into `karabiner.json`
- Automatically deploys to `~/.config/karabiner/karabiner.json`
- Changes are immediately live in Karabiner-Elements

**Requirements**: `jq` must be installed for JSON processing

### Generate Codebase Snapshot
```bash
python3 joiner.py
```
Compiles all files into a timestamped text file in `joiner/` directory (useful for documentation/backups).

## Architecture

### Modular Rule System

Each `hyper-*.json` file contains a single rule configuration with this structure:
```json
{
  "description": "Rule description",
  "manipulators": [...]
}
```

The compile script concatenates these into `karabiner.json` which has the full Karabiner profile structure:
```
karabiner.json
├── profiles[0]
    ├── complex_modifications
    │   └── rules[] (compiled from hyper-*.json files)
    ├── name: "Default profile"
    └── virtual_hid_keyboard settings
```

### Hyper Key Implementation

The Hyper modifier is implemented via a variable-based system:
1. `hyper-key.json` sets the `hyper_caps_lock` variable when Caps Lock is held
2. All other rules check for `{"name": "hyper_caps_lock", "type": "variable_if", "value": 1}` in their conditions
3. This allows Caps Lock + any key combinations without modifier key conflicts

### Application-Specific Rules

App-specific shortcuts use `frontmost_application_if` conditions with bundle identifiers:
- `hyper-app-vscode.json`: Rules for `com.microsoft.VSCode`
- `hyper-app-chrome.json`: Rules for `com.google.Chrome`

These files demonstrate the pattern for adding app-specific shortcuts that only activate when the target app is focused.

### Modifier Combinations

Rules support layered modifiers with the Hyper key:
- `Hyper + Key`: Basic shortcuts (e.g., arrow navigation)
- `Hyper + Cmd + Key`: Secondary layer (e.g., page up/down)
- `Hyper + Option + Key`: Tertiary layer (e.g., document top/bottom)

## Workflow for Adding New Shortcuts

1. Create new file: `hyper-<descriptive-name>.json`
2. Follow the JSON structure from existing files
3. Add manipulators with appropriate conditions
4. Run `./compile.sh` to build and deploy
5. Test the shortcuts immediately (no restart needed)
6. Commit if working correctly

## Important Files

- `hyper-key.json`: Core Hyper modifier definition - **required for all other rules**
- `compile.sh`: Build and deployment script
- `karabiner.json`: Compiled output (auto-generated, tracked for reference)
- `keybindings.json`: VS Code keybindings (separate from Karabiner config)

## Notes

- The order of rules in `compile.sh` matters: files are processed alphabetically via `hyper-*.json` glob
- `hyper-key.json` should logically be first but the alphabetical ordering places it mid-sequence; this works because variable setting happens independently
- Global shortcuts (no app condition) should use `"modifiers": {"optional": ["any"]}` to work with any modifier state
- App-specific rules override global rules when their conditions match
