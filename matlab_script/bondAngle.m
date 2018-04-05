function angle = bondAngle( atom1, atom2, atom3 )
%calculate the bondAngle of atom1--atom2----atom3
%   atom1 atom2 atom3 should be 3D vectors

distance12 = atomDistance(atom1, atom2);
distance23 = atomDistance(atom2, atom3);
distance13 = atomDistance(atom1, atom3);

cos2 = (distance12^2+distance23^2-distance13^2)/2/distance12/distance23;

angle = acos(cos2)*180/pi;

end

