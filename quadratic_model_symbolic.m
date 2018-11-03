%symbolic equations
%cs761 midterm question 2 (a)
%when a linear model w'*x is inadequate for a good prediction
%use quadratic model w0 + w1'x + x'*w2*x where w2 is a matrix, w1 is a
%vector and w0 is a constant
clc;
clear;
X = sym('x', [4 1], 'real');
W2 = sym('w', [4 4], 'real');
W1 = sym('w', [4 1], 'real');
w0 = sym('w0', 'real');
X_tilde = reshape(X*X', 16, 1);
X_tilde = [X_tilde; X; 1];
W_tilde = reshape(W2, 16, 1);
W_tilde = [W_tilde; W1; w0];
first = expand(w0 + W1'*X + X'*W2*X);
second = expand(W_tilde'*X_tilde);
isequaln(first, second)