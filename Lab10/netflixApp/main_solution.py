# -*- coding: utf-8 -*-

import os
import pickle
from server_solution import app

if __name__ == '__main__':
    print('Flask starting server...')
    app.run(
        host='0.0.0.0',
        port=5432,
        debug=True
    )
