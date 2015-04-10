function [ x,R ] = getIIDSamples(a,s,n)
    x = rand(1,n)*4 - 2;

    y = polyval(a,x);

    R = normrnd(y,s);
end

