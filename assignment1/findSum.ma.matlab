function [ f ] = findSum( p,n,x,y,m )
	sum = 0;
	for i = 1:n
    	sum = sum + polyval(p,x(i)) - polyval(m,x(i))*y(i);
	end
	f = sum/n;
end