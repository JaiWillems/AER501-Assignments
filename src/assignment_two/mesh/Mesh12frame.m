%
% Generate mesh for frame with nbays and inode internal nodes
%
% Each bay is assumed to have repeated geometry of the following form.
%
%
%  2     4     6     8
% |>o-----o-----o-----o
%    \    |\    |\    |
%      \  |  \  |  \  |
%        \|    \|    \|
% |>o-----o-----o-----o
%   1     3     5     7
%

function [NOD, X, Y, dof_active] = Mesh12frame(inodes)

nbays = 3;

% inodes = 1;

% Define baseline geometry with 1 element per beam here
NODorig = [1,3; 3,4; 2,4; 2,3; 3,5; 5,6; 4,6; 4,5; 5,7; 7,8; 6,8; 6,7];
Xcord = [0,0,1,1,2,2,3,3]; 
Ycord = [0,1,0,1,0,1,0,1];

% Prepare counters for element and node numbers
elc = 1; nc = 1;

% First node
X(1) = Xcord(1); Y(1) = Ycord(1);

delx = 1/(inodes+1); dely = delx;

%%%%%%%
%%BAY 1
%%%%%%%
%Beam 1
for i = 1: inodes + 1
    X(nc + 1) = X(nc) + delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
%Beam 2
for i = 1: inodes + 1
    X(nc + 1) = X(nc);
    Y(nc + 1) = Y(nc) + dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 

%Beam 3
for i = 1: inodes + 1
    X(nc + 1) = X(nc)-delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 

%Beam 4
for i = 1: inodes 
    X(nc + 1) = X(nc)+delx;
    Y(nc + 1) = Y(nc)-dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
NOD(elc,1) = nc; NOD(elc,2) = inodes+2;
elc = elc + 1;


%%%%%%%
%%BAY 2
%%%%%%%
%Beam 1
X(nc+1) = X(inodes+2) + delx; 
Y(nc+1) = Y(inodes+2) ;
nc = nc + 1;
NOD(elc,1) = inodes+2; NOD(elc,2) = nc;
elc = elc + 1;
for i = 1: inodes 
    X(nc + 1) = X(nc) + delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
%Beam 2
for i = 1: inodes + 1
    X(nc + 1) = X(nc);
    Y(nc + 1) = Y(nc) + dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 

%Beam 3
for i = 1: inodes 
    X(nc + 1) = X(nc)-delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
NOD(elc,1) = nc; NOD(elc,2) = 2*inodes+3;
elc = elc + 1;

X(nc+1) = X(2*inodes+3) + delx; 
Y(nc+1) = Y(2*inodes+3) - dely ;
nc = nc + 1; 
NOD(elc,1) = 2*inodes+3; NOD(elc,2) = nc;
elc = elc + 1;
%Beam 4
for i = 1: inodes - 1
    X(nc + 1) = X(nc)+delx;
    Y(nc + 1) = Y(nc)-dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
NOD(elc,1) = nc; NOD(elc,2) = 4*inodes+4+inodes+1;
elc = elc + 1;


%%%%%%%
%%BAY 3
%%%%%%%
%Beam 1
X(nc+1) = X(5*inodes+5) + delx; 
Y(nc+1) = Y(5*inodes+5) ;
nc = nc + 1; 
NOD(elc,1) = 5*inodes+5; NOD(elc,2) = nc;
elc = elc + 1;
for i = 1: inodes 
    X(nc + 1) = X(nc) + delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
%Beam 2
for i = 1: inodes + 1
    X(nc + 1) = X(nc);
    Y(nc + 1) = Y(nc) + dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 

%Beam 3
for i = 1: inodes 
    X(nc + 1) = X(nc)-delx;
    Y(nc + 1) = Y(nc);
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
NOD(elc,1) = nc; NOD(elc,2) = 6*inodes+6;
elc = elc + 1;

X(nc+1) = X(6*inodes+6) + delx; 
Y(nc+1) = Y(6*inodes+6) - dely ;
nc = nc + 1; 
NOD(elc,1) = 6*inodes+6; NOD(elc,2) = nc;
elc = elc + 1;
%Beam 4
for i = 1: inodes - 1
    X(nc + 1) = X(nc)+delx;
    Y(nc + 1) = Y(nc)-dely;
    nc = nc + 1;
    NOD(elc,1) = nc-1; NOD(elc,2) = nc;
    elc = elc + 1;
end 
NOD(elc,1) = nc; NOD(elc,2) = 9*inodes+7;
elc = elc + 1;


% Find indices of constrained nodes
constr_node(1) = 1;
constr_node(2) = 4+3*inodes;


% Find indices of constrained nodes
constr_node(1) = 1;
constr_node(2) = 4+3*inodes;

% Generate indices of active and inactive DOFs
itmp = constr_node(2) - 1;

dof_restr = [1, 2, 3, 3*itmp + 1, 3*itmp + 2, 3*itmp + 3]; % indices of restrained DOF 
dof_active = [4:3*itmp, 3*itmp+4:3*length(X)]; % indices of unrestrained DOF

% To enforce zero displacement BCs after assembly 
%
% K = K(dof_active, dof_active); should do the job
%

