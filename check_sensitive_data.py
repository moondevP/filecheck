import os
import re

# Define sensitive patterns (e.g., API keys, passwords, etc.)
SENSITIVE_PATTERNS = [
    r'(api|secret|key|token|password)\s*[:=]\s*["\']?[A-Za-z0-9-_]{16,}["\']?',  # Example API key pattern
    r'^[A-Za-z0-9+\/=]{20,}$',  # Base64 strings (could be a secret key)
    r'(?i)\b(?:password|passwd|pwd)\b\s*[:=]\s*["\']?.{8,}["\']?',  # Password field
]

# Function to scan a single file for sensitive data
def scan_file_for_sensitive_data(filepath):
    with open(filepath, 'r', errors='ignore') as f:
        content = f.read()
        for pattern in SENSITIVE_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                print(f"[WARNING] Found sensitive data in {filepath}:")
                for match in matches:
                    print(f"  - {match}")

# Function to recursively scan directory for files
def scan_directory_for_sensitive_data(directory):
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.py', '.txt', '.md', '.yml', '.json')):
                scan_file_for_sensitive_data(file_path)

if __name__ == '__main__':
    directory_to_scan = input("Enter the directory to scan for sensitive data: ")
    scan_directory_for_sensitive_data(directory_to_scan)
