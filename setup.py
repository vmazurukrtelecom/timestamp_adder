from setuptools import setup, find_packages

setup(
    name='timestamp_adder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'add-timestamp=timestamp_adder.main:add_timestamp_command',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple tool to add timestamp to text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vmazurukrtelecom/timestamp_adder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
