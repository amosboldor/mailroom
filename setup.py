"""Setup mailroom madness module."""


from setuptools import setup

setup(
    name="mailroom",
    description="Help track and thank donors for donations",
    version=0.2,
    author=["Ford Fowler", "Amos Boldor"],
    author_email=["fordjfowler@gmail.com", "amosboldor@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["mailroom"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    },
    entry_points={
        'console_scripts': [
            'mailroom = mailroom:main'
        ]
    }
)
