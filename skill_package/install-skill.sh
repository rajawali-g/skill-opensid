#!/usr/bin/env bash
# ==============================================================================
# Installer AI Skill OpenSID Theme Developer untuk Antigravity (Linux / macOS)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SOURCE="$SCRIPT_DIR/opensid-theme-developer"

if [ ! -d "$SKILL_SOURCE" ]; then
    SKILL_SOURCE="$SCRIPT_DIR/.agents/skills/opensid"
fi

if [ ! -d "$SKILL_SOURCE" ]; then
    echo "Error: Direktori sumber skill tidak ditemukan di $SKILL_SOURCE"
    exit 1
fi

GLOBAL_DIR="$HOME/.gemini/config/skills/opensid-theme-developer"
WORKSPACE_DIR="$(pwd)/.agents/skills/opensid-theme-developer"

echo "=========================================================="
echo "  INSTALLER: AI SKILL OPENSID THEME DEVELOPER             "
echo "  Platform: Google Antigravity / Gemini CLI / AI Agent    "
echo "=========================================================="

echo "[*] Memasang ke Global Antigravity ($GLOBAL_DIR)..."
mkdir -p "$GLOBAL_DIR"
cp -r "$SKILL_SOURCE"/* "$GLOBAL_DIR/"
echo "    [OK] Berhasil dipasang ke Global!"

echo "[*] Memasang ke Workspace Aktif ($WORKSPACE_DIR)..."
mkdir -p "$WORKSPACE_DIR"
cp -r "$SKILL_SOURCE"/* "$WORKSPACE_DIR/"
echo "    [OK] Berhasil dipasang ke Workspace!"

echo "=========================================================="
echo "  INSTALASI SELESAI & SKILL TELAH SIAP DIGUNAKAN!        "
echo "=========================================================="
