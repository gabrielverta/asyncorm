class MigrationBase(object):
    depends = []
    operations = {
        'stage1': [],
        'stage2': [],
        'stage3': [],
        'stage4': [],
    }
    models = {}
