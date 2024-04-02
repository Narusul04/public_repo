from setuptools import setup, find_packages

setup(
    name='your_script',
    version='1.0',
    packages=find_packages(),
    scripts=['your_script.py'],
    entry_points={
        'console_scripts': [
            'your_script = your_script:main'
        ]
    },
    install_requires=[
        # List of dependencies
    ],
    author='Your Name',
    author_email='your@email.com',
    description='Description of your script',
    url='https://github.com/your_username/your_script',
)

"""
A Basic setup.py file
"""