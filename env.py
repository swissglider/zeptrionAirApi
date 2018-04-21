from setuptools import setup

requires = [
    'zeroconf', 'requests', 'xml.etree.ElementTree', 'asyncio', 'websockets', 'json', 'socket', 'aiohttp'
]

setup(
    name='zeptrion_air_api',
    install_requires=requires,
)