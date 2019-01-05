EXPECTED = {'Parameterization': {'extensibility-implied': False,
    'imports': {},
    'object-classes': {},
    'object-sets': {},
    'tags': 'AUTOMATIC',
    'types': {'A-Boolean': {'members': [{'name': 'a',
                                         'tag': {'kind': 'EXPLICIT',
                                                 'number': 0},
                                         'type': 'BOOLEAN'}],
                            'type': 'SEQUENCE'},
              'A-Integer': {'members': [{'name': 'a',
                                         'tag': {'kind': 'EXPLICIT',
                                                 'number': 0},
                                         'type': 'INTEGER'}],
                            'type': 'SEQUENCE'},
              'B-BooleanInteger': {'members': [{'name': 'a',
                                                'tag': {'kind': 'EXPLICIT',
                                                        'number': 0},
                                                'type': 'BOOLEAN'},
                                               {'name': 'b',
                                                'optional': True,
                                                'tag': {'kind': 'EXPLICIT',
                                                        'number': 1},
                                                'type': 'INTEGER'}],
                                   'type': 'SEQUENCE'},
              'D': {'members': [{'members': [{'name': 'a',
                                              'tag': {'kind': 'EXPLICIT',
                                                      'number': 0},
                                              'type': 'B-BooleanInteger'},
                                             {'members': [{'name': 'a',
                                                           'tag': {'kind': 'EXPLICIT',
                                                                   'number': 0},
                                                           'type': 'B-BooleanInteger'},
                                                          {'name': 'b',
                                                           'optional': True,
                                                           'tag': {'kind': 'EXPLICIT',
                                                                   'number': 1},
                                                           'type': 'INTEGER'}],
                                              'name': 'b',
                                              'tag': {'kind': 'IMPLICIT',
                                                      'number': 1},
                                              'type': 'SEQUENCE'}],
                                 'name': 'a',
                                 'tag': {'kind': 'EXPLICIT',
                                         'number': 0},
                                 'type': 'CHOICE'},
                                {'members': [{'members': [{'members': [{'name': 'a',
                                                                        'tag': {'kind': 'EXPLICIT',
                                                                                'number': 0},
                                                                        'type': 'NULL'},
                                                                       {'name': 'b',
                                                                        'optional': True,
                                                                        'tag': {'kind': 'EXPLICIT',
                                                                                'number': 1},
                                                                        'type': 'INTEGER'}],
                                                           'name': 'a',
                                                           'tag': {'kind': 'EXPLICIT',
                                                                   'number': 0},
                                                           'type': 'SEQUENCE'}],
                                              'name': 'c',
                                              'tag': {'kind': 'IMPLICIT',
                                                      'number': 0},
                                              'type': 'SEQUENCE'},
                                             {'members': [{'name': 'a',
                                                           'tag': {'kind': 'EXPLICIT',
                                                                   'number': 0},
                                                           'type': 'NULL'},
                                                          {'name': 'b',
                                                           'optional': True,
                                                           'tag': {'kind': 'EXPLICIT',
                                                                   'number': 1},
                                                           'type': 'INTEGER'}],
                                              'name': 'd',
                                              'tag': {'kind': 'IMPLICIT',
                                                      'number': 1},
                                              'type': 'SEQUENCE'}],
                                 'name': 'b',
                                 'tag': {'kind': 'EXPLICIT',
                                         'number': 1},
                                 'type': 'CHOICE'}],
                    'type': 'SEQUENCE'}},
    'values': {}}}