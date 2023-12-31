from setuptools import setup, find_packages


setup(
    name="linear-reg-diagnostic",
    version="1.0",
    packages=['linear_reg_diagnostic'],
    install_requires=[
        'numpy',
        'pandas',
        'statsmodels',
        'seaborn',
        'matplotlib'
    ],
    url="https://www.statsmodels.org/dev/examples/notebooks/generated/linear_regression_diagnostics_plots.html"
)
