import os

config = {
    'server': {
        'host': '0.0.0.0',
        'port': os.getenv('SERVICE_PORT', '8081'),
        'server': 'paste',
        'threadpool_workers': 1000,
        'request_queue_size': 500,
        'quiet': True
    },
    'name': os.getenv('NAME', 'coding_team'),
    'database': {
        'type': 'postgresql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': os.getenv('DB_PORT', '5432'),
        'user': os.getenv('DB_USER', 'rve'),
        'pass': os.getenv('DB_PASS', ''),
        'base': os.getenv('DB_NAME', 'coding_team'),
        'app_name': os.getenv('APP_NAME', 'coding_team'),
        'charset': 'utf8'
    }
}
