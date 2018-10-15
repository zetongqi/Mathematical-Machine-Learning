clc;
clear;
%param for first Binomial dist x1
n1 = 160;
p1 = 0.7;
%param for second Binomial dist x2
n2 = 160;
p2 = 0.7;
n = n1 + n2;
theta = p1 - p2;
var1 = p1*(1-p1)/n1;
var2 = p2*(1-p2)/n2;
cnt = 0;
for i=0:5000
    r1 = normrnd(p1,p1*(1-p1)/(n1^2/(n1+n2)));
    r2 = normrnd(p2,p2*(1-p2)/(n2^2/(n1+n2)));
    theta_hat = r1 - r2;
    if abs(theta_hat - theta) > 0.01
        cnt = cnt + 1;
    end
end
cnt/i
