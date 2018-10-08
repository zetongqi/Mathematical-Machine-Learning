# Mathematical-Machine-Learning
The repository for ECE761: Mathematical Foundations of Machine Learning
## Distrete Probability Distributions
Bernoulli, Binomial, Multinomial, Poisson
## Optimal Bayes Classification
Bayes Optimal Classifier

Bayes Risk

## Nearest Neighbor Classifier

Classification rule: return the label of the nearest point

Bound of probability of error

## Histogram Classifier

Classification rule: divide subspace into bins, return the majority vote of the bin in which the test point falls into

Bound of difference of probability of error with Bayes classifier

## Multivariate Normal Distribution

Fitting a model with class-conditional probabilities

Log Likelihood Ratio Test (Log-LRT)

Generative Models: given a label, what is the probability of a data from that label that looks that X=x

Bound of error rate of a classifier

## Kullback-Leibler Divergence

Distance measure of two distributions

## Maximum Likelihood Estimation

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta^{\star}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta^{\star}" title="\theta^{\star}" /></a> is a parameter from the family of all posible <a href="https://www.codecogs.com/eqnedit.php?latex=\Theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Theta" title="\Theta" /></a> that parameterize the function <a href="https://www.codecogs.com/eqnedit.php?latex=f(x|\theta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x|\theta)" title="f(x|\theta)" /></a> that minimizes the KL-Divergence <a href="https://www.codecogs.com/eqnedit.php?latex=D(q||p_{\theta})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D(q||p_{\theta})" title="D(q||p_{\theta})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{\theta_{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{\theta_{n}}" title="\hat{\theta_{n}}" /></a> is a parameter from the family that maximize the likelihood <a href="https://www.codecogs.com/eqnedit.php?latex=\prod_{i}&space;p(x_i|\theta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\prod_{i}&space;p(x_i|\theta)" title="\prod_{i} p(x_i|\theta)" /></a> or minimizes the loss<a href="https://www.codecogs.com/eqnedit.php?latex=-\sum_{i}&space;\log&space;p(x_{i}|\theta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?-\sum_{i}&space;\log&space;p(x_{i}|\theta)" title="-\sum_{i} \log p(x_{i}|\theta)" /></a>.

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{\theta_{n}}&space;\stackrel{asymp}\sim&space;\mathcal{N}(\theta^{*},\,n^{-1}I^{-1}(\theta^{*}))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{\theta_{n}}&space;\stackrel{asymp}\sim&space;\mathcal{N}(\theta^{*},\,n^{-1}I^{-1}(\theta^{*}))" title="\hat{\theta_{n}} \stackrel{asymp}\sim \mathcal{N}(\theta^{*},\,n^{-1}I^{-1}(\theta^{*}))" /></a>
