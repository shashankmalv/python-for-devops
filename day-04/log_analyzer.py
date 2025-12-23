"""
Log Analyzer - Analyzes log files and counts log levels
Follows PEP8 and Python best practices
"""


def read_log_file(log_file):
    """
    Read log file and return lines.
    
    Args:
        log_file (str): Path to log file
        
    Returns:
        list: Lines from file or None if error
    """
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            
            if not lines:
                print(f"Warning: File '{log_file}' is empty.")
                return None
                
            return lines
            
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{log_file}'.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def count_log_levels(lines):
    """
    Count log levels (INFO, WARNING, ERROR) in lines.
    
    Args:
        lines (list): List of log lines
        
    Returns:
        dict: Dictionary with counts
    """
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    
    for line in lines:
        for level in counts.keys():
            if level in line:
                counts[level] += 1
    
    return counts


def create_summary(counts):
    """
    Create summary string from counts.
    
    Args:
        counts (dict): Dictionary with log level counts
        
    Returns:
        str: Formatted summary
    """
    total = sum(counts.values())
    
    summary = []
    summary.append("=" * 50)
    summary.append("LOG SUMMARY")
    summary.append("=" * 50)
    summary.append(f"INFO messages: {counts['INFO']}")
    summary.append(f"WARNING messages: {counts['WARNING']}")
    summary.append(f"ERROR messages: {counts['ERROR']}")
    summary.append(f"Total messages: {total}")
    summary.append("=" * 50)
    
    return "\n".join(summary)


def write_summary_to_file(summary, output_file):
    """
    Write summary to output file.
    
    Args:
        summary (str): Summary text
        output_file (str): Output file path
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(output_file, 'w') as file:
            file.write(summary)
        return True
    except PermissionError:
        print(f"Error: Permission denied to write '{output_file}'.")
        return False
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def main():
    """Main function to orchestrate log analysis."""
    log_file = input("Enter log file name (default: app.log): ") or "app.log"
    output_file = input("Enter output file name (default: log_summary.txt): ") or "log_summary.txt"
    
    lines = read_log_file(log_file)
    
    if lines:
        counts = count_log_levels(lines)
        summary = create_summary(counts)
        
        print("\n" + summary)
        
        if write_summary_to_file(summary, output_file):
            print(f"\n✓ Summary saved to '{output_file}'")
        else:
            print(f"\n✗ Failed to save summary to '{output_file}'")
    else:
        print("\n✗ Unable to analyze log file.")


if __name__ == "__main__":
    main()
