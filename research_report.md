The Relationship Between Inflation and Economic Growth in Somalia (2013–2023)

1. Executive Summary

This study examines the relationship between inflation and economic growth in Somalia between 2013 and 2023. The analysis uses annual inflation and GDP growth data and applies descriptive statistics, exploratory data analysis (EDA), data visualization, and Ordinary Least Squares (OLS) regression using Python.

The regression results indicate a negative association between inflation and GDP growth. The estimated inflation coefficient is -0.8255, suggesting that a one-percentage-point increase in inflation is associated with an estimated 0.8255-percentage-point decrease in GDP growth.

However, the relationship is not statistically significant at the 5% level (p-value = 0.198). The model has an R-squared of 0.177, indicating that inflation explains approximately 17.7% of the variation in GDP growth in the sample.

2. Introduction

Inflation and economic growth are important macroeconomic indicators used to evaluate economic performance. High inflation can affect household purchasing power, production costs, investment decisions, and overall economic stability.

Somalia’s economy faces various economic challenges, making it important to understand how changes in inflation are associated with economic growth.

This study investigates the relationship between inflation and GDP growth in Somalia over the period 2git013–2023.

3. Research Question

Is inflation negatively associated with economic growth in Somalia between 2013 and 2023?

4. Research Objectives

* Examine inflation and GDP growth trends between 2013 and 2023.
* Investigate the relationship between inflation and economic growth.
* Estimate the relationship using OLS regression.
* Interpret the statistical results and identify limitations.

5. Data and Methodology

The study uses annual observations covering 2013–2023, consisting of 11 observations and three variables:

* Year
* Inflation rate (%)
* GDP growth rate (%)

GDP growth is the dependent variable, while inflation is the independent variable.

The analysis was conducted using Python, particularly Pandas, Matplotlib, and Statsmodels.

The econometric model is:

GDP Growth = β₀ + β₁ Inflation + ε

OLS regression was used to estimate the coefficient and examine the relationship between the two variables.

Data source: [Insert the original dataset source and reference.]

6. Exploratory Data Analysis

The descriptive analysis identified the following observations:

* The lowest inflation rate was 0.02% in 2016.
* The highest inflation rate was 6.78% in 2022.
* The highest GDP growth rate was 9.9% in 2015.
* The lowest GDP growth rate was -2.7% in 2013.

The visualizations showed that inflation and GDP growth followed different trends over the study period. The scatter plot indicated a downward pattern, suggesting a negative association between the variables.

7. OLS Regression Results

The estimated regression equation is:

GDP Growth = 6.9397 − 0.8255(Inflation)

The principal results are:

Statistical measure	Result
Inflation coefficient	-0.8255
Constant	6.9397
P-value	0.198
R-squared	0.177
F-statistic	1.929
Observations	11

Interpretation

The negative inflation coefficient indicates that a one-percentage-point increase in inflation is associated with an estimated 0.8255-percentage-point decrease in GDP growth.

However, the p-value of 0.198 exceeds the conventional 5% significance threshold. Therefore, the study does not find sufficient statistical evidence of a significant linear relationship between inflation and GDP growth.

The R-squared indicates that inflation explains approximately 17.7% of the variation in GDP growth in this sample.

8. Limitations

This research has several limitations:

1. The sample contains only 11 annual observations.
2. The regression includes only inflation as an explanatory variable.
3. Other economic factors, including investment, trade, remittances, agricultural production, and external shocks, are not controlled for.
4. The study does not establish a causal relationship.
5. Further time-series diagnostic testing is required.

9. Conclusion

This study investigated the relationship between inflation and economic growth in Somalia from 2013 to 2023.

The estimated OLS coefficient indicates a negative association between inflation and GDP growth. Nevertheless, the relationship is not statistically significant at the 5% level.

Consequently, the findings do not provide sufficient evidence to conclude that inflation has a statistically significant linear relationship with economic growth during the period examined.

Future research could incorporate additional macroeconomic variables and a longer time period to provide a more comprehensive understanding of Somalia’s economic performance.