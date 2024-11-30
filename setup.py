from setuptools import setup, find_packages
import re


def parse_requirements(filename):
    """ Load requirements from a pip requirements file """
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                # Skip commented lines
                continue
            if line.startswith('-e '):
                continue
            if '#' in line:
                # Split on first ' #' and remove trailing whitespace
                line = re.split(r'\s+#', line, maxsplit=1)[0].strip()
            if line:
                lines.append(line)
    return lines


requirements = parse_requirements('requirements.txt')

setup(
    name='AIDepotPythonClient',
    description='Provides AI Access at scale',
    version='0.alpha.0',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
