POSTGRES = {
    'user': 'sportspots',
    'pw': 'sportspotspass',
    'db': 'spotsdb',
    'host': '172.17.0.2',
    'port': '5432',
}

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


SECRET_KEY = 'd33cdf514b426b4183059e5b7b3299550871e03c'