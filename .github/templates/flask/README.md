# python_template_usage Flask Application

This is a Flask application.

## Installation

From source:

```bash
git clone https://github.com/rex106/python_template_usage python_template_usage
cd python_template_usage
make install
```

From pypi:

```bash
pip install python_template_usage
```

## Executing

This application has a CLI interface that extends the Flask CLI.

Just run:

```bash
$ python_template_usage
```

or

```bash
$ python -m python_template_usage
```

To see the help message and usage instructions.

## First run

```bash
python_template_usage create-db   # run once
python_template_usage populate-db  # run once (optional)
python_template_usage add-user -u admin -p 1234  # ads a user
python_template_usage run
```

Go to:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - https://localhost:5000/api/v1/product/
  - https://localhost:5000/api/v1/product/1
  - https://localhost:5000/api/v1/product/2
  - https://localhost:5000/api/v1/product/3


> **Note**: You can also use `flask run` to run the application.
