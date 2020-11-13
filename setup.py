import setuptools

setuptools.setup(
  name='project_webber',
  version="0.0.1",
  author="Stefan Eng",
  packages=setuptools.find_packages(),
  install_requires=[
    'flask',
  ],
  entry_points={
    'console_scripts': [
      'webber=project_webber:main',
    ],
  },
)
