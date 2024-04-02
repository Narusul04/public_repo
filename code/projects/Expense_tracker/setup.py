from setuptools import setup, find_packages

setup(
    name='expense_tracker',
    version='1.0',
    packages=find_packages(),
    scripts=['expense_tracker.py'],
    entry_points={
        'console_scripts': [
            'expense_tracker = expense_tracker:main'
        ]
    },
    install_requires=[
        # List of dependencies
    ],
    author='Jason Sul',
    author_email='Narusul04@gmail.com',
    description='A basic expense tracker.',
    url='https://github.com/Narusul04/public_repo/tree/main/code/projects/Expense_tracker',
)
