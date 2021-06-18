from setuptools import setup, find_packages

requires = [
    'requests = "*"',
    'urllib3 = ">=1.26.4"',
    'Pygments = ">=2.7.4"',
    'protobuf = ">=3.17"',
    'websocket-client = ">=1.0.1"',
]

test_requirements = [
    'faker = ">=8"',
    'httpie = "*"',
    # 'pytest>=2.8.0',
    # 'mock>=2.0.0',
    # 'pytest-cov',
    # 'pytest-mock',
    # 'pytest-xdist',
]

exclude_packages = [
    "*.tests",
    "*.tests.*",
    "tests.*",
    "tests",
]

setup(
    name="python-testing-park",
    version="1.0",
    # dependencies
    install_requires=requires,
    tests_require=test_requirements,
    packages=find_packages(
        exclude=exclude_packages,
    ),
    entry_points={
        'console_scripts': [
            'test = test.help:main'
        ]
    },
    # if use console scripts must open below
    zip_safe=False,
    scripts=[],
    platforms="any",
    include_package_data=True,
    keywords=("python-testing-park", "sinlov"),
    description="eds sdk",
    long_description="testing park for python",
    license="MIT Licence",
    url="https://blog.sinlov.cn",
    author="sinlov",
    author_email="sinlovgmppt@gmail.com"
)
