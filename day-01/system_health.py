import psutil


# Get threshold values from user input
print("\nEnter threshold values for monitoring:")
cpu_threshold = int(input("CPU threshold (%): "))
memory_threshold = int(input("Memory threshold (%): "))
disk_threshold = int(input("Disk threshold (%): "))


def check_cpu(threshold):
    """Check CPU usage and alert if above threshold"""
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"\n--- CPU Metrics ---")
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Threshold: {threshold}%")
    
    if cpu_percent > threshold:
        print(f"⚠️  ALERT: CPU usage is above threshold!")
    else:
        print(f"✓ CPU usage is normal")
    
    return cpu_percent

def check_memory(threshold):
    """Check memory usage"""
    memory = psutil.virtual_memory()
    print(f"\n--- Memory Metrics ---")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Threshold: {threshold}%")
  
    if memory.percent > threshold:
        print(f"⚠️  ALERT: Memory usage is above threshold!")
    else:
        print(f"✓ Memory usage is normal")
    
    return memory.percent

def check_disk(threshold):
    """Check disk usage"""
    disk = psutil.disk_usage('/')
    print(f"\n--- Disk Metrics ---")
    print(f"Disk Usage: {disk.percent}%")
    print(f"Threshold: {threshold}%")
    
    if disk.percent > threshold:
        print(f"⚠️  ALERT: Disk usage is above threshold!")
    else:
        print(f"✓ Disk usage is normal")
    
    return disk.percent



# Check system metrics against thresholds
check_cpu(cpu_threshold)
check_memory(memory_threshold)
check_disk(disk_threshold)