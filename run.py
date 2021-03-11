#!/usr/bin/env python3

import os
from main import app
from service.InitializeService import InitializeService


def initialize():
    print("initializing")
    InitializeService.initialize()

if __name__ == '__main__':
    initialize()
    app.run(host='0.0.0.0', port=8080)

