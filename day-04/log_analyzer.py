def read_log_file(log_file):
    try:
        with open(log_file, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except Exception as e:
        return None


def count_log_levels(content):
    info_count = content.count("INFO")
    warning_count = content.count("WARNING")
    error_count = content.count("ERROR")
    
    return info_count, warning_count, error_count


def create_summary(info_count, warning_count, error_count):
    summary = []
    summary.append("=" * 50)
    summary.append("LOG SUMMARY")
    summary.append("=" * 50)
    summary.append(f"INFO messages: {info_count}")
    summary.append(f"WARNING messages: {warning_count}")
    summary.append(f"ERROR messages: {error_count}")
    summary.append(f"Total messages: {info_count + warning_count + error_count}")
    summary.append("=" * 50)
    
    return "\n".join(summary)


def write_summary_to_file(summary, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(summary)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def main():
    log_file = input("Enter log file name (default: app.log): ") or "app.log"
    output_file = input("Enter output file name (default: log_summary.txt): ") or "log_summary.txt"
    
    content = read_log_file(log_file)
    
    if content:
        info_count, warning_count, error_count = count_log_levels(content)
        summary = create_summary(info_count, warning_count, error_count)
        
        print("\n" + summary)
        
        if write_summary_to_file(summary, output_file):
            print(f"\n✓ Summary saved to {output_file}")
    else:
        print(f"Error: Unable to read file '{log_file}'")


if __name__ == "__main__":
    main()
