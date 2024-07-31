from setuptools import setup

setup(
    name='cli-calculator',
    version='0.1',
    packages=['app', 'tests'],
    url='',
    license='Mit License',
    author='Luis Guerra',
    author_email='guerraherrera000@gmail.com',
    description='A simple CLI calculator',
    install_requires=[
        'click'
    ],
    entry_points='''
      [console_scripts]
      calc=app.calculator:calc
  '''

)