
Int expo(Int a, Int b){
    Int result = 1;
    while (b)
    {
        if (b&1)
        {
            result = (result*a)%MOD;
        }
        b >>=1 ;
        a = (a*a)%MOD;
    }

    return result;
}
