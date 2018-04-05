
function [Q,R] = mgs_mm(A)
%MGS Modified Gram-Schmidt
%   [Q,R]=MGS(A) computes the reduced QR factorization of A
%   using the modified Gram-Schmidt algorithm.

% UC Berkeley Math 221, Per-Olof Persson <persson@berkeley.edu>

% inner loop replaced by matrix multification

[m,n] = size(A);
V = A;
Q = zeros(m,n);
R = zeros(n,n);
for i = 1:n
    R(i,i) = norm(V(:,i));
    Q(:,i) = V(:,i) / R(i,i);
    R(i,i+1:n) = Q(:,i)' * V(:,i+1:n); %calculate all rij(j>i) for this qi
    V(:,i+1:n) = V(:,i+1:n) - Q(:,i) * R(i,i+1:n); %substract components of all future a's in the direction of this qi   
end