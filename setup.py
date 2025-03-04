from setuptools import setup, find_packages

setup(
    name='toolfuzz',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='',
    license='MIT',
    author='Ivan Milev',
    author_email='imilev@ethz.ch',
    description='ToolFuzz - Automatic Agent Tool Testing',
    install_requires=[
        'langchain-openai>=0.3.6',
        'langgraph>=0.2.74',
        'langchain>=0.3.19',
        'langchain-core>=0.3.37',
        'faker',
        'jinja2',
        'tqdm',
    ]
)
