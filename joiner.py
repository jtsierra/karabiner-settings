#!/usr/bin/env python3
"""
Karabiner Config Joiner
Automatically compiles all files in the karabiner directory into a single text file
"""

import os
from datetime import datetime

# Configuration
project_name = 'karabiner'
base_path = os.path.expanduser('~/Documents/')
project_path = os.path.join(base_path, project_name)
output_folder = os.path.join(project_path, 'joiner')
exclusions = ['.git', '__pycache__', '.DS_Store', 'venv', 'node_modules', 'joiner']

def should_include_file(file_path, exclusions):
    """Check if file should be included based on exclusions"""
    return not any(exclusion in file_path for exclusion in exclusions)

def compile_all_files(project_path, project_name, output_folder, exclusions):
    """Compile all files in the project directory"""
    
    # Create joiner folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Create output filename with timestamp at the beginning
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = os.path.join(output_folder, f'{timestamp}_{project_name}_compiled.txt')
    
    # Collect all files
    files_to_compile = []
    for root, dirs, files in os.walk(project_path):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not any(exclusion in d for exclusion in exclusions)]
        
        for file in files:
            file_path = os.path.join(root, file)
            if should_include_file(file_path, exclusions):
                files_to_compile.append(file_path)
    
    # Sort files for consistent output
    files_to_compile.sort()
    
    # Write compiled output
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Header
        compile_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{'='*80}\n")
        output_file.write(f"PROJECT: {project_name.upper()}\n")
        output_file.write(f"COMPILED ON: {compile_timestamp}\n")
        output_file.write(f"TOTAL FILES: {len(files_to_compile)}\n")
        output_file.write(f"{'='*80}\n\n")
        
        # File contents
        for file_path in files_to_compile:
            relative_path = os.path.relpath(file_path, project_path)
            output_file.write(f"{'-'*40}\n")
            output_file.write(f"File: {relative_path}\n")
            output_file.write(f"{'-'*40}\n")
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    output_file.write(file.read())
                    output_file.write('\n\n')
                print(f"✓ Compiled: {relative_path}")
            except Exception as e:
                print(f"✗ Error reading {relative_path}: {e}")
    
    print(f"\n{'='*80}")
    print(f"✅ Compilation complete!")
    print(f"📁 Output file: {output_file_path}")
    print(f"📊 Total files compiled: {len(files_to_compile)}")
    print(f"{'='*80}")
    
    return output_file_path

if __name__ == "__main__":
    print(f"🔧 Karabiner Config Joiner")
    print(f"{'='*80}")
    print(f"Project path: {project_path}")
    print(f"Output folder: {output_folder}\n")
    
    if not os.path.exists(project_path):
        print(f"❌ Error: Project path does not exist: {project_path}")
        exit(1)
    
    compile_all_files(project_path, project_name, output_folder, exclusions)