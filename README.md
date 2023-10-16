# linear-reg-diagnostic
* URL:

  https://www.statsmodels.org/dev/examples/notebooks/generated/linear_regression_diagnostics_plots.html

* Install:
  
`pip install "git+https://github.com/camilousa/linear-reg-diagnostic.git`

* Example:
```python
from linear_reg_diagnostic.graphics import LinearRegDiagnostic
model = formula.ols(formula="np.log(mpg) ~ horsepower + I(horsepower ** 2)", data=df).fit()
cls = LinearRegDiagnostic(res)
cls.residual_plot()
```


