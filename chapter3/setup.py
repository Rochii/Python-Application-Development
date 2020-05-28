from distutils.core import setup

with open("README") as file:
    readme = file.read()

setup(
    name = "attack_of_the_orcs_private",
    version = "2.0.0",
    packages = ["wargame"],
    url = "http://localhost:8081/simple",
    license = "LICENSE.txt",
    description = "A fantasy private game",
    long_description=readme,
    author="Rochii",
    author_email="truchero.roger@gmail.com"
)