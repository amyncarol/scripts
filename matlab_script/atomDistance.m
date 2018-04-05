function  distance  = atomDistance( atom1, atom2 )
%calculate the distance between two points in 3D space.
%   atom1 and atom2 should be a 3D vector
    distance = ((atom1(1)-atom2(1))^2+ (atom1(2)-atom2(2))^2+ (atom1(3)-atom2(3))^2)^0.5;

end

