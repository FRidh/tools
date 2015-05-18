from setuptools import setup, find_packages

setup(
      name='tools',
      version='0.0',
      description="tools",
      author='tools',
      author_email='fridh@fridh.nl',
      license='LICENSE',
      packages=find_packages(exclude=["tests"]),
      #py_modules=['turbulence'],
      scripts=[],
      zip_safe=False,
      )
