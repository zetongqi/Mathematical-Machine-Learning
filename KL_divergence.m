clc;
clear;
x = [-10:0.1:10];
Apdf = normpdf(x, -1, 1);
Bpdf = normpdf(x, 1, 1);
plot(x,Apdf);
hold on;
plot(x, Bpdf);
legend('A', 'B');
KL = 0.1 * sum(Apdf .* (log(Apdf./Bpdf)));

