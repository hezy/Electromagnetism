s = -2:0.1:2;
[x,y] = meshgrid(s);
f = x.*exp(-(x.^2 + y.^2));
figure(1); mesh(x,y,f);
title('2D Scalar function f=e^{-(x^2+y^2)}');

 [px,py] = gradient(f,.2,.2);
 figure(2); contour(x,y,f); hold on
 quiver(s,s,px,py)
 title('Contour and gradient of function f=e^{-(x^2+y^2)}');
%
