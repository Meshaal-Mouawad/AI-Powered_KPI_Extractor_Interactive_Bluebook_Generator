import os
import re
from typing import List, Dict, Any # <-- ADD THIS LINE

def find_kpis_in_directory(path: str) -> List[Dict[str, Any]]:
    """
    Scans a directory for Python files and extracts KPI definitions.

    A KPI is defined by a comment like: '# KPI: KPI Name'
    """
    kpis = []
    kpi_pattern = re.compile(r'#\s*KPI:\s*(.*)')

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # Capture code context around the KPI
                        for i, line in enumerate(lines):
                            match = kpi_pattern.search(line)
                            if match:
                                kpi_name = match.group(1).strip()
                                # Get a larger window before/after so the function header and calculation are included
                                start = max(0, i - 80)
                                end = min(len(lines), i + 120)
                                code_context = "".join(lines[start:end])

                                kpis.append({
                                    'name': kpi_name,
                                    'file_path': os.path.abspath(file_path),
                                    'line_number': i + 1,
                                    'code_context': code_context
                                })
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")
    return kpis