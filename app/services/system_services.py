import psutil


def get_system_metrics():
    return {
        'cpu': psutil.cpu_percent(),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'network': psutil.net_connections(kind='tcp'),
        'users': psutil.users()
    }
