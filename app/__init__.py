from flask import Flask


def generate_app(context='config.development'):
    return Flask()
