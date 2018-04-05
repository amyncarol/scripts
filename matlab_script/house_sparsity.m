function [W,R] = house_sparsity(A,p,q)
%HOUSE Householder triangularization. modified taking advantage of sparsity pattern of A, 
	%which has lower bandwidth p and upper bandwidth q.
%   [W,R]=house_sparsity(A,p,q) computes the QR factorization of A using
%   the modified Householder algorithm. Use FORMQ to construct Q.

% UC Berkeley Math 221, Per-Olof Persson <persson@berkeley.edu>

[m,n] = size(A);
W = zeros(m,n);
for k = 1:n
    m0 = min(m, k+p);
    n0 = min(n, k+p+q);
    v = A(k:m0,k);
    v(1) = v(1) + (2 * (v(1) >= 0) - 1) * norm(v);
    v = v / norm(v);
    W(k:m0,k) = v;
    A(k:m0,k:n0) = A(k:m0,k:n0) - 2 * v * (v' * A(k:m0,k:n0));
end
R = triu(A(1:n,1:n));
