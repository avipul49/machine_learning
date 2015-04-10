function [ f ] = loss( p,n,x,y )
	sum = 0;
	for i = 1:n
    	sum = sum + (polyval(p,x(i)) - y(i)).^2;
	end
	f = sum/n;
end
