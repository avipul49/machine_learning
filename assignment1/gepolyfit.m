function [ final ] = getpolyfit( n,x,R )
a1 = 1;
a2 = 1;
a3 = 1;
a4 = 1;

while(loss([a1 a2 a3 a4],n,x,R)>=0)
    
    
    tempa1 = a1 - 0.1*findSum([a1 a2 a3 a4 0 0 0],n,x,R,[1 0 0 0]);

    tempa2 = a2 - 0.1*findSum([a1 a2 a3 a4 0 0],n,x,R,[1 0 0]);

    tempa3 = a3 - 0.1*findSum([a1 a2 a3 a4 0],n,x,R,[1 0]);

    tempa4 = a4 - 0.1*findSum([a1 a2 a3 a4],n,x,R,1);

    if loss([tempa1,tempa2,tempa3,tempa4],n,x,R)>= loss([a1 a2 a3 a4],n,x,R)
        break;
    end
    a1 = tempa1;
    a2 = tempa2;
    a3 = tempa3;
    a4 = tempa4;

end

final = [a1 a2 a3 a4];

end

