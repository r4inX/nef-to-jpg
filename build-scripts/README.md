# Build Scripts for Standalone Executables

This directory contains PyInstaller configuration files for building standalone executables.

## Prerequisites

```bash
pip install pyinstaller
```

## Building

### Windows
```powershell
pyinstaller build-scripts/build-windows.spec
```

Output: `dist/nef-converter.exe`

### macOS
```bash
pyinstaller build-scripts/build-macos.spec
```

Output: `dist/nef-converter.app`

### Linux
```bash
pyinstaller build-scripts/build-linux.spec
```

Output: `dist/nef-converter`

## Testing

After building, test the executable:

```bash
# Windows
dist/nef-converter.exe --version

# macOS/Linux
dist/nef-converter --version
```

## Distribution

The executables can be distributed without requiring Python installation on the target system.

## Notes

- Executables are platform-specific
- Size: ~50-100 MB (includes Python runtime and dependencies)
- First run may be slower due to extraction
