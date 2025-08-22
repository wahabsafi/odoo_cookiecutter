{
    'name': '{{ cookiecutter.module_name  }}',
    'version': '{{ cookiecutter.version }}',
    'summary': '{{ cookiecutter.summary }}',
    'description': '{{ cookiecutter.description }}',
    'author': '{{ cookiecutter.author }}',
    "license": "{{ cookiecutter.license }}",
    'website': '{{ cookiecutter.website }}',
    'category': '{{cookiecutter.category }}',
    'depends': ["{{ cookiecutter.dependencies }}"],
    'data': [
        # Add XML/CSV files here if needed
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
