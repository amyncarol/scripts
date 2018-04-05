
function [Q,R] = clgs_mm(A)
%CLGS Classical Gram-Schmidt
%   [Q,R]=CLSG(A) computes the reduced QR factorization of A
%   using the classical Gram-Schmidt algorithm.

% UC Berkeley Math 221, Per-Olof Persson <persson@berkeley.edu>

% inner loop replaced by matrix multification

[m,n] = size(A);
Q = zeros(m,n);
R = zeros(n,n);
for j = 1:n
    v = A(:,j);
    R(1:j-1,j) = Q(:,1:j-1)' * v; %calculate Rij's
    v = v - Q(:,1:j-1) * R(1:j-1,j);  %substract all the components of a in previous q
    R(j,j) = norm(v);
    Q(:,j) = v / R(j,j);
end
