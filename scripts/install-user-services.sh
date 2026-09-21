#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/systemd/user"
target_dir="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"

mkdir -p "$target_dir"

for unit in "$source_dir"/*; do
    ln -sfn "$unit" "$target_dir/$(basename "$unit")"
done

systemctl --user daemon-reload
systemctl --user enable qtile-session.target

printf 'Qtile user services installed in %s\n' "$target_dir"
