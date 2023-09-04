from setuptools import setup, find_packages

setup(
    name='toDoList',
    version='1.0.0',
    author='Víctor Manuel Ordiales García',
    author_email='vmordiales@gmail.com',
    description='Una aplicación de lista de tareas',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'prompt_toolkit',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'toDolist = app:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='tareas, aplicación, CLI',
    project_urls={
        'Source': 'https://github.com/tu-usuario/tu-repositorio',
    },
)