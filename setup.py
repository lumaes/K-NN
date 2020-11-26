from setuptools import find_packages, setup
setup(
    name='arcana-ml',
    packages=find_packages(),
    version='0.1.0',
    description='A minimalist and educational machine learning library',
    author='lumaes',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)