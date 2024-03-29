from setuptools import find_namespace_packages, setup


setup(
    name='bs_admin_utils',
    classifiers=[
        'License :: Freely Distributable'
    ],
    packages=find_namespace_packages(),
    package_data={
        'bs_admin_utils': ['*.ttf']
    },
    include_package_data=True,
    zip_safe=True,
    version='1.1.7',
    description='Blacksheep admin backend utils classes and function.',
    author='kiki-kanri',
    author_email='a470666@gmail.com',
    keywords=[],
    install_requires=[
        'beanie',
        'blacksheep',
        'kiki_utils',
        'pillow',
        'uvicorn'
    ],
    python_requires=">=3.8"
)
