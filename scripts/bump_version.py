#!/usr/bin/env python3
"""
Simple script to bump the version number in all relevant files.
Usage: python bump_version.py NEW_VERSION
Example: python bump_version.py 0.2.0
"""

import sys
import re
import os

def update_file(filename, pattern, replacement):
    """Update a file by replacing pattern with replacement."""
    with open(filename, 'r') as f:
        content = f.read()
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py NEW_VERSION")
        print("Example: python bump_version.py 0.2.0")
        sys.exit(1)
    
    new_version = sys.argv[1]
    
    # Remove the 'v' prefix if provided
    if new_version.startswith('v'):
        new_version = new_version[1:]
    
    # Update setup.py
    update_file(
        'setup.py',
        r'version="[0-9]+\.[0-9]+\.[0-9]+"',
        f'version="{new_version}"'
    )
    
    # Update __init__.py
    update_file(
        'tax_calculator/__init__.py',
        r"__version__ = '[0-9]+\.[0-9]+\.[0-9]+'",
        f"__version__ = '{new_version}'"
    )
    
    # Update README.md badge
    update_file(
        'README.md',
        r'!\[Version\]\(https://img\.shields\.io/badge/version-[0-9]+\.[0-9]+\.[0-9]+-blue\)',
        f'![Version](https://img.shields.io/badge/version-{new_version}-blue)'
    )
    
    print(f"\nVersion bumped to {new_version}")
    print("\nNext steps:")
    print(f"1. git commit -am 'Bump version to {new_version}'")
    print(f"2. git tag v{new_version}")
    print(f"3. git push origin main && git push origin v{new_version}")
    print("4. Create a release on GitHub")

if __name__ == "__main__":
    main()