from setuptools import setup, find_packages

setup(
    name='fast_dijkstra',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    author='Chenwei Zhang',
    author_email='chwzhan@gmail.com',
    py_modules=['fast_dijkstra'],
    description='A Python package for Fast Dijkstra\'s algorithm with limited neighborhood exploration',
    url='https://github.com/chenwei-zhang/fast_dijkstra',
    license='GNU GPLv3',
    keywords='dijkstra graph shortest-path',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
    ],
)