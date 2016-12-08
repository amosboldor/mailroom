"""Setup mailroom madness module."""


from setuptools import setup

setup(
    name="mailroom",
    description="An implementation of backscrather function",
    version=0.1,
    author=["Ford Fowler", "Amos Boldor"],
    author_email=["fordjfowler@gmail.com", "amosboldor@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["mailroom"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
