
function [Q,R] = mgs(A)
%MGS Modified Gram-Schmidt
%   [Q,R]=MGS(A) computes the reduced QR factorization of A
%   using the modified Gram-Schmidt algorithm.

% UC Berkeley Math 221, Per-Olof Persson <persson@berkeley.edu>

[m,n] = size(A);
V = A;
Q = zeros(m,n);
R = zeros(n,n);
for i = 1:n
    R(i,i) = norm(V(:,i));
    Q(:,i) = V(:,i) / R(i,i);
    for j = i+1:n
        R(i,j) = Q(:,i)' * V(:,j);
        V(:,j) = V(:,j) - R(i,j) * Q(:,i);
    end
end
