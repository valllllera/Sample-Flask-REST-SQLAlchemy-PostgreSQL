POSTGRES = {
    'user': 'val',
    'pw': '',
    'db': 'sportspots',
    'host': 'localhost',
    'port': '5432',
}

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES