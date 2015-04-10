function [ s ] = printpoly( p )

    s = '';
    psize = size(p,2);
    for i = 1: psize
        if(i==psize)
            s = strcat(s,sprintf(' %+.2f', p(i)));
        else
            s = strcat(s,sprintf(' %+.2fx^%d', p(i),psize-i));
        end
    end

end

