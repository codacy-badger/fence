from setuptools import setup, find_packages

setup(
    name="fence",
    version="0.2.0",
    install_requires=[
        "Authlib",
        "oauth2client<4.0dev,>=2.0.0",
        "addict>=2.1.1, <3.0.0",
        "boto>=2.36.0,<3.0.0",
        "botocore>=1.7,<1.9.0",
        "boto3>=1.5,<1.6",
        "cached_property>=1.5.1,<2.0.0",
        "cryptography>=2.1.2",
        "enum34>=1.1.6",
        "flask-restful>=0.3.6,<1.0.0",
        "Flask>=0.10.1,<1.0.0",
        "Flask-CORS>=3.0.3,<4.0.0",
        "Flask_OAuthlib>=0.9.4,<1.0.0",
        "Flask_SQLAlchemy_Session>=1.1,<2.0",
        "gen3cirrus>=0.4.0,<1.0",
        "google_api_python_client>=1.6.4,<2.0.0",
        "httplib2>=0.10.3,<1.0.0",
        "python-jose>=2.0.0,<3.0.0",
        "oauthlib>=2.1.0,<3.0.0",
        "psycopg2>=2.7.3.2,<3.0.0.0",
        "pysftp>=0.2.9,<1.0.0",
        "pytest-flask>=0.10.0,<1.0.0",
        "pytest>=3.2.3,<4.0.0",
        "bcrypt>=3.1.4,<4.0.0",
        "python_dateutil>=2.6.1,<3.0.0",
        "PyJWT>=1.5.3,<2.0.0",
        "requests>=2.18.0,<3.0.0",
        "six>=1.11.0,<2.0.0",
        "SQLAlchemy>=0.9.9,<1.0.0",
        "temps>=0.3.0,<1.0.0",
        "userdatamodel~=1.4",
        "Werkzeug>=0.12.2,<1.0.0",
        "storageclient",
        "pyyaml~=5.1",
    ],
    scripts=["bin/fence-create"],
    packages=find_packages(),
)
