#!/bin/bash

# Compile to local karabiner.json first
cat > karabiner.json << 'EOF'
{
  "profiles": [{
    "complex_modifications": {
      "rules": [
EOF

# Add each rule
first=true
for file in hyper-*.json; do
  if [ "$first" = true ]; then
    cat "$file" | jq -c '.' >> karabiner.json
    first=false
  else
    echo "," >> karabiner.json
    cat "$file" | jq -c '.' >> karabiner.json
  fi
done

# Close the JSON structure
cat >> karabiner.json << 'EOF'
      ]
    },
    "name": "Default profile",
    "selected": true,
    "virtual_hid_keyboard": {
      "country_code": 0,
      "keyboard_type_v2": "ansi"
    }
  }]
}
EOF

# Copy to Karabiner config location
cp karabiner.json ~/.config/karabiner/karabiner.json

echo "✅ Compiled and copied to Karabiner config successfully!"
echo "📍 Config updated at: ~/.config/karabiner/karabiner.json"