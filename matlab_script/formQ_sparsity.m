function Q = formQ_sparsity(W,p,q)
%FORMQ Form the Q matrix in Householder triangularization.
%   Q=FORMQ(W) constructs the Q matrix from the output W in
%   the HOUSE function.

% UC Berkeley Math 221, Per-Olof Persson <persson@berkeley.edu>

[m,n] = size(W);
Q = eye(m);
for k = n:-1:1
    m0 = min(m, k+p);
    Q(k:m0,:) = Q(k:m0,:) - 2 * W(k:m0,k) * (W(k:m0,k)' * Q(k:m0,:));
end