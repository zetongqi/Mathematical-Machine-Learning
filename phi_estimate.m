%homework 5 question 3 Monte Carlo estimate of phi
clc;
clear;
n = 1000;
p1 = 0.7;
p2 = 0.7;
%phi_hat ~ N(0, 3.2000e-06)
%true phi
phi = 0;
phi_hat = normrnd(p1-p2, (p1*(1-p1)+p2*(1-p2))/n);