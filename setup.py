import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='keynoteSlideStopwatch',  
     version='0.1.6',
     scripts=['keynoteSlideStopwatch'] ,
     author="Géry Casiez",
     author_email="gery.casiez@gmail.com",
     description="Allows to measure the time spent on each slide during a presentation with Apple Keynote.",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://github.com/casiez/KeynoteSlideStopwatch",
     packages=setuptools.find_packages(),
     install_requires=[ 'py-applescript', 'pyobjc==6.1', 'datetime'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: MacOS",
     ],

 )