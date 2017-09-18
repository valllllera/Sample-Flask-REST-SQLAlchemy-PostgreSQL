POSTGRES = {
    'user': 'sportspots',
    'pw': 'sportspotspass',
    'db': 'spotsdb',
    'host': '172.17.0.2',
    'port': '5432',
}

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES